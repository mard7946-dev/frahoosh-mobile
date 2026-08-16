# ============================================================
# Frahoosh Mobile
# Professional Persian Dashboard
# ============================================================

import os

from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView

from kivy.core.text import LabelBase
from kivy.graphics import Color, RoundedRectangle


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

BACKGROUND_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "f20639fa-bd85-4a6e-aad1-913d61e16875.png"
)

FONT_PATH = os.path.join(
    BASE_DIR,
    "assets",
    "BTitr.ttf"
)

FONT_NAME = "Default"

try:
    if os.path.isfile(FONT_PATH):
        LabelBase.register(
            name="FrahooshBTitrDashboard",
            fn_regular=FONT_PATH
        )
        FONT_NAME = "FrahooshBTitrDashboard"
except Exception:
    FONT_NAME = "Default"


class DashboardScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = FloatLayout()

        # ====================================================
        # BACKGROUND
        # ====================================================

        if os.path.isfile(BACKGROUND_PATH):

            background = Image(
                source=BACKGROUND_PATH,
                allow_stretch=True,
                keep_ratio=False,
                size_hint=(1, 1)
            )

            root.add_widget(background)

        # ====================================================
        # MAIN CONTENT
        # ====================================================

        content = BoxLayout(
            orientation="vertical",
            padding=[18, 12, 18, 10],
            spacing=7,
            size_hint=(0.90, 1),
            pos_hint={
                "center_x": 0.5,
                "y": 0
            }
        )

        # ====================================================
        # HEADER
        # ====================================================

        header = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height=90
        )

        header.add_widget(
            Label(
                text="فراهوش",
                font_name=FONT_NAME,
                font_size=32,
                bold=True,
                color=(1, 1, 1, 1),
                size_hint_y=None,
                height=48
            )
        )

        header.add_widget(
            Label(
                text="دبیرستان سردارحاجی زاده ۲",
                font_name=FONT_NAME,
                font_size=19,
                color=(1, 1, 1, 1),
                size_hint_y=None,
                height=38
            )
        )

        content.add_widget(header)

        # ====================================================
        # SCROLL
        # ====================================================

        scroll = ScrollView(
            size_hint=(1, 1),
            bar_width=4
        )

        panels = GridLayout(
            cols=1,
            spacing=8,
            padding=[12, 4, 25, 15],
            size_hint_y=None
        )

        panels.bind(
            minimum_height=panels.setter("height")
        )

        # ====================================================
        # PANEL DATA
        # ====================================================

        panel_data = [

            (
                "🏢",
                "مدیریت",
                [
                    ("نمای کلی مدرسه", True),
                    ("اطلاعیه‌ها", True),
                    ("تقویم مدرسه", True),
                    ("گزارش‌ها", False),
                ],
                (0.08, 0.35, 0.72, 1)
            ),

            (
                "👥",
                "کادر اجرایی",
                [
                    ("حضور و غیاب", True),
                    ("وظایف روزانه", True),
                    ("پرونده دانش‌آموزان", False),
                    ("گزارش‌های اجرایی", False),
                ],
                (0.08, 0.55, 0.40, 1)
            ),

            (
                "👨‍🏫",
                "دبیران",
                [
                    ("ثبت تکلیف", True),
                    ("ثبت نمره", True),
                    ("برنامه کلاس", True),
                    ("عملکرد دانش‌آموز", False),
                ],
                (0.15, 0.50, 0.25, 1)
            ),

            (
                "🧠",
                "مشاوره",
                [
                    ("درخواست مشاوره", True),
                    ("نوبت مشاوره", True),
                    ("پرونده مشاوره", False),
                    ("گزارش مشاوره", False),
                ],
                (0.48, 0.20, 0.58, 1)
            ),

            (
                "👨‍👩‍👧",
                "اولیاء",
                [
                    ("اطلاعیه‌ها", True),
                    ("نظردهی اولیاء", True),
                    ("ارتباط با دبیر", False),
                    ("جلسات", False),
                ],
                (0.68, 0.32, 0.18, 1)
            ),

            (
                "🎓",
                "دانش‌آموزان",
                [
                    ("پروفایل دانش‌آموز", True),
                    ("تکالیف", True),
                    ("حضور و غیاب", False),
                    ("نمرات", False),
                ],
                (0.18, 0.45, 0.62, 1)
            ),

            (
                "📚",
                "بانک سوالات",
                [
                    ("مشاهده سوالات", True),
                    ("نمونه سوالات", True),
                    ("ثبت سوال", False),
                    ("دسته‌بندی سوالات", False),
                ],
                (0.55, 0.32, 0.20, 1)
            ),

            (
                "💻",
                "کلاس‌های مجازی",
                [
                    ("کلاس‌های فعال", True),
                    ("برنامه کلاس", True),
                    ("ورود به کلاس", False),
                    ("کلاس‌های ضبط شده", False),
                ],
                (0.10, 0.48, 0.65, 1)
            ),

            (
                "💰",
                "امور مالی",
                [
                    ("وضعیت مالی", True),
                    ("وضعیت پرداخت", True),
                    ("سوابق پرداخت", False),
                    ("پرداخت آنلاین", False),
                ],
                (0.52, 0.32, 0.15, 1)
            ),

            (
                "📺",
                "تابلو هوشمند",
                [
                    ("اطلاعیه مدرسه", True),
                    ("برنامه روزانه", True),
                    ("پیام‌های مهم", False),
                    ("اعلامیه اضطراری", False),
                ],
                (0.22, 0.42, 0.68, 1)
            ),

            (
                "🤖",
                "هوش مصنوعی",
                [
                    ("دستیار هوشمند", True),
                    ("دستیار آموزشی", True),
                    ("تحلیل هوشمند", False),
                    ("گزارش هوشمند", False),
                ],
                (0.52, 0.20, 0.58, 1)
            ),
        ]

        # ====================================================
        # CREATE PANELS
        # ====================================================

        for icon, title, items, color in panel_data:

            panel = BoxLayout(
                orientation="vertical",
                size_hint_y=None,
                height=58,
                spacing=3,
                padding=[3, 3, 3, 3]
            )

            with panel.canvas.before:

                Color(
                    color[0],
                    color[1],
                    color[2],
                    0.96
                )

                panel_bg = RoundedRectangle(
                    pos=panel.pos,
                    size=panel.size,
                    radius=[13]
                )

            panel.bind(
                pos=lambda instance, value,
                bg=panel_bg:
                self.update_background(instance, bg)
            )

            panel.bind(
                size=lambda instance, value,
                bg=panel_bg:
                self.update_background(instance, bg)
            )

            # =================================================
            # PANEL BUTTON
            # =================================================

            main_button = Button(
                text=icon + "   " + title,
                font_name=FONT_NAME,
                font_size=23,
                bold=True,
                size_hint_y=None,
                height=52,
                color=(1, 1, 1, 1),
                background_normal="",
                background_color=(
                    color[0] * 0.82,
                    color[1] * 0.82,
                    color[2] * 0.82,
                    1
                )
            )

            panel.add_widget(main_button)

            # =================================================
            # SUBMENU
            # =================================================

            submenu = GridLayout(
                cols=1,
                spacing=4,
                size_hint_y=None,
                height=0
            )

            submenu.bind(
                minimum_height=submenu.setter("height")
            )

            for item_name, active in items:

                if active:

                    prefix = "✓  "
                    text_color = (
                        0.04,
                        0.40,
                        0.16,
                        1
                    )

                else:

                    prefix = "•  "
                    text_color = (
                        0.25,
                        0.25,
                        0.25,
                        1
                    )

                item_button = Button(
                    text=prefix + item_name,
                    font_name=FONT_NAME,
                    font_size=20,
                    size_hint_y=None,
                    height=58,
                    color=text_color,
                    background_normal="",
                    background_color=(
                        0.97,
                        0.97,
                        0.97,
                        1
                    )
                )

                item_button.bind(
                    on_press=lambda btn,
                    active=active:
                    self.item_clicked(
                        btn.text,
                        active
                    )
                )

                submenu.add_widget(item_button)

            panel.add_widget(submenu)

            # =================================================
            # ACCORDION
            # =================================================

            def toggle(
                instance,
                submenu=submenu,
                panel=panel
            ):

                if submenu.height == 0:

                    submenu.height = submenu.minimum_height

                    panel.height = (
                        58 +
                        submenu.minimum_height +
                        6
                    )

                else:

                    submenu.height = 0

                    panel.height = 58

            main_button.bind(
                on_press=toggle
            )

            panels.add_widget(panel)

        scroll.add_widget(panels)

        content.add_widget(scroll)

        # ====================================================
        # LOGOUT
        # ====================================================

        logout_button = Button(
            text="🚪   خروج از حساب",
            font_name=FONT_NAME,
            font_size=19,
            bold=True,
            size_hint_y=None,
            height=55,
            background_normal="",
            background_color=(
                0.55,
                0.10,
                0.10,
                0.95
            )
        )

        logout_button.bind(
            on_press=self.logout
        )

        content.add_widget(logout_button)

        root.add_widget(content)

        self.add_widget(root)

    # ========================================================
    # BACKGROUND
    # ========================================================

    def update_background(self, widget, background):

        background.pos = widget.pos
        background.size = widget.size

    # ========================================================
    # ACTIVE SECTION
    # ========================================================

    def item_clicked(self, text, active):

        if active:

            print(
                "Frahoosh Active Section:",
                text
            )

        else:

            print(
                "Frahoosh Coming Soon:",
                text
            )

    # ========================================================
    # LOGOUT
    # ========================================================

    def logout(self, instance):

        if self.manager:
            self.manager.current = "login"
