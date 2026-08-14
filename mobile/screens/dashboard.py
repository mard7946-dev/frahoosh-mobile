# ============================================================
# Frahoosh Mobile
# داشبورد اصلی نسخه موبایل
# ============================================================

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup

from config import APP_NAME, SYSTEM_TITLE, APP_VERSION


class DashboardScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # ----------------------------------------------------
        # صفحه اصلی
        # ----------------------------------------------------

        root = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=12
        )

        # ----------------------------------------------------
        # عنوان
        # ----------------------------------------------------

        title = Label(
            text=APP_NAME,
            font_size=30,
            bold=True,
            size_hint_y=None,
            height=55
        )

        root.add_widget(title)

        subtitle = Label(
            text="داشبورد اصلی فراهوش",
            font_size=22,
            size_hint_y=None,
            height=45
        )

        root.add_widget(subtitle)

        system_title = Label(
            text=SYSTEM_TITLE,
            font_size=15,
            size_hint_y=None,
            height=40
        )

        root.add_widget(system_title)

        # ----------------------------------------------------
        # ماژول‌های اصلی
        # ----------------------------------------------------

        modules = GridLayout(
            cols=2,
            spacing=12,
            padding=5
        )

        buttons = [
            ("👨‍🎓\nدانش‌آموزان", self.open_students),
            ("👨‍🏫\nدبیران", self.open_teachers),
            ("🏫\nمدیریت مدرسه", self.open_management),
            ("👨‍👩‍👦\nاولیا", self.open_parents),
            ("💰\nامور مالی", self.open_finance),
            ("🤖\nهوش مصنوعی نورا", self.open_ai),
        ]

        for title, callback in buttons:

            button = Button(
                text=title,
                font_size=18,
                bold=True
            )

            button.bind(
                on_press=callback
            )

            modules.add_widget(button)

        root.add_widget(modules)

        # ----------------------------------------------------
        # بخش خدمات
        # ----------------------------------------------------

        services = BoxLayout(
            orientation="horizontal",
            spacing=10,
            size_hint_y=None,
            height=55
        )

        online_button = Button(
            text="کلاس‌های آنلاین",
            font_size=15
        )

        online_button.bind(
            on_press=self.open_online_class
        )

        services.add_widget(online_button)

        notification_button = Button(
            text="اطلاعیه‌ها",
            font_size=15
        )

        notification_button.bind(
            on_press=self.open_notifications
        )

        services.add_widget(notification_button)

        root.add_widget(services)

        # ----------------------------------------------------
        # بروزرسانی
        # ----------------------------------------------------

        update_button = Button(
            text="به‌روزرسانی فراهوش",
            size_hint_y=None,
            height=50,
            font_size=16
        )

        update_button.bind(
            on_press=self.open_update
        )

        root.add_widget(update_button)

        # ----------------------------------------------------
        # خروج
        # ----------------------------------------------------

        logout_button = Button(
            text="خروج از حساب",
            size_hint_y=None,
            height=50,
            font_size=16
        )

        logout_button.bind(
            on_press=self.logout
        )
        gout_button)

        # ----------------------------------------------------
        # نسخه
        # ----------------------------------------------------

        version = Label(
            text=f"فراهوش | نسخه {APP_VERSION}",
            font_size=12,
            size_hint_y=None,
            height=30
        )

        root.add_widget(version)

        self.add_widget(root)

    # ========================================================
    # پیام موقت ماژول‌ها
    # ========================================================

    def show_message(self, title, message):

        popup = Popup(
            title=title,
            content=Label(
                text=message,
                font_size=16
            ),
            size_hint=(0.8, 0.35)
        )

        popup.open()

    # ========================================================
    # ماژول‌ها
    # ========================================================

    def open_students(self, instance):
        self.show_message(
            "دانش‌آموزان",
            "ماژول مدیریت دانش‌آموزان فراهوش در حال ساخت است."
        )

    def open_teachers(self, instance):
        self.show_message(
            "دبیران",
            "ماژول دبیران فراهوش در حال ساخت است."
        )

    def open_management(self, instance):
        self.show_message(
            "مدیریت مدرسه",
            "پنل مدیریت مدرسه در حال ساخت است."
        )

    def open_parents(self, instance):
        self.show_message(
            "اولیا",
            "پنل اولیا در حال ساخت است."
        )

    def open_finance(self, instance):
        self.show_message(
            "امور مالی",
            "ماژول امور مالی در حال ساخت است."
        )

    def open_ai(self, instance):
        self.show_message(
            "هوش مصنوعی نورا",
            "دستیار هوشمند مدیر مدرسه در حال ساخت است."
        )

    def open_online_class(self, instance):
        self.show_message(
            "کلاس‌های آنلاین",
            "ماژول کلاس‌های آنلاین در حال ساخت است."
        )

    def open_notifications(self, instance):
        self.show_message(
            "اطلاعیه‌ها",
            "مرکز اطلاعیه‌های فراهوش در حال ساخت است."
        )

    # ========================================================
    # بروزرسانی
    # ========================================================

    def open_update(self, instance):
        self.manager.current = "update"

    # ========================================================
    # خروج
    # ========================================================

    def logout(self, instance):
        self.manager.current = "login"

        

        root.add_widget(lo
