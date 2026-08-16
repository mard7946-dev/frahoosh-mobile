# ============================================================
# Frahoosh Mobile
# Professional Login - Compact Mobile UI
# ============================================================

import os

from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from kivy.graphics import Color, RoundedRectangle


class LoginScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = FloatLayout()

        # ====================================================
        # Background
        # ====================================================

        base_dir = os.path.dirname(os.path.dirname(__file__))

        background_path = os.path.join(
            base_dir,
            "assets",
            "background.png"
        )

        if os.path.isfile(background_path):

            background = Image(
                source=background_path,
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
                0.18
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
            padding=[24, 24, 24, 24],
            spacing=12,
            size_hint=(0.82, 0.62),
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
                radius=[24]
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
        # Title
        # ====================================================

        card.add_widget(
            Label(
                text="FRAHOOSH",
                font_size=34,
                bold=True,
                color=(0.06, 0.18, 0.38, 1),
                size_hint_y=None,
                height=58
            )
        )

        card.add_widget(
            Label(
                text="Smart Educational System",
                font_size=17,
                color=(0.25, 0.25, 0.25, 1),
                size_hint_y=None,
                height=36
            )
        )

        card.add_widget(
            Label(
                text="Welcome",
                font_size=24,
                bold=True,
                color=(0.06, 0.18, 0.38, 1),
                size_hint_y=None,
                height=42
            )
        )

        # ====================================================
        # Username
        # ====================================================

        self.username = TextInput(
            hint_text="Username",
            font_size=20,
            multiline=False,
            size_hint_y=None,
            height=60,
            padding=[18, 17],
            background_color=(0.93, 0.95, 0.98, 1),
            foreground_color=(0.05, 0.05, 0.05, 1)
        )

        card.add_widget(self.username)

        # ====================================================
        # Password
        # ====================================================

        self.password = TextInput(
            hint_text="Password",
            font_size=20,
            password=True,
            multiline=False,
            size_hint_y=None,
            height=60,
            padding=[18, 17],
            background_color=(0.93, 0.95, 0.98, 1),
            foreground_color=(0.05, 0.05, 0.05, 1)
        )

        card.add_widget(self.password)

        # ====================================================
        # Login
        # ====================================================

        login_button = Button(
            text="LOGIN",
            font_size=21,
            bold=True,
            size_hint_y=None,
            height=62,
            background_normal="",
            background_color=(0.06, 0.32, 0.68, 1)
        )

        login_button.bind(
            on_press=self.login
        )

        card.add_widget(login_button)

        # ====================================================
        # Footer
        # ====================================================

        card.add_widget(
            Label(
                text="FRAHOOSH MOBILE  •  1.0.0",
                font_size=12,
                color=(0.40, 0.40, 0.40, 1),
                size_hint_y=None,
                height=28
            )
        )

        root.add_widget(card)

        self.add_widget(root)

    # ========================================================
    # Background Helper
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
