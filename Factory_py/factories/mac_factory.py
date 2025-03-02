from factories.gui_factory import GUIFactory
from models.button import MacButton
from models.window import MacWindow

class MacFactory(GUIFactory):
    def create_button(self) -> MacButton:
        return MacButton()

    def create_window(self) -> MacWindow:
        return MacWindow()