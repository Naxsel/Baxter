import socket               # Import socket module

"""
Client with GUI
"""


from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
ip = 'localhost'  # Get local machine name
port = 8080  # Reserve a port for your service.

def bttn1(instance):
    print('The button <%s> is being pressed' % instance.text)
    s.send("3")

def connect(instance):
    print('The button <%s> is being pressed' % instance.text)
    s.connect((ip, port))
    print s.recv(1024)

def toneutral(instance):
    print('The button <%s> is being pressed' % instance.text)
    s.send("1")

def sayHello(instance):
    print('The button <%s> is being pressed' % instance.text)
    s.send("2")

def disconnect(instance):
    print('The button <%s> is being pressed' % instance.text)
    s.send("0")
    s.close                     # Close the socket when done


class SuperButton(GridLayout):

    def __init__(self, **kwargs):
        super(SuperButton, self).__init__(**kwargs)
        self.cols = 2
        btn1= Button(text="Connect")
        btn1.bind(on_press=connect)
        self.button = btn1
        self.add_widget(self.button)
        btn2= Button(text="Test2")
        btn2.bind(on_press=bttn1)
        self.button = btn2
        self.add_widget(self.button)
        btn3= Button(text="Move to Neutral")
        btn3.bind(on_press=toneutral)
        self.button = btn3
        self.add_widget(self.button)
        btn4= Button(text="Hello Baxter")
        btn4.bind(on_press=sayHello)
        self.button = btn4
        self.add_widget(self.button)
        btn5= Button(text="Disconnect")
        btn5.bind(on_press=disconnect)
        self.button = btn5
        self.add_widget(self.button)

class MyApp(App):

    def build(self):
        return SuperButton()

if __name__ == '__main__':
    MyApp().run()