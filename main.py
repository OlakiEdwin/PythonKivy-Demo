from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton

class Demo(MDApp):

    def build(self):
        screen = Screen()

        l = MDLabel(text="HI PEOPLE!", halign='center',
                    theme_text_color="Custom",
                    text_color=(0.5, 0, 0.5, 1),
                    font_style='Caption')

        name = MDTextField(text="Enter name", pos_hint={
                        'center_x': 0.8, 'center_y': 0.8},
                           size_hint_x=None, width=100)