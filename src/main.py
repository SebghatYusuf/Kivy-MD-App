from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard


class MainApp(MDApp):

    def build(self):
        return MDLabel(text='HELLO', halign='center')


MainApp().run()
