from typing import Text
from kivy.app import App
from kivy.uix.behaviors import button
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

class Ip_app(App):
    def build(self):
        #hauptfenster
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.95, 0.95)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}

        #image 
        self.image = Image(source= "resources/photo_2022-01-01_10-46-11.jpg")
        self.image.size_hint = (1, None)

        #self.image.width = "400dp"
        self.image.height = "400dp"
        self.window.add_widget(self.image)

        #Label
        self.greeting = Label(
            text = "Hi honey, what is your name: ",
            font_size = 22,
            size_hint= (1,0.5),
            color = '#00FFCE',
            bold = True
            )
        self.window.add_widget(self.greeting)

        #input
        self.user_name = TextInput(
            multiline = False,
            size_hint= (1,0.5),
            font_size = 20
            )
        self.window.add_widget(self.user_name)

        #knopf zum klicken hier gleich mit nächste function Callback eingebunden
        self.button = Button(
            text = "submmit",
            size_hint= (1,0.5),
            bold= True,
            background_color ='#00FFCE'
            )
        self.button.bind(on_press = self.callback) 
        self.window.add_widget(self.button)

        return self.window

    def callback(self, action):
        self.greeting.text = "Hello" + " " + self.user_name.text + "!"
        
if __name__ == "__main__":
    Ip_app().run()


