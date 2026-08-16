# ============================================================
# Frahoosh Mobile
# صفحه ورود نسخه پایدار با فونت فارسی
# ============================================================

import os

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from kivy.core.text import LabelBase


# ------------------------------------------------------------
# مسیر فونت فارسی
# ------------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

FONT_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "Vazirmatn-Regular (1).ttf"
)

FONT_NAME = "Default"

try:
    if os.path.isfile(FONT_PATH):
        LabelBase.register(
            name="FrahooshVazir",
            fn_regular=FONT_PATH
        )
        FONT_NAME = "FrahooshVazir"
except Exception:
    FONT_NAME = "Default"


class LoginScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(
            orientation="vertical",
            padding=[30, 40, 30, 40],
            spacing=18
        )

        # ----------------------------------------------------
        # عنوان
        # ----------------------------------------------------

        root.add_widget(
            Label(
                text="فراهوش",
                font_name=FONT_NAME,
                font_size=32,
                bold=True,
                size_hint_y=None,
                height=70
            )
        )

        # ----------------------------------------------------
        # زیرعنوان
        # ----------------------------------------------------

        root.add_widget(
            Label(
                text="سامانه هوشمند آموزشی",
                font_name=FONT_NAME,
                font_size=20,
                size_hint_y=None,
                height=55
            )
        )

        # ----------------------------------------------------
        # نام کاربری
        # ----------------------------------------------------

        self.username = TextInput(
            hint_text="نام کاربری",
            font_name=FONT_NAME,
            font_size=18,
            multiline=False,
            size_hint_y=None,
            height=60,
            padding=[15, 15]
        )

        root.add_widget(self.username)

        # ----------------------------------------------------
        # رمز عبور
        # ----------------------------------------------------

        self.password = TextInput(
            hint_text="رمز عبور",
            font_name=FONT_NAME,
            font_size=18,
            password=True,
            multiline=False,
            size_hint_y=None,
            height=60,
            padding=[15, 15]
        )

        root.add_widget(self.password)

        # ----------------------------------------------------
        # دکمه ورود
        # ----------------------------------------------------

        login_button = Button(
            text="ورود به فراهوش",
            font_name=FONT_NAME,
            font_size=20,
            size_hint_y=None,
            height=65
        )

        login_button.bind(on_press=self.login)

        root.add_widget(login_button)

        # ----------------------------------------------------
        # نسخه
        # ----------------------------------------------------

        root.add_widget(
            Label(
                text="نسخه 1.0.0",
                font_name=FONT_NAME,
                font_size=13,
                size_hint_y=None,
                height=35
            )
        )

        self.add_widget(root)

    # --------------------------------------------------------
    # ورود - فعلاً فقط تست
    # --------------------------------------------------------

    def login(self, instance):
        # Dashboard هنوز در main.py ثبت نشده است.
        # بنابراین فعلاً هیچ Screen دیگری را صدا نمی‌زنیم.
        pass
