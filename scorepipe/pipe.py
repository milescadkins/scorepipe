class ScorePipe:
    """
    The ScorePipe pipeline

    Determine the scoring path for a new scoring record or for batch scoring records.

    """

    def __init__(self):

        self.model_deployments = {}

    def add_deployment(self, model_deployment_object):
        """
        """

        self.model_deployments[model_deployment_object.name] = {
            'model_deployment_object': model_deployment_object
        }

        return self









        """
            Code to implement later on..
        """

    def init(self):
        """
        Initialize the maestro harness.
        This method must be called before calling  :func:`PredictionMaestro.predict`

        :return: self
        """
        if self._pre_prediction_func is None:
            prepost_obj = DupPrePost()
            self._pre_prediction_func = prepost_obj.pre_prediction
        if self._post_prediction_func is None:
            prepost_obj = DupPrePost()
            self._post_prediction_func = prepost_obj.post_prediction
        if len(self._predictors) == 0:
            raise Exception("No predictor was added")

        self._init_called = True

        process_predictors = sum(map(lambda x: int(self._predictors[x]["obj"].is_cpu_intensive()), self._predictors))
        thread_predictors = len(self._predictors) - process_predictors

        if thread_predictors > 0:
            self._thread_executor = \
                concurrent.futures.ThreadPoolExecutor(max_workers=thread_predictors)
        if process_predictors > 0:
            self._process_executor = \
                concurrent.futures.ProcessPoolExecutor(max_workers=process_predictors)

        self._init_model_delivery()

    def predict(self, input_dataframe, **kwargs):
        """
        Perform a prediction using the registered predictors.
        The harness will send the data to the predictors according to the harness mode.
        See :func:`PredictionMaestro.partition_mode` for more details.


        :param input_dataframe: Dataframe to use as input data for predictions
        :param kwargs:
        :return: a list of :class:`prediction_maestro.PredictorResult`
        """

        self._predict_sanity_check()

        prediction_input = {
            "input_dataframe": input_dataframe,
            "kwargs": kwargs,
            "per_pred_input": {}
        }

        pred_instance = self._init_pred_instance(prediction_input)
        self._start_predictions(pred_instance)
        self._prediction_wait_loop(pred_instance)
        predictions = self._prepare_results(pred_instance)

        for p_name in pred_instance.predictors_to_use:
            p_info = pred_instance.info[p_name]
            self._logger.debug(p_info)

        self._update_stats(pred_instance)
        self._mlops_report(pred_instance)
        return predictions
