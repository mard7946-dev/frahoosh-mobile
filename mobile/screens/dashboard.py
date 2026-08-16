# ============================================================
# Frahoosh Mobile
# داشبورد ساده و پایدار برای دمو
# ============================================================

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class DashboardScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(
            orientation="vertical",
            padding=[30, 40, 30, 40],
            spacing=20
        )

        root.add_widget(
            Label(
                text="Frahoosh",
                font_size=32,
                size_hint_y=None,
                height=70
            )
        )

        root.add_widget(
            Label(
                text="Welcome to Frahoosh",
                font_size=22,
                size_hint_y=None,
                height=60
            )
        )

        root.add_widget(
            Label(
                text="Login successful",
                font_size=18
            )
        )

        logout_button = Button(
            text="Logout",
            font_size=18,
            size_hint_y=None,
            height=60
        )

        logout_button.bind(
            on_press=self.logout
        )

        root.add_widget(logout_button)

        self.add_widget(root)

    def logout(self, instance):

        if self.manager:
            self.manager.current = "login"
