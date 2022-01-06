from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import StringProperty, BooleanProperty

class WidgetsExample(GridLayout):
    counter = 0
    text_in_label = StringProperty("Hello!")
    enable_counter = BooleanProperty(False)

    def on_button_click(self):
        if self.enable_counter == True:
            self.counter += 1
            self.text_in_label = str(self.counter)

    def on_toggle_button_state(self, togle):
        print("togle state: " + togle.state)
        if togle.state == "normal":
            togle.text = "OFF"
            self.enable_counter = False    
        else:
            togle.text = "ON"
            self.enable_counter = True

# class CanvasExample1(Widget):
#     pass

class Main(App):
    pass





Main().run()