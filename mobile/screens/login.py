# ============================================================
# Frahoosh Mobile
# Professional Login
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
                size_hint=(1, 1),
                pos_hint={"x": 0, "y": 0}
            )

            root.add_widget(background)

        # ====================================================
        # Dark Transparent Layer
        # ====================================================

        with root.canvas.before:

            Color(
                0,
                0,
                0,
                0.25
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
        # Login Card
        # ====================================================

        card = BoxLayout(
            orientation="vertical",
            padding=[28, 28, 28, 28],
            spacing=14,
            size_hint=(0.88, 0.70),
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
                0.94
            )

            card_background = RoundedRectangle(
                pos=card.pos,
                size=card.size,
                radius=[22]
            )

        card.bind(
            pos=lambda instance, value:
            self.update_background(
                card_background,
                instance
            )
        )

        card.bind(
            size=lambda instance, value:
            self.update_background(
                card_background,
                instance
            )
        )

        # ====================================================
        # Title
        # ====================================================

        card.add_widget(
            Label(
                text="FRAHOOSH",
                font_size=36,
                bold=True,
                color=(0.08, 0.18, 0.35, 1),
                size_hint_y=None,
                height=65
            )
        )

        card.add_widget(
            Label(
                text="Smart Educational System",
                font_size=18,
                color=(0.25, 0.25, 0.25, 1),
                size_hint_y=None,
                height=40
            )
        )

        card.add_widget(
            Label(
                text="Welcome",
                font_size=25,
                bold=True,
                color=(0.08, 0.18, 0.35, 1),
                size_hint_y=None,
                height=48
            )
        )

        # ====================================================
        # Username
        # ====================================================

        self.username = TextInput(
            hint_text="Username",
            font_size=21,
            multiline=False,
            size_hint_y=None,
            height=64,
            padding=[18, 18],
            background_color=(0.94, 0.95, 0.97, 1),
            foreground_color=(0.08, 0.08, 0.08, 1),
            cursor_color=(0.08, 0.18, 0.35, 1)
        )

        card.add_widget(self.username)

        # ====================================================
        # Password
        # ====================================================

        self.password = TextInput(
            hint_text="Password",
            font_size=21,
            password=True,
            multiline=False,
            size_hint_y=None,
            height=64,
            padding=[18, 18],
            background_color=(0.94, 0.95, 0.97, 1),
            foreground_color=(0.08, 0.08, 0.08, 1),
            cursor_color=(0.08, 0.18, 0.35, 1)
        )

        card.add_widget(self.password)

        # ====================================================
        # Login Button
        # ====================================================

        login_button = Button(
            text="LOGIN",
            font_size=21,
            bold=True,
            size_hint_y=None,
            height=68,
            background_normal="",
            background_color=(0.08, 0.35, 0.70, 1)
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
                font_size=13,
                color=(0.35, 0.35, 0.35, 1),
                size_hint_y=None,
                height=30
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
    # Login
    # ========================================================

    def login(self, instance):

        if self.manager:
            self.manager.current = "dashboard"
