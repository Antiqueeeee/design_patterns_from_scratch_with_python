from abc import ABC, abstractmethod
class base_operation(ABC):
    def __init__(self, target_1, target_2):
        self.target_1 = target_1
        self.target_2 = target_2
    
    @abstractmethod
    def calculating():
        pass

class invalid_operation(base_operation):
    def __init__(self, target_1, target_2):
        super().__init__(target_1, target_2)
    def calculating(self):
        return f"The operator you is invalid."

class add_operation(base_operation):
    def __init__(self, target_1, target_2):
        super().__init__(target_1, target_2)

    def calculating(self):
        return self.target_1 + self.target_2

