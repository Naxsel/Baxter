
import socket
import time
import kivy
kivy.require('1.9.1')

"""
Client side of Baxter GUI
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, ObjectProperty,NumericProperty
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.actionbar import ActionBar
from kivy.uix.actionbar import ActionView
from kivy.uix.actionbar import ActionButton
from kivy.uix.actionbar import ActionPrevious


# Global vars
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
ip = 'localhost'  # Get local machine name
# ip = "10.108.10.29"
port = 8080  # Reserve a port for your service.
cnt = "true"
dcnt = "false"


# Class definition
class MainScreen(Screen):
    global s

    def on_index(self, instance, value):
        tab = instance.current_slide.tab
        if self.TabbedPanel.current_tab != tab:
            self.TabbedPanel.switch_to(tab)

    def switch_to(self, header):
        self.current_tab.state = "normal"
        header.state = 'down'
        self._current_tab = header

    def enable_robot(self):
        global s

    def disable_robot(self):
        global s

    def move_to_neutral(self):
        global s

    def hello_baxter(self):
        global s

    def open_cylinder(self):
        global s
        s.send("1")
        s.recv(1024)

    def camera_stream(self):
        global s

    def send2(self):
        s.send("2")

class ConnectionScreen(Screen):
    pass

class AboutScreen(Screen):
    pass

# Screen management functions
class ScreenManagement(ScreenManager):

    # Connection with the server
    def connect(self):
        global s
        global cnt,dcnt
        cnt = 'false'
        dcnt = 'true'
        print ("Connecting to the Baxter...")
        s.connect((ip, port))
        print ("Hey")
        print s.recv(1024)
        self.current = "main"

    # Disconnection from the server
    def disconnect(self):
        global s
        global cnt,dcnt
        cnt = 'true'
        dcnt = 'false'
        s.send("0")
        s.close()
        print ("Closed Connection")
        self.current="Connection"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # reset socket object

    def about(self):
        self.current="About"

    def back(self):
        self.current="Connection"


class ConnectBar(ActionBar):
    pass

class DisconnectBar(ActionBar):
    pass

class AboutBar(ActionBar):
    pass

class Manager1(ScreenManager):
    pass

class Manager2(ScreenManager):
    pass

class EssentialScreen(Screen):
    pass

class EssentialList(BoxLayout):
    pass

class EssentialScreen1(Screen):
    def run(self):
        global s

class EssentialScreen2(Screen):
    def run(self):
        global s

class EssentialScreen3(Screen):
    def run(self):
        global s
        s.send("2")

class EssentialScreen4(Screen):
    pass

class EssentialScreen5(Screen):
    pass

class CustomScreen(Screen):
    pass

class CustomList(BoxLayout):
    pass

class HelloScreen(Screen):
    def run(self):
        global s

class OpenCylinderScreen(Screen):
    def run(self):
        global s
        s.send("1")
        s.recv(1024)

class CameraStreamScreen(Screen):
    def run(self):
        global s


# Main kivy file, all the interface design is done through it
presentation = Builder.load_file("main.kv")

class BaxterGUIApp(App):
    def cnt(self):
        return cnt
    def dcnt(self):
        return dcnt
    def build(self):
        return presentation

BaxterGUIApp().run()