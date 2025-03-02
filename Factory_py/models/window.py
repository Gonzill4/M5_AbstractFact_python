from abc import ABC, abstractmethod

class Window(ABC):
    @abstractmethod
    def show(self):
        pass

class WindowsWindow(Window):
    def show(self):
        return "Displaying Windows Window"
    
    def windows_specific_feature(self):
        return "Windows Window supports Aero Snap"

class MacWindow(Window):
    def show(self):
        return "Displaying Mac Window"
    
    def mac_specific_feature(self):
        return "Mac Window has a translucent title bar"

class LinuxWindow(Window):
    def show(self):
        return "Displaying Linux Window"
    
    def linux_specific_feature(self):
        return "Linux Window supports tiling window managers"
