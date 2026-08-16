# ============================================================
# Frahoosh Mobile
# Professional Login Screen
# ============================================================

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class LoginScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(
            orientation="vertical",
            padding=[35, 45, 35, 35],
            spacing=18
        )

        # ----------------------------------------------------
        # Header
        # ----------------------------------------------------

        root.add_widget(
            Label(
                text="🏫 FRAHOOSH",
                font_size=34,
                bold=True,
                size_hint_y=None,
                height=70
            )
        )

        root.add_widget(
            Label(
                text="Smart Educational Management System",
                font_size=18,
                size_hint_y=None,
                height=45
            )
        )

        # ----------------------------------------------------
        # Welcome
        # ----------------------------------------------------

        root.add_widget(
            Label(
                text="Welcome",
                font_size=25,
                bold=True,
                size_hint_y=None,
                height=55
            )
        )

        root.add_widget(
            Label(
                text="Please login to continue",
                font_size=17,
                size_hint_y=None,
                height=40
            )
        )

        # ----------------------------------------------------
        # Username
        # ----------------------------------------------------

        self.username = TextInput(
            hint_text="Username",
            font_size=21,
            multiline=False,
            size_hint_y=None,
            height=65,
            padding=[18, 18]
        )

        root.add_widget(self.username)

        # ----------------------------------------------------
        # Password
        # ----------------------------------------------------

        self.password = TextInput(
            hint_text="Password",
            font_size=21,
            password=True,
            multiline=False,
            size_hint_y=None,
            height=65,
            padding=[18, 18]
        )

        root.add_widget(self.password)

        # ----------------------------------------------------
        # Login Button
        # ----------------------------------------------------

        login_button = Button(
            text="LOGIN",
            font_size=21,
            bold=True,
            size_hint_y=None,
            height=70
        )

        login_button.bind(
            on_press=self.login
        )

        root.add_widget(login_button)

        # ----------------------------------------------------
        # Footer
        # ----------------------------------------------------

        root.add_widget(
            Label(
                text="Frahoosh Mobile • Version 1.0.0",
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

            # Dashboard باید در main.py ثبت شده باشد
            self.manager.current = "dashboard"
