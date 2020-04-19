from abc import ABC

class BaseDeployment(ABC):

    def __init__(self,name):

        self.name = name
