from scorepipe.deployment_status import DeploymentStatus

class PredictionResult:
    """
    """

    def __init__(self):

        self.name = None
        self.status = DeploymentStatus.NA
        self.error = None
        self.prediction_values = None
