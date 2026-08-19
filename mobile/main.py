from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

from config import APP_NAME
from services.api import APIClient
from services.session import SessionStore
from screens.login import LoginScreen
from screens.dashboard import DashboardScreen
from screens.update import UpdateScreen

class FrahooshMobileApp(App):
    title = APP_NAME

    def build(self):
        self.session = SessionStore()
        self.api = APIClient(token=self.session.token)

        manager = ScreenManager()
        manager.add_widget(LoginScreen(app=self, name="login"))
        manager.add_widget(DashboardScreen(app=self, name="dashboard"))
        manager.add_widget(UpdateScreen(name="update"))

        if self.session.token:
            try:
                manager.get_screen("dashboard").refresh()
                manager.current = "dashboard"
            except Exception:
                self.session.clear()
                manager.current = "login"
        else:
            manager.current = "login"

        return manager

if __name__ == "__main__":
    FrahooshMobileApp().run()
