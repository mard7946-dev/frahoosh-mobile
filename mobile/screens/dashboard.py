# ============================================================
# Frahoosh Mobile
# Professional Compact Dashboard
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
        # ROOT
        # ====================================================

        root = FloatLayout()

        # ====================================================
        # BACKGROUND
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
                size_hint=(1, 1)
            )

            root.add_widget(background)

        # ====================================================
        # MAIN CONTENT
        # ====================================================

        content = BoxLayout(
            orientation="vertical",
            padding=[18, 12, 18, 12],
            spacing=8,
            size_hint=(0.94, 1),
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
            height=82,
            spacing=2
        )

        header.add_widget(
            Label(
                text="FRAHOOSH",
                font_size=32,
                bold=True,
                color=(1, 1, 1, 1),
                size_hint_y=None,
                height=43
            )
        )

        header.add_widget(
            Label(
                text="Smart Educational Management System",
                font_size=16,
                color=(0.94, 0.97, 1, 1),
                size_hint_y=None,
                height=30
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
            spacing=9,
            padding=[8, 5, 8, 15],
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
                "MANAGEMENT",
                [
                    ("School Overview", True),
                    ("Announcements", True),
                    ("School Calendar", True),
                    ("Reports", False),
                    ("Staff Management", False),
                ],
                (0.08, 0.35, 0.72, 1)
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
                (0.08, 0.55, 0.40, 1)
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
                (0.15, 0.50, 0.25, 1)
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
                (0.48, 0.20, 0.58, 1)
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
                (0.68, 0.32, 0.18, 1)
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
                (0.18, 0.45, 0.62, 1)
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
                (0.55, 0.32, 0.20, 1)
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
                (0.10, 0.48, 0.65, 1)
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
                (0.52, 0.32, 0.15, 1)
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
                (0.22, 0.42, 0.68, 1)
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

            # ------------------------------------------------
            # PANEL BUTTON
            # ------------------------------------------------

            main_button = Button(
                text=icon + "   " + title,
                font_size=21,
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

            # ------------------------------------------------
            # SUBMENU
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
                    text_color = (
                        0.05,
                        0.42,
                        0.18,
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
                    font_size=19,
                    size_hint_y=None,
                    height=56,
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

            # ------------------------------------------------
            # ACCORDION
            # ------------------------------------------------

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

        # ====================================================
        # ADD SCROLL
        # ====================================================

        scroll.add_widget(panels)

        content.add_widget(scroll)

        # ====================================================
        # LOGOUT
        # ====================================================

        logout_button = Button(
            text="🚪   LOGOUT",
            font_size=18,
            bold=True,
            size_hint_y=None,
            height=54,
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
    # SECTION
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
