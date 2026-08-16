# ============================================================
# Frahoosh Mobile
# صفحه ورود - نسخه پایدار
# ============================================================

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


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
                font_size=32,
                bold=True,
                size_hint_y=None,
                height=70
            )
        )

        root.add_widget(
            Label(
                text="سامانه هوشمند آموزشی",
                font_size=20,
                size_hint_y=None,
                height=50
            )
        )

        self.username = TextInput(
            hint_text="نام کاربری",
            font_size=18,
            multiline=False,
            size_hint_y=None,
            height=60
        )

        root.add_widget(self.username)

        self.password = TextInput(
            hint_text="رمز عبور",
            font_size=18,
            password=True,
            multiline=False,
            size_hint_y=None,
            height=60
        )

        root.add_widget(self.password)

        login_button = Button(
            text="ورود به فراهوش",
            font_size=20,
            size_hint_y=None,
            height=65
        )

        login_button.bind(on_press=self.login)

        root.add_widget(login_button)

        root.add_widget(
            Label(
                text="نسخه 1.0.0",
                font_size=13,
                size_hint_y=None,
                height=35
            )
        )

        self.add_widget(root)

    def login(self, instance):
        # فعلاً فقط تست رابط ورود
        # تا زمانی که Dashboard را به ScreenManager اضافه نکرده‌ایم.
        pass
