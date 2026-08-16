# ============================================================
# Frahoosh Mobile
# Professional Persian Login
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
    "BTitr.ttf"
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
        # Background
        # ====================================================

        if os.path.isfile(BACKGROUND_PATH):

            background = Image(
                source=BACKGROUND_PATH,
                allow_stretch=True,
                keep_ratio=False,
                size_hint=(1, 1)
            )

            root.add_widget(background)

        # ====================================================
        # Dark Overlay
        # ====================================================

        with root.canvas.after:

            Color(
                0,
                0,
                0,
                0.20
            )

            overlay = RoundedRectangle(
                pos=root.pos,
                size=root.size
            )

        root.bind(
            pos=lambda instance, value:
            self.update_background(overlay, instance)
        )

        root.bind(
            size=lambda instance, value:
            self.update_background(overlay, instance)
        )

        # ====================================================
        # LOGIN CARD
        # ====================================================

        card = BoxLayout(
            orientation="vertical",
            padding=[28, 22, 28, 22],
            spacing=10,
            size_hint=(0.82, 0.68),
            pos_hint={
                "center_x": 0.5,
                "center_y": 0.52
            }
        )

        with card.canvas.before:

            Color(
                1,
                1,
                1,
                0.96
            )

            card_bg = RoundedRectangle(
                pos=card.pos,
                size=card.size,
                radius=[22]
            )

        card.bind(
            pos=lambda instance, value:
            self.update_background(card_bg, instance)
        )

        card.bind(
            size=lambda instance, value:
            self.update_background(card_bg, instance)
        )

        # ====================================================
        # APP NAME
        # ====================================================

        card.add_widget(
            Label(
                text="فراهوش",
                font_name=FONT_NAME,
                font_size=32,
                bold=True,
                color=(0.05, 0.18, 0.38, 1),
                size_hint_y=None,
                height=55
            )
        )

        # ====================================================
        # SCHOOL NAME
        # ====================================================

        card.add_widget(
            Label(
                text="دبیرستان سردارحاجی زاده ۲",
                font_name=FONT_NAME,
                font_size=20,
                color=(0.15, 0.15, 0.15, 1),
                size_hint_y=None,
                height=45
            )
        )

        # ====================================================
        # USERNAME
        # ====================================================

        self.username = TextInput(
            hint_text="نام کاربری",
            font_name=FONT_NAME,
            font_size=20,
            multiline=False,
            size_hint_y=None,
            height=62,
            padding=[18, 17],
            background_color=(0.93, 0.95, 0.98, 1),
            foreground_color=(0.05, 0.05, 0.05, 1)
        )

        card.add_widget(self.username)

        # ====================================================
        # PASSWORD
        # ====================================================

        self.password = TextInput(
            hint_text="رمز عبور",
            font_name=FONT_NAME,
            font_size=20,
            password=True,
            multiline=False,
            size_hint_y=None,
            height=62,
            padding=[18, 17],
            background_color=(0.93, 0.95, 0.98, 1),
            foreground_color=(0.05, 0.05, 0.05, 1)
        )

        card.add_widget(self.password)

        # ====================================================
        # REMEMBER + FORGOT PASSWORD
        # ====================================================

        options = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height=42,
            spacing=5
        )

        self.remember = CheckBox(
            size_hint=(None, 1),
            width=40
        )

        options.add_widget(self.remember)

        options.add_widget(
            Label(
                text="مرا بخاطر بسپار",
                font_name=FONT_NAME,
                font_size=17,
                color=(0.15, 0.15, 0.15, 1),
                halign="right"
            )
        )

        forgot = Button(
            text="فراموشی رمز عبور",
            font_name=FONT_NAME,
            font_size=16,
            color=(0.05, 0.30, 0.65, 1),
            background_normal="",
            background_color=(0, 0, 0, 0)
        )

        forgot.bind(
            on_press=self.forgot_password
        )

        options.add_widget(forgot)

        card.add_widget(options)

        # ====================================================
        # LOGIN BUTTON
        # ====================================================

        login_button = Button(
            text="ورود به فراهوش",
            font_name=FONT_NAME,
            font_size=22,
            bold=True,
            size_hint_y=None,
            height=66,
            background_normal="",
            background_color=(0.05, 0.32, 0.68, 1)
        )

        login_button.bind(
            on_press=self.login
        )

        card.add_widget(login_button)

        # ====================================================
        # VERSION
        # ====================================================

        card.add_widget(
            Label(
                text="نسخه ۱.۰.۰",
                font_name=FONT_NAME,
                font_size=14,
                color=(0.40, 0.40, 0.40, 1),
                size_hint_y=None,
                height=28
            )
        )

        root.add_widget(card)

        self.add_widget(root)

    # ========================================================
    # BACKGROUND
    # ========================================================

    def update_background(self, background, widget):

        background.pos = widget.pos
        background.size = widget.size

    # ========================================================
    # LOGIN
    # ========================================================

    def login(self, instance):

        if self.manager:
            self.manager.current = "dashboard"

    # ========================================================
    # FORGOT PASSWORD
    # ========================================================

    def forgot_password(self, instance):

        print("Frahoosh: Password recovery requested")
