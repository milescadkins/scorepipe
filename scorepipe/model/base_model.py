from abc import ABC

class BaseModel(ABC):

    """
    A deployment that enacts a user defined rule as a function.
    """

    def __init__(self,name):

        self.name = name
