from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label


class TestScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(
            Label(
                text="FRAHOOSH SCREEN TEST",
                font_size=32
            )
        )


class FrahooshMobileApp(App):

    def build(self):

        manager = ScreenManager()

        manager.add_widget(
            TestScreen(name="test")
        )

        manager.current = "test"

        return manager


if __name__ == "__main__":
    FrahooshMobileApp().run()
