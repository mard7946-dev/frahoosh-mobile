# ============================================================
# Frahoosh Mobile
# صفحه ورود نسخه موبایل
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


# ------------------------------------------------------------
# بارگذاری ایمن فونت فارسی
# ------------------------------------------------------------

try:
    if os.path.isfile(FONT_PATH):
        LabelBase.register(
            name="VazirFrahoosh",
            fn_regular=FONT_PATH
        )
        FONT_NAME = "VazirFrahoosh"
except Exception:
    FONT_NAME = "Default"


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
                text="فراهوش",
                font_name=FONT_NAME,
                font_size=32,
                size_hint_y=None,
                height=70
            )
        )

        root.add_widget(
            Label(
                text="سامانه هوشمند آموزشی",
                font_name=FONT_NAME,
                font_size=20,
                size_hint_y=None,
                height=60
            )
        )

        root.add_widget(
            Label(
                text="",
                size_hint_y=1
            )
        )

        login_button = Button(
            text="ورود به فراهوش",
            font_name=FONT_NAME,
            font_size=20,
            size_hint_y=None,
            height=65
        )

        login_button.bind(
            on_press=self.login
        )

        root.add_widget(login_button)

        root.add_widget(
            Label(
                text="نسخه 1.0.0",
                font_name=FONT_NAME,
                font_size=14,
                size_hint_y=None,
                height=45
            )
        )

        self.add_widget(root)

    def login(self, instance):

        if self.manager:
            self.manager.current = "dashboard"
