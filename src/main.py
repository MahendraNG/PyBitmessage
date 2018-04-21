from kivy.uix.popup import Popup
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
import xmlrpclib
import json
import time
from api import MySimpleXMLRPCRequestHandler

# api = xmlrpclib.ServerProxy("http://mahendracis:download1@192.168.2.139:8442/")

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.row = 2
        self.add_widget(Label(text='Message'))
        self.message = TextInput(multiline=False)
        self.add_widget(self.message)
        self.sendmessage = Button(text="send message", on_press=lambda a:self.send())
        self.add_widget(self.sendmessage)

    def send(self):
        MySimpleXMLRPCRequestHandler.HandleSendMessage('BM-2cUUx8HDzZkD6RTR4N6av5oUJZtmZFe8oR', 'BM-2cWYjpG3jK72mTcwGLjDhQPbx5eXjrqkaf', "testmahendra","prashanttest")
        # pass
        # ackData = api.sendMessage(
        #     'BM-2cUUx8HDzZkD6RTR4N6av5oUJZtmZFe8oR', 'BM-2cWYjpG3jK72mTcwGLjDhQPbx5eXjrqkaf', "test","test")
        # print 'The ackData is:', ackData

class MyApp(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()