# ============================================================
# Frahoosh Mobile
# داشبورد تست ورود
# ============================================================

import os

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.text import LabelBase


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
FONT_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "Vazirmatn-Regular.ttf"
)

FONT_NAME = "Default"

try:
    if os.path.isfile(FONT_PATH):
        LabelBase.register(
            name="VazirFrahooshDashboard",
            fn_regular=FONT_PATH
        )
        FONT_NAME = "VazirFrahooshDashboard"
except Exception:
    FONT_NAME = "Default"


class DashboardScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        root.add_widget(
            Label(
                text="فراهوش",
                font_name=FONT_NAME,
                font_size=32,
                size_hint_y=None,
                height=70
            )
        )

        root.add_widget(
            Label(
                text="به فراهوش خوش آمدید",
                font_name=FONT_NAME,
                font_size=22,
                size_hint_y=None,
                height=60
            )
        )

        root.add_widget(
            Label(
                text="ورود با موفقیت انجام شد",
                font_name=FONT_NAME,
                font_size=18
            )
        )

        logout_button = Button(
            text="خروج",
            font_name=FONT_NAME,
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
