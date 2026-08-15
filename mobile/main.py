from kivy.app import App
from kivy.uix.label import Label


class FrahooshMobileApp(App):

    def build(self):
        return Label(
            text="FRAHOOSH TEST",
            font_size=32
        )


if __name__ == "__main__":
    FrahooshMobileApp().run()
