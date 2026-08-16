# ============================================================
# Frahoosh Mobile
# برنامه اصلی نسخه پایدار
# ============================================================

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screens.login import LoginScreen


class FrahooshMobileApp(App):

    def build(self):
        manager = ScreenManager()

        # ----------------------------------------------------
        # فقط صفحه ورود هنگام شروع برنامه ساخته می‌شود.
        # داشبورد فعلاً هنگام لودینگ ساخته نمی‌شود.
        # ----------------------------------------------------

        manager.add_widget(
            LoginScreen(name="login")
        )

        manager.current = "login"

        return manager


if __name__ == "__main__":
    FrahooshMobileApp().run()
