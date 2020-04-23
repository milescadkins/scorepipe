from scorepipe.model_status import ModelStatus

class PredictionResult:
    """
    """

    def __init__(self):

        self.name = None
        self.status = DeploymentStatus.NA
        self.error = None
        self.prediction_values = None
