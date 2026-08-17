# ============================================================
# Frahoosh Mobile
# Professional Login Screen
# ============================================================

import os

from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.core.text import LabelBase

from kivy.graphics import Color, RoundedRectangle


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

BACKGROUND_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "f20639fa-bd85-4a6e-aad1-913d61e16875.png"
)

FONT_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "B Titr Bold_0.ttf"
)

FONT_NAME = "Default"

try:
    if os.path.isfile(FONT_PATH):
        LabelBase.register(
            name="FrahooshBTitr",
            fn_regular=FONT_PATH
        )
        FONT_NAME = "FrahooshBTitr"
except Exception:
    FONT_NAME = "Default"


class LoginScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = FloatLayout()

        # ====================================================
        # BACKGROUND
        # ====================================================

        if os.path.isfile(BACKGROUND_PATH):

            background = Image(
                source=BACKGROUND_PATH,
                size_hint=(1, 1),
                allow_stretch=True,
                keep_ratio=False
            )

            root.add_widget(background)

        # ====================================================
        # LOGIN CARD
        # ====================================================

        card = BoxLayout(
            orientation="vertical",
            padding=[24, 22, 24, 22],
            spacing=10,
            size_hint=(0.82, None),
            height=390,
            pos_hint={
                "center_x": 0.5,
                "center_y": 0.38
            }
        )

        with card.canvas.before:

            Color(
                1,
                1,
                1,
                0.95
            )

            card_background = RoundedRectangle(
                pos=card.pos,
                size=card.size,
                radius=[22]
            )

        card.bind(
            pos=lambda obj, value:
            self.update_rect(card_background, obj)
        )

        card.bind(
            size=lambda obj, value:
            self.update_rect(card_background, obj)
        )

        # ====================================================
        # USERNAME
        # ====================================================

        self.username = TextInput(
            hint_text="نام کاربری",
            font_name=FONT_NAME,
            font_size=21,
            multiline=False,
            size_hint_y=None,
            height=62,
            padding=[18, 17],
            background_color=(0.94, 0.96, 0.98, 1),
            foreground_color=(0.05, 0.05, 0.05, 1)
        )

        card.add_widget(self.username)

        # ====================================================
        # PASSWORD
        # ====================================================

        self.password = TextInput(
            hint_text="رمز عبور",
            font_name=FONT_NAME,
            font_size=21,
            password=True,
            multiline=False,
            size_hint_y=None,
            height=62,
            padding=[18, 17],
            background_color=(0.94, 0.96, 0.98, 1),
            foreground_color=(0.05, 0.05, 0.05, 1)
        )

        card.add_widget(self.password)

        # ====================================================
        # OPTIONS
        # ====================================================

        options = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height=48,
            spacing=4
        )

        self.remember = CheckBox(
            size_hint=(None, 1),
            width=42
        )

        options.add_widget(self.remember)

        options.add_widget(
            Label(
                text="مرا بخاطر بسپار",
                font_name=FONT_NAME,
                font_size=18,
                color=(0.12, 0.12, 0.12, 1)
            )
        )

        forgot_button = Button(
            text="فراموشی رمز عبور",
            font_name=FONT_NAME,
            font_size=17,
            color=(0.05, 0.30, 0.70, 1),
            background_normal="",
            background_color=(0, 0, 0, 0)
        )

        forgot_button.bind(
            on_press=self.forgot_password
        )

        options.add_widget(forgot_button)

        card.add_widget(options)

        # ====================================================
        # LOGIN
        # ====================================================

        login_button = Button(
            text="ورود به فراهوش",
            font_name=FONT_NAME,
            font_size=23,
            bold=True,
            size_hint_y=None,
            height=68,
            background_normal="",
            background_color=(0.05, 0.32, 0.68, 1)
        )

        login_button.bind(
            on_press=self.login
        )

        card.add_widget(login_button)

        root.add_widget(card)

        self.add_widget(root)

    # ========================================================
    # RECTANGLE
    # ========================================================

    def update_rect(self, rect, widget):

        rect.pos = widget.pos
        rect.size = widget.size

    # ========================================================
    # LOGIN
    # ========================================================

    def login(self, instance):

        if self.manager:

            if self.remember.active:
                print("Frahoosh: remember user enabled")

            self.manager.current = "dashboard"

    # ========================================================
    # FORGOT PASSWORD
    # ========================================================

    def forgot_password(self, instance):

        print("Frahoosh: password recovery")
