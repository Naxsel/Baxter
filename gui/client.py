
import socket
import time
import kivy
kivy.require('1.9.1')


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


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
# ip = '192.168.1.54'  # Get local machine name
ip = "localhost"
port = 8080  # Reserve a port for your service.
cnt = "true"
dcnt = "false"


class MainScreen(Screen):
    def on_index(self, instance, value):
        tab = instance.current_slide.tab
        if self.TabbedPanel.current_tab != tab:
            self.TabbedPanel.switch_to(tab)

    def switch_to(self, header):
        # we have to replace the functionality of the original switch_to
        self.current_tab.state = "normal"
        header.state = 'down'
        self._current_tab = header

    def open_cilinder(self):
        global s
        s.send("1")
        s.recv(1024)

    def send2(self):
        global s
        s.send("2")

class ConnectionScreen(Screen):
    pass

class AboutScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    def connect(self):
        global s
        global cnt,dcnt
        cnt = 'false'
        dcnt = 'true'
        print ("Connecting to the Baxter...")
        s.connect((ip, port))
        print ("hola")
        print s.recv(1024)
        self.current = "main"

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

presentation = Builder.load_file("main.kv")

class BaxterGUIApp(App):
    def cnt(self):
        return cnt
    def dcnt(self):
        return dcnt
    def build(self):
        return presentation

BaxterGUIApp().run()