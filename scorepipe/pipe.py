class ScorePipe:
    """
    The ScorePipe pipeline

    Determine the scoring path for a new scoring record or batch scoring records

    """

    def __init__(self):

        self.models = {}

    def add_model(self, model_object):
        """
        """

        self.models[model_object.name] = {
            'object': model_object
        }

        return self
