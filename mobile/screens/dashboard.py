# ============================================================
# Frahoosh Mobile
# Professional Dashboard
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

from kivy.graphics import Color, RoundedRectangle


class DashboardScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # ====================================================
        # Root
        # ====================================================

        root = FloatLayout()

        # ====================================================
        # Background
        # ====================================================

        base_dir = os.path.dirname(os.path.dirname(__file__))

        background_path = os.path.join(
            base_dir,
            "assets",
            "background.png"
        )

        if os.path.isfile(background_path):

            background = Image(
                source=background_path,
                allow_stretch=True,
                keep_ratio=False,
                size_hint=(1, 1),
                pos_hint={"x": 0, "y": 0}
            )

            root.add_widget(background)

        # ====================================================
        # Main Content
        # ====================================================

        content = BoxLayout(
            orientation="vertical",
            padding=[14, 14, 14, 12],
            spacing=8,
            size_hint=(1, 1)
        )

        # ====================================================
        # Header
        # ====================================================

        header = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height=72,
            spacing=8
        )

        header.add_widget(
            Label(
                text="FRAHOOSH",
                font_size=29,
                bold=True,
                color=(1, 1, 1, 1)
            )
        )

        header.add_widget(
            Label(
                text="Smart School",
                font_size=16,
                color=(0.92, 0.95, 1, 1)
            )
        )

        content.add_widget(header)

        # ====================================================
        # Scroll
        # ====================================================

        scroll = ScrollView(
            size_hint=(1, 1),
            bar_width=5
        )

        panels = GridLayout(
            cols=1,
            spacing=8,
            padding=[3, 3, 3, 15],
            size_hint_y=None
        )

        panels.bind(
            minimum_height=panels.setter("height")
        )

        # ====================================================
        # Panels
        # ====================================================

        panel_data = [

            (
                "🏢",
                "MANAGEMENT",
                [
                    ("School Overview", True),
                    ("Announcements", True),
                    ("School Calendar", True),
                    ("Reports", False),
                    ("Staff Management", False),
                ],
                (0.10, 0.35, 0.70, 1)
            ),

            (
                "👥",
                "EXECUTIVE STAFF",
                [
                    ("Attendance", True),
                    ("Daily Tasks", True),
                    ("Student Records", False),
                    ("Administrative Reports", False),
                ],
                (0.10, 0.50, 0.35, 1)
            ),

            (
                "👨‍🏫",
                "TEACHERS",
                [
                    ("Homework", True),
                    ("Grades", True),
                    ("Class Schedule", True),
                    ("Student Performance", False),
                    ("Question Bank", False),
                ],
                (0.15, 0.48, 0.25, 1)
            ),

            (
                "🧠",
                "COUNSELING",
                [
                    ("Counseling Requests", True),
                    ("Appointments", True),
                    ("Student Counseling", False),
                    ("Counseling Reports", False),
                ],
                (0.45, 0.20, 0.55, 1)
            ),

            (
                "👨‍👩‍👧",
                "PARENTS",
                [
                    ("Announcements", True),
                    ("Parent Feedback", True),
                    ("Teacher Communication", False),
                    ("Meetings", False),
                ],
                (0.65, 0.30, 0.20, 1)
            ),

            (
                "🎓",
                "STUDENTS",
                [
                    ("Student Profile", True),
                    ("Homework", True),
                    ("Attendance", False),
                    ("Grades", False),
                    ("Educational Progress", False),
                ],
                (0.20, 0.45, 0.60, 1)
            ),

            (
                "📚",
                "QUESTION BANK",
                [
                    ("Browse Questions", True),
                    ("Sample Questions", True),
                    ("Create Question", False),
                    ("Question Categories", False),
                ],
                (0.55, 0.30, 0.20, 1)
            ),

            (
                "💻",
                "VIRTUAL CLASSES",
                [
                    ("Active Classes", True),
                    ("Class Schedule", True),
                    ("Join Class", False),
                    ("Recorded Classes", False),
                ],
                (0.10, 0.45, 0.60, 1)
            ),

            (
                "💰",
                "FINANCE",
                [
                    ("Financial Overview", True),
                    ("Payment Status", True),
                    ("Payment History", False),
                    ("Online Payment", False),
                ],
                (0.50, 0.30, 0.15, 1)
            ),

            (
                "📺",
                "SMART BOARD",
                [
                    ("School Announcements", True),
                    ("Daily Schedule", True),
                    ("Important Messages", False),
                    ("Emergency Notices", False),
                ],
                (0.25, 0.40, 0.65, 1)
            ),

            (
                "🤖",
                "ARTIFICIAL INTELLIGENCE",
                [
                    ("AI Assistant", True),
                    ("Educational Assistant", True),
                    ("Smart Analysis", False),
                    ("AI Reports", False),
                ],
                (0.50, 0.20, 0.55, 1)
            ),
        ]

        # ====================================================
        # Create Panels
        # ====================================================

        for icon, title, items, color in panel_data:

            panel = BoxLayout(
                orientation="vertical",
                size_hint_y=None,
                height=62,
                spacing=3,
                padding=[3, 3, 3, 3]
            )

            # ------------------------------------------------
            # Panel Background
            # ------------------------------------------------

            with panel.canvas.before:

                Color(
                    color[0],
                    color[1],
                    color[2],
                    0.96
                )

                background_rect = RoundedRectangle(
                    pos=panel.pos,
                    size=panel.size,
                    radius=[14]
                )

            panel.bind(
                pos=lambda instance, value,
                bg=background_rect:
                self.update_background(instance, bg)
            )

            panel.bind(
                size=lambda instance, value,
                bg=background_rect:
                self.update_background(instance, bg)
            )

            # ------------------------------------------------
            # Main Panel Button
            # ------------------------------------------------

            main_button = Button(
                text=icon + "   " + title,
                font_size=19,
                bold=True,
                size_hint_y=None,
                height=56,
                background_normal="",
                background_color=(
                    color[0] * 0.82,
                    color[1] * 0.82,
                    color[2] * 0.82,
                    1
                )
            )

            panel.add_widget(main_button)

            # ------------------------------------------------
            # Submenu
            # ------------------------------------------------

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
                    text_color = (0.05, 0.45, 0.20, 1)
                else:
                    prefix = "•  "
                    text_color = (0.25, 0.25, 0.25, 1)

                item_button = Button(
                    text=prefix + item_name,
                    font_size=17,
                    size_hint_y=None,
                    height=52,
                    color=text_color,
                    background_normal="",
                    background_color=(0.97, 0.97, 0.97, 1)
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

            # ------------------------------------------------
            # Accordion
            # ------------------------------------------------

            def toggle(
                instance,
                submenu=submenu,
                panel=panel
            ):

                if submenu.height == 0:

                    submenu.height = submenu.minimum_height

                    panel.height = (
                        62 +
                        submenu.minimum_height +
                        6
                    )

                else:

                    submenu.height = 0
                    panel.height = 62

            main_button.bind(
                on_press=toggle
            )

            panels.add_widget(panel)

        scroll.add_widget(panels)

        content.add_widget(scroll)

        # ====================================================
        # Logout
        # ====================================================

        logout_button = Button(
            text="🚪  LOGOUT",
            font_size=17,
            bold=True,
            size_hint_y=None,
            height=52,
            background_normal="",
            background_color=(0.55, 0.10, 0.10, 0.95)
        )

        logout_button.bind(
            on_press=self.logout
        )

        content.add_widget(logout_button)

        root.add_widget(content)

        self.add_widget(root)

    # ========================================================
    # Background Helper
    # ========================================================

    def update_background(self, widget, background):

        background.pos = widget.pos
        background.size = widget.size

    # ========================================================
    # Section
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
    # Logout
    # ========================================================

    def logout(self, instance):

        if self.manager:
            self.manager.current = "login"
