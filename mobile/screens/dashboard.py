# ============================================================
# Frahoosh Mobile
# داشبورد اصلی نسخه موبایل
# مرحله اول: 11 پنل اصلی فراهوش
# ============================================================

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup


class DashboardScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # ====================================================
        # صفحه اصلی
        # ====================================================

        root = BoxLayout(
            orientation="vertical",
            padding=[20, 20, 20, 20],
            spacing=12
        )

        # ====================================================
        # عنوان برنامه
        # ====================================================

        title = Label(
            text="Welcome to Frahoosh",
            font_size=28,
            bold=True,
            size_hint_y=None,
            height=60
        )

        root.add_widget(title)

        # ====================================================
        # زیرعنوان
        # ====================================================

        subtitle = Label(
            text="سامانه هوشمند آموزشی",
            font_size=18,
            size_hint_y=None,
            height=45
        )

        root.add_widget(subtitle)

        # ====================================================
        # ناحیه پنل‌ها
        # ====================================================

        scroll = ScrollView(
            size_hint=(1, 1)
        )

        panels = GridLayout(
            cols=2,
            spacing=12,
            padding=[5, 10, 5, 20],
            size_hint_y=None
        )

        panels.bind(
            minimum_height=panels.setter("height")
        )

        # ====================================================
        # 11 پنل اصلی فراهوش
        # ====================================================

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

        # ====================================================
        # ساخت پنل‌ها
        # ====================================================

        for panel_name in panel_names:

            button = Button(
                text=panel_name,
                font_size=18,
                size_hint_y=None,
                height=95
            )

            button.bind(
                on_press=self.open_panel
            )

            panels.add_widget(button)

        scroll.add_widget(panels)

        root.add_widget(scroll)

        # ====================================================
        # دکمه خروج
        # ====================================================

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
    # انتخاب پنل
    # ========================================================

    def open_panel(self, instance):

        panel_name = instance.text

        popup_content = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        popup_content.add_widget(
            Label(
                text=panel_name,
                font_size=24,
                bold=True
            )
        )

        popup_content.add_widget(
            Label(
                text="این بخش در حال به‌روزرسانی است.\n"
                     "به‌زودی امکانات این بخش در دسترس قرار خواهد گرفت.",
                font_size=17
            )
        )

        close_button = Button(
            text="باشه",
            size_hint_y=None,
            height=50
        )

        popup_content.add_widget(close_button)

        popup = Popup(
            title="فراهوش",
            content=popup_content,
            size_hint=(0.85, 0.4),
            auto_dismiss=False
        )

        close_button.bind(
            on_press=popup.dismiss
        )

        popup.open()

    # ========================================================
    # خروج
    # ========================================================

    def logout(self, instance):

        if self.manager:
            self.manager.current = "login"
