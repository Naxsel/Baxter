import time
import kivy
kivy.require('1.9.1')


from kivy.app import App
from kivy.properties import StringProperty, ObjectProperty,NumericProperty
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout



Builder.load_string('''
<MainMenu>:
    carousel: carousel
    do_default_tab: False
    tab_pos: 'top_mid'
    tab_width: 750/3
    Carousel:
        on_index: root.on_index(*args)
        id: carousel
        BoxLayout:
            orientation: 'horizontal'
            tab: tab1
            Button:
                text: 'Slide one'
                size_hint: .5,1
                on_press: app.do_sleep()
            Button:
                text: 'Slide 4'
                on_press: print "Slide 4 pressed"
        Button:
            text: 'Slide Two'
            tab: tab2
        Button:
            text: 'Slide three'
            tab: tab3

    TabbedPanelItem:
        id: tab1
        text: 'Baxter Essentials'
        slide: 0

    TabbedPanelItem:
        id: tab2
        text: 'Custom Scripts'
        slide: 1
    TabbedPanelItem:
        id: tab3
        text: 'About'
        slide: 2
''')

class MainMenu(TabbedPanel):

    def on_index(self, instance, value):
        tab = instance.current_slide.tab
        if self.current_tab != tab:
            self.switch_to(tab)

    def switch_to(self, header):
        # we have to replace the functionality of the original switch_to
        self.current_tab.state = "normal"
        header.state = 'down'
        self._current_tab = header
        # set the carousel to load  the appropriate slide
        # saved in the screen attribute of the tab head
        self.carousel.index = header.slide


class BaxterGUIApp(App):

    def build(self):
        return MainMenu()

    def do_sleep(self):
        App.get_running_app().root.disabled = False
        time.sleep(2)

        # App.get_running_app().root.disabled= False


if __name__ == '__main__':
    BaxterGUIApp().run()