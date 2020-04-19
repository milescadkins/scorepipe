from scorepipe.model_deployment.base_deployment import BaseDeployment

class RuleDeployment(BaseDeployment):

    """
    A deployment that enacts a user defined rule as a function.
    """

    def __init__(self,name,rule_func):
        super().__init__(name) #Inherit from base_deployment.py

        self.rule_function = rule_func #A function that will trigger something
