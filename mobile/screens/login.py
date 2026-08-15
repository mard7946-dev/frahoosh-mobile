from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class LoginScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=15
        )

        root.add_widget(
            Label(
                text="فراهوش",
                font_size=32,
                size_hint_y=None,
                height=70
            )
        )

        root.add_widget(
            Label(
                text="سامانه هوشمند آموزشی",
                font_size=20,
                size_hint_y=None,
                height=60
            )
        )

        root.add_widget(
            Button(
                text="ورود آزمایشی",
                size_hint_y=None,
                height=60
            )
        )

        self.add_widget(root)
