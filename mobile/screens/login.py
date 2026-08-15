# ============================================================
# Frahoosh Mobile
# صفحه ورود نسخه موبایل
# ============================================================

import os

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
FONT_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "Vazirmatn-Regular.ttf"
)


class LoginScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # ----------------------------------------------------
        # پس‌زمینه
        # ----------------------------------------------------

        with self.canvas.before:
            Color(0.04, 0.06, 0.10, 1)

            self.background = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[0]
            )

        self.bind(
            pos=self._update_background,
            size=self._update_background
        )

        # ----------------------------------------------------
        # صفحه اصلی
        # ----------------------------------------------------

        root = BoxLayout(
            orientation="vertical",
            padding=[30, 50, 30, 50],
            spacing=20
        )

        # ----------------------------------------------------
        # عنوان
        # ----------------------------------------------------

        title = Label(
            text="فراهوش",
            font_name=FONT_PATH,
            font_size=32,
            size_hint_y=None,
            height=70
        )

        root.add_widget(title)

        # ----------------------------------------------------
        # زیرعنوان
        # ----------------------------------------------------

        subtitle = Label(
            text="سامانه هوشمند آموزشی",
            font_name=FONT_PATH,
            font_size=20,
            size_hint_y=None,
            height=60
        )

        root.add_widget(subtitle)

        # ----------------------------------------------------
        # فضای خالی
        # ----------------------------------------------------

        root.add_widget(
            Label(
                text="",
                size_hint_y=1
            )
        )

        # ----------------------------------------------------
        # دکمه ورود
        # ----------------------------------------------------

        login_button = Button(
            text="ورود به فراهوش",
            font_name=FONT_PATH,
            font_size=20,
            size_hint_y=None,
            height=65
        )

        login_button.bind(
            on_press=self.login
        )

        root.add_widget(login_button)

        # ----------------------------------------------------
        # نسخه
        # ----------------------------------------------------

        version = Label(
            text="نسخه 1.0.0",
            font_name=FONT_PATH,
            font_size=14,
            size_hint_y=None,
            height=45
        )

        root.add_widget(version)

        self.add_widget(root)

    def _update_background(self, instance, value):
        self.background.pos = self.pos
        self.background.size = self.size

    def login(self, instance):
        self.manager.current = "dashboard"
