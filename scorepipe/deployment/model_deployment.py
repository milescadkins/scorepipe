from scorepipe.deployment.base_deployment import BaseDeployment

class ModelDeployment(BaseDeployment):

    """
    A deployment that .
    """

    def __init__(self,name):
        super().__init__(name) #Inherit from base_deployment.py

        self.champion_model = {}
        self.challenger_models = {}

    def add_models(self, champion, challengers=[]):
        """
        """

        self.champion_model[champion.name] = {
            str(0): champion
        }

        for i,challenger in enumerate(challengers):
            self.challenger_models[challenger.name] = {
                str(i+1): challenger
            }

        return self
