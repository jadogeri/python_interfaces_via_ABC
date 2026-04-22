from abc import ABC, abstractmethod
class Bird(ABC):
    @abstractmethod
    def eat(self):
        pass
