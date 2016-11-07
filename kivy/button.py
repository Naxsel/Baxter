from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


def callback(instance):
    print('The button <%s> is being pressed' % instance.text)

class SuperButton(GridLayout):

    def __init__(self, **kwargs):
        super(SuperButton, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Baxter'))
        btn1= Button(text="boton de prueba")
        btn1.bind(on_press=callback)
        self.button = btn1
        self.add_widget(self.button)

class MyApp(App):

    def build(self):
        return SuperButton()


if __name__ == '__main__':
    MyApp().run()