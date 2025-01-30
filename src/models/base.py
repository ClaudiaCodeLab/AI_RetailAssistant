from abc import ABC, abstractmethod

class ChatModel(ABC):
    @abstractmethod
    def chat(self, messages):
        """Abstract method to be implemented by specific model integrations"""
        pass
