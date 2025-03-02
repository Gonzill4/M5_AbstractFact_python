from factories.gui_factory import GUIFactory
from models.button import LinuxButton
from models.window import LinuxWindow

class LinuxFactory(GUIFactory):
    def create_button(self) -> LinuxButton:
        return LinuxButton()

    def create_window(self) -> LinuxWindow:
        return LinuxWindow()