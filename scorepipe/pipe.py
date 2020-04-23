class ScorePipe:
    """
    The ScorePipe pipeline

    Determine the scoring path for a new scoring record or for batch scoring records.

    """

    def __init__(self):
        """
        """

        self.deployments = {}
        self.pre_prediction_func = None
        self.post_prediction_func = None
        self.partition_col = None

    def add_deployment(self, deployments=[]):
        """
        """
        for deployment in deployments:

            self.deployments[deployment.name] = {
            'deployment_obj': deployment
        }

        return self

    def pre_prediction(self, func):
        """
        """

        self.pre_prediction_func = pre_prediction_func

        return self

    def post_prediction(self, func):
        """
        """

        self.post_prediction_func = post_prediction_func

        return self
