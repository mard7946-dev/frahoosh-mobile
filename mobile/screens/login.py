# ============================================================
# Frahoosh Mobile
# صفحه ورود نسخه موبایل
# ============================================================

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

from config import APP_NAME, SYSTEM_TITLE, APP_VERSION


class LoginScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=15
        )

        root.add_widget(
            Label(
                text=APP_NAME,
                font_size=32,
                bold=True,
                size_hint_y=None,
                height=70
            )
        )

        root.add_widget(
            Label(
                text=SYSTEM_TITLE,
                font_size=18,
                size_hint_y=None,
                height=60
            )
        )

        self.username = TextInput(
            hint_text="نام کاربری",
            multiline=False,
            size_hint_y=None,
            height=55
        )

        self.password = TextInput(
            hint_text="رمز عبور",
            password=True,
            multiline=False,
            size_hint_y=None,
            height=55
        )

        root.add_widget(self.username)
        root.add_widget(self.password)

        login_button = Button(
            text="ورود به فراهوش",
            size_hint_y=None,
            height=60
        )

        login_button.bind(on_press=self.login)

        root.add_widget(login_button)

        root.add_widget(
            Label(
                text=f"نسخه {APP_VERSION}",
                font_size=14
            )
        )

        self.add_widget(root)

    def login(self, instance):

        username = self.username.text.strip()
        password = self.password.text.strip()

        if not username or not password:
            self.show_message(
                "خطا",
                "لطفاً نام کاربری و رمز عبور را وارد کنید."
            )
            return

        # فعلاً برای تست اولیه
        # اتصال واقعی به AuthService را در مرحله بعد انجام می‌دهیم.

        self.manager.current = "dashboard"

    def show_message(self, title, message):

        popup = Popup(
            title=title,
            content=Label(text=message),
            size_hint=(0.85, 0.35)
        )

        popup.open()