class ScorePipe:
    """
    The ScorePipe pipeline

    Determine the scoring path for a new scoring record or for batch scoring records

    """

    def __init__(self):

        self.model_deployments = {}

    def add_model(self, model_deployment_object):
        """
        """

        self.model_deployments[model_deployment_object.name] = {
            'model_deployment_object': model_deployment_object
        }

        return self
