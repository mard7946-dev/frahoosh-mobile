from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.clock import Clock

from config import APP_NAME, SYSTEM_TITLE, APP_VERSION
from services.api import APIClient, APIError

class LoginScreen(Screen):
    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        root = BoxLayout(orientation="vertical", padding=28, spacing=12)

        root.add_widget(Label(text=APP_NAME, font_size=32, bold=True,
                              size_hint_y=None, height=65))
        root.add_widget(Label(text=SYSTEM_TITLE, font_size=17,
                              size_hint_y=None, height=50))

        self.username = TextInput(hint_text="نام کاربری / کد ملی",
                                  multiline=False, size_hint_y=None, height=54)
        self.password = TextInput(hint_text="رمز عبور", password=True,
                                  multiline=False, size_hint_y=None, height=54)
        root.add_widget(self.username)
        root.add_widget(self.password)

        self.status = Label(text="", size_hint_y=None, height=55)
        root.add_widget(self.status)

        button = Button(text="ورود به فراهوش", size_hint_y=None, height=58)
        button.bind(on_press=self.login)
        root.add_widget(button)

        root.add_widget(Label(text=f"نسخه {APP_VERSION}", font_size=12))
        self.add_widget(root)

    def login(self, _):
        username = self.username.text.strip()
        password = self.password.text
        if not username or not password:
            self.status.text = "نام کاربری و رمز عبور را وارد کنید."
            return

        self.status.text = "در حال اتصال..."
        try:
            client = APIClient()
            token, user = client.login(username, password)
            self.app.session.save(token, user)
            self.app.api.set_token(token)
            self.manager.get_screen("dashboard").refresh()
            self.manager.current = "dashboard"
        except APIError as exc:
            self.status.text = str(exc)
        except Exception as exc:
            self.status.text = f"خطای ورود: {exc}"
