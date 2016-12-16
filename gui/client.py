
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


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
ip = '192.168.1.54'  # Get local machine name
port = 8080  # Reserve a port for your service.

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

    def disconnect(self):
        global s
        s.send("0")
        s.close()
        print ("Closed Connection")
        self.parent.current="Connection"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # reset socket object

    def open_cilinder(self):
        global s
        s.send("1")
        s.recv(1024)

class ConnectionScreen(Screen):
    def connect(self):
        global s
        print ("Connecting to the Baxter...")
        s.connect((ip, port))
        print ("hola")
        print s.recv(1024)
        self.parent.current = "main"

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("main.kv")

class BaxterGUIApp(App):
    def build(self):
        return presentation

BaxterGUIApp().run()