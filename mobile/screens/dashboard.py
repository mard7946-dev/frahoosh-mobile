# ============================================================
# Frahoosh Mobile
# داشبورد اصلی - مرحله اول
# 11 پنل اصلی فراهوش
# ============================================================

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView


class DashboardScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # ----------------------------------------------------
        # صفحه اصلی
        # ----------------------------------------------------

        root = BoxLayout(
            orientation="vertical",
            padding=[20, 20, 20, 20],
            spacing=15
        )

        # ----------------------------------------------------
        # عنوان
        # ----------------------------------------------------

        root.add_widget(
            Label(
                text="Frahoosh",
                font_size=30,
                bold=True,
                size_hint_y=None,
                height=60
            )
        )

        root.add_widget(
            Label(
                text="School Management System",
                font_size=17,
                size_hint_y=None,
                height=40
            )
        )

        # ----------------------------------------------------
        # اسکرول پنل‌ها
        # ----------------------------------------------------

        scroll = ScrollView(
            size_hint=(1, 1)
        )

        panels = GridLayout(
            cols=2,
            spacing=12,
            padding=[5, 5, 5, 20],
            size_hint_y=None
        )

        panels.bind(
            minimum_height=panels.setter("height")
        )

        # ----------------------------------------------------
        # پنل‌های اصلی فراهوش
        # ----------------------------------------------------

        panel_names = [
            "مدیریت",
            "کادر اجرایی",
            "دبیران",
            "مشاوره",
            "اولیاء",
            "دانش‌آموزان",
            "بانک سؤالات",
            "کلاس‌های مجازی",
            "امور مالی",
            "تابلو هوشمند",
            "هوش مصنوعی",
        ]

        # ----------------------------------------------------
        # ساخت کارت‌ها
        # ----------------------------------------------------

        for name in panel_names:

            button = Button(
                text=name,
                font_size=18,
                size_hint_y=None,
                height=100
            )

            button.bind(
                on_press=self.panel_clicked
            )

            panels.add_widget(button)

        scroll.add_widget(panels)

        root.add_widget(scroll)

        # ----------------------------------------------------
        # دکمه خروج
        # ----------------------------------------------------

        logout_button = Button(
            text="خروج از حساب",
            font_size=17,
            size_hint_y=None,
            height=55
        )

        logout_button.bind(
            on_press=self.logout
        )

        root.add_widget(logout_button)

        self.add_widget(root)

    # ========================================================
    # کلیک روی پنل
    # ========================================================

    def panel_clicked(self, instance):

        print(
            "Frahoosh panel:",
            instance.text
        )

    # ========================================================
    # خروج
    # ========================================================

    def logout(self, instance):

        if self.manager:
            self.manager.current = "login"
