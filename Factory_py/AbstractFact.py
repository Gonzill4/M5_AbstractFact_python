# Patrón Abstract Factory - M5 

from factories.windows_factory import WindowsFactory
from factories.mac_factory import MacFactory
from factories.linux_factory import LinuxFactory
from factories.gui_factory import GUIFactory

class Application:
    def __init__(self, factory: GUIFactory):
        self.button = factory.create_button()
        self.window = factory.create_window()
    
    def run(self):
        print(self.button.render())
        print(self.window.show())

# Function to get the right factory
def get_factory(os_type: str) -> GUIFactory:
    factories = {
        "Windows": WindowsFactory,
        "Mac": MacFactory,
        "Linux": LinuxFactory
    }
    return factories.get(os_type, WindowsFactory)()

if __name__ == "__main__":
    os_type = input("Enter OS (Windows/Mac/Linux): ")
    factory = get_factory(os_type)
    app = Application(factory)
    app.run()
