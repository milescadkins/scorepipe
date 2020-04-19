from prediction_maestro.predictor.base_predictor import BasePredictor
from scorepipe.model_deployment.base_deployment import BaseDeployment

class RuleDeployment(BaseDeployment):

    def __init__(self):

        self.name = 'rule'
