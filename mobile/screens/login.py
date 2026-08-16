# ============================================================
# Frahoosh Mobile
# Professional Login Screen
# Stable Version
# ============================================================

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class LoginScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # ====================================================
        # Main
        # ====================================================

        root = BoxLayout(
            orientation="vertical",
            padding=[35, 55, 35, 40],
            spacing=18
        )

        # ====================================================
        # Logo / Title
        # ====================================================

        root.add_widget(
            Label(
                text="FRAHOOSH",
                font_size=38,
                bold=True,
                size_hint_y=None,
                height=75
            )
        )

        root.add_widget(
            Label(
                text="Smart Educational System",
                font_size=21,
                size_hint_y=None,
                height=48
            )
        )

        root.add_widget(
            Label(
                text="Welcome",
                font_size=27,
                bold=True,
                size_hint_y=None,
                height=55
            )
        )

        root.add_widget(
            Label(
                text="Please enter your account information",
                font_size=17,
                size_hint_y=None,
                height=40
            )
        )

        # ====================================================
        # Username
        # ====================================================

        self.username = TextInput(
            hint_text="Username",
            font_size=22,
            multiline=False,
            size_hint_y=None,
            height=70,
            padding=[20, 20]
        )

        root.add_widget(self.username)

        # ====================================================
        # Password
        # ====================================================

        self.password = TextInput(
            hint_text="Password",
            font_size=22,
            password=True,
            multiline=False,
            size_hint_y=None,
            height=70,
            padding=[20, 20]
        )

        root.add_widget(self.password)

        # ====================================================
        # Login Button
        # ====================================================

        login_button = Button(
            text="LOGIN",
            font_size=23,
            bold=True,
            size_hint_y=None,
            height=75
        )

        login_button.bind(
            on_press=self.login
        )

        root.add_widget(login_button)

        # ====================================================
        # Footer
        # ====================================================

        root.add_widget(
            Label(
                text="FRAHOOSH MOBILE  •  VERSION 1.0.0",
                font_size=14,
                size_hint_y=None,
                height=40
            )
        )

        self.add_widget(root)

    # ========================================================
    # Login
    # ========================================================

    def login(self, instance):

        if self.manager:
            self.manager.current = "dashboard"
