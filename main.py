from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(selfself):
        return Button(text="Hello!")

MyApp().run()
