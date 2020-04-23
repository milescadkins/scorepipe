from scorepipe.model.base_model import BaseModel
from scorepipe.model_status import ModelStatus
from scorepipe.prediction_result import PredictionResult

class Rule(BaseModel):

    """
    A deployment that enacts a user defined rule as a function.
    """

    def __init__(self,name,func):
        super().__init__(name) #Inherit from base_deployment.py

        self.rule_func = func #A function that will trigger something

    def predict(self, X):

        prediction_result = PredictionResult()

        #Try making a prediction
        try:
            status = ModelStatus.IN_PROGRESS
            predictions = self.rule_func(X)
            status = ModelStatus.OK
            prediction_result.prediction_values = predictions
        except Exception as e:
            status = DeploymentStatus.FAIL
            prediction_result.error = str(e)

        return prediction_result
