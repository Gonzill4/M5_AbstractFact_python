from factories.gui_factory import GUIFactory
from models.button import WindowsButton
from models.window import WindowsWindow

class WindowsFactory(GUIFactory):
    def create_button(self) -> WindowsButton:
        return WindowsButton()

    def create_window(self) -> WindowsWindow:
        return WindowsWindow()