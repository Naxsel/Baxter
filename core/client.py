import socket               # Import socket module

"""
Client with GUI
"""


from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


def connect(instance):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        # Create a socket object
    ip = 'localhost'         # Get local machine name
    port = 8080                 # Reserve a port for your service.

    s.connect((ip, port))
    print s.recv(1024)
    print "Conected to Baxter!"
    s.close                     # Close the socket when done

def bttn1(instance):
    print('The button <%s> is being pressed' % instance.text)

class SuperButton(GridLayout):

    def __init__(self, **kwargs):
        super(SuperButton, self).__init__(**kwargs)
        self.cols = 2
        btn1= Button(text="Prueba")
        btn1.bind(on_press=bttn1)
        self.button = btn1
        self.add_widget(self.button)
        btn2= Button(text="Conexion")
        btn2.bind(on_press=connect)
        self.button = btn2
        self.add_widget(self.button)

class MyApp(App):

    def build(self):
        return SuperButton()

if __name__ == '__main__':
    MyApp().run()