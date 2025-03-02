from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class WindowsButton(Button):
    def render(self):
        return "Rendering Windows Button"
    
    def windows_specific_feature(self):
        return "Windows Button has a right-click menu"

class MacButton(Button):
    def render(self):
        return "Rendering Mac Button"
    
    def mac_specific_feature(self):
        return "Mac Button supports force touch"

class LinuxButton(Button):
    def render(self):
        return "Rendering Linux Button"
    
    def linux_specific_feature(self):
        return "Linux Button supports customizable shortcuts"