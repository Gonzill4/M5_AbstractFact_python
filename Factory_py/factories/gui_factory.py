from abc import ABC, abstractmethod
from models.button import Button
from models.window import Window

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_window(self) -> Window:
        pass

