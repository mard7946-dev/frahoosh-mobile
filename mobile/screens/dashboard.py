# ============================================================
# Frahoosh Mobile
# داشبورد نسخه موبایل
# ============================================================

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

from config import APP_NAME, SYSTEM_TITLE, APP_VERSION


class DashboardScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(
            orientation="vertical",
            padding=25,
            spacing=15
        )

        root.add_widget(
            Label(
                text=APP_NAME,
                font_size=30,
                bold=True,
                size_hint_y=None,
                height=65
            )
        )

        root.add_widget(
            Label(
                text="داشبورد فراهوش",
                font_size=22,
                size_hint_y=None,
                height=55
            )
        )

        root.add_widget(
            Label(
                text=SYSTEM_TITLE,
                font_size=16,
                size_hint_y=None,
                height=45
            )
        )

        # ----------------------------------------------------
        # دکمه‌ها
        # ----------------------------------------------------

        buttons = [
            ("پنل آموزشی", self.open_education),
            ("کلاس‌های آنلاین", self.open_online_class),
            ("تابلو هوشمند", self.open_smart_board),
            ("اطلاعیه‌ها", self.open_notifications),
            ("به‌روزرسانی فراهوش", self.open_update),
        ]

        for title, callback in buttons:

            button = Button(
                text=title,
                size_hint_y=None,
                height=58
            )

            button.bind(on_press=callback)
            root.add_widget(button)

        # ----------------------------------------------------
        # خروج
        # ----------------------------------------------------

        logout_button = Button(
            text="خروج از حساب",
            size_hint_y=None,
            height=58
        )

        logout_button.bind(
            on_press=self.logout
        )

        root.add_widget(logout_button)

        root.add_widget(
            Label(
                text=f"نسخه {APP_VERSION}",
                font_size=13
            )
        )

        self.add_widget(root)

    # ========================================================
    # بخش‌ها
    # ========================================================

    def open_education(self, instance):
        pass

    def open_online_class(self, instance):
        pass

    def open_smart_board(self, instance):
        pass

    def open_notifications(self, instance):
        pass

    def open_update(self, instance):
        self.manager.current = "update"

    # ========================================================
    # خروج
    # ========================================================

    def logout(self, instance):
        self.manager.current = "login"