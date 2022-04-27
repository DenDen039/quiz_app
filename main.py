from urllib.parse import ParseResultBytes
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty,ReferenceListProperty, ObjectProperty
from  kivy.vector import Vector
from kivy.clock import Clock
from random import randint
import time
Builder.load_file("QuizApp.kv")

class Menu(Widget):
    def GotoGameList(self):
        pass
    def GotoStats(self):
        pass
    def GotoCreativeMode(self):
        pass
    def __init__(self):
        super(Menu,self).__init__()


class QuizApp(App):
    def build(self):
        return Menu()

if __name__ ==  "__main__":
    QuizApp().run()