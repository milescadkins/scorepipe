from scorepipe.model_deployment.base_deployment import BaseDeployment
from scorepipe.deployment_status import DeploymentStatus
from scorepipe.prediction_result import PredictionResult
class RuleDeployment(BaseDeployment):

    """
    A deployment that enacts a user defined rule as a function.
    """

    def __init__(self,name,rule_func):
        super().__init__(name) #Inherit from base_deployment.py

        self.rule_function = rule_func #A function that will trigger something

    def predict(self, input_dataframe):
        prediction_result = PredictionResult()
        try:
            predictions = self.rule_function(input_dataframe)
            status = PredictionStatus.OK
            prediction_result.prediction_values = predictions
        except Exception as e:
            status = DeploymentStatus.FAIL
            prediction_result.error = str(e)

        return prediction_result
