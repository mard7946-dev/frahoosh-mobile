from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screens.login import LoginScreen


class FrahooshMobileApp:

    def build(self):
        manager = ScreenManager()

        manager.add_widget(
            LoginScreen(name="login")
        )

        manager.current = "login"

        return manager


if __name__ == "__main__":
    FrahooshMobileApp().run()
