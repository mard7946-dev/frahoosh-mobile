# ============================================================
# Frahoosh Mobile
# داشبورد اصلی نسخه موبایل
# ============================================================

import os

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
FONT_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "Vazirmatn-Regular.ttf"
)


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
                font_name=FONT_PATH,
                font_size=32,
                size_hint_y=None,
                height=70
            )
        )

        root.add_widget(
            Label(
                text="به سامانه فراهوش خوش آمدید",
                font_name=FONT_PATH,
                font_size=20,
                size_hint_y=None,
                height=60
            )
        )

        root.add_widget(
            Label(
                text="داشبورد اصلی",
                font_name=FONT_PATH,
                font_size=18
            )
        )

        students_button = Button(
            text="دانش‌آموزان",
            font_name=FONT_PATH,
            font_size=18,
            size_hint_y=None,
            height=60
        )

        root.add_widget(students_button)

        teachers_button = Button(
            text="دبیران",
            font_name=FONT_PATH,
            font_size=18,
            size_hint_y=None,
            height=60
        )

        root.add_widget(teachers_button)

        logout_button = Button(
            text="خروج از حساب",
            font_name=FONT_PATH,
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
        self.manager.current = "login"
