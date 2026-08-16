# ============================================================
# Frahoosh Mobile
# صفحه ورود نسخه موبایل
# ============================================================

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
            spacing=20
        )

        root.add_widget(
            Label(
                text="Frahoosh",
                font_size=32,
                bold=True,
                size_hint_y=None,
                height=70
            )
        )

        root.add_widget(
            Label(
                text="Frahoosh Mobile",
                font_size=22,
                size_hint_y=None,
                height=60
            )
        )

        root.add_widget(
            Label(
                text="سامانه هوشمند آموزشی",
                font_size=18,
                size_hint_y=None,
                height=60
            )
        )

        root.add_widget(
            Label(
                text="برای ورود به برنامه دکمه زیر را بزنید",
                font_size=16
            )
        )

        login_button = Button(
            text="ورود به فراهوش",
            font_size=20,
            size_hint_y=None,
            height=65
        )

        login_button.bind(
            on_press=self.login
        )

        root.add_widget(login_button)

        self.add_widget(root)

    def login(self, instance):

        if self.manager.has_screen("dashboard"):
            self.manager.current = "dashboard"
