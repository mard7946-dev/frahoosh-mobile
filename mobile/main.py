# ============================================================
# Frahoosh Mobile
# Main - Safe Startup
# ============================================================

import os

# جلوگیری از مشکلات اولیه SDL / صوت
os.environ.setdefault("KIVY_GL_BACKEND", "gles2")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screens.login import LoginScreen


class FrahooshMobileApp(App):

    def build(self):

        manager = ScreenManager()

        # فقط صفحه ورود در شروع برنامه ساخته می‌شود
        manager.add_widget(
            LoginScreen(name="login")
        )

        manager.current = "login"

        return manager


if __name__ == "__main__":
    FrahooshMobileApp().run()
