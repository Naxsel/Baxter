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
        # set the carousel to load  the appropriate slide
        # saved in the screen attribute of the tab head
        self.carousel.index = header.slide


class ConnectionScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("main.kv")

class BaxterGUIApp(App):
    def build(self):
        return presentation

BaxterGUIApp().run()