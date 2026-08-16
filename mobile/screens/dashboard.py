# ============================================================
# Frahoosh Mobile
# Professional Color Dashboard
# Stable Accordion Version
# ============================================================

from kivy.uix.screenmanager import Screen
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
        # Main Layout
        # ====================================================

        root = BoxLayout(
            orientation="vertical",
            padding=[18, 18, 18, 18],
            spacing=12
        )

        # ====================================================
        # Header
        # ====================================================

        root.add_widget(
            Label(
                text="FRAHOOSH",
                font_size=34,
                bold=True,
                size_hint_y=None,
                height=65
            )
        )

        root.add_widget(
            Label(
                text="Smart Educational Management System",
                font_size=19,
                size_hint_y=None,
                height=45
            )
        )

        # ====================================================
        # Scroll
        # ====================================================

        scroll = ScrollView(
            size_hint=(1, 1),
            bar_width=7
        )

        panels = GridLayout(
            cols=1,
            spacing=12,
            padding=[4, 4, 4, 20],
            size_hint_y=None
        )

        panels.bind(
            minimum_height=panels.setter("height")
        )

        # ====================================================
        # Panel Data
        # ====================================================

        panel_data = [

            (
                "MANAGEMENT",
                "🏢",
                [
                    ("School Overview", True),
                    ("Announcements", True),
                    ("School Calendar", True),
                    ("Reports", False),
                    ("Staff Management", False),
                ],
                (0.15, 0.40, 0.80, 1)
            ),

            (
                "EXECUTIVE STAFF",
                "👥",
                [
                    ("Attendance", True),
                    ("Daily Tasks", True),
                    ("Student Records", False),
                    ("Administrative Reports", False),
                ],
                (0.15, 0.60, 0.40, 1)
            ),

            (
                "TEACHERS",
                "👨‍🏫",
                [
                    ("Homework", True),
                    ("Grades", True),
                    ("Class Schedule", True),
                    ("Student Performance", False),
                    ("Question Bank", False),
                ],
                (0.20, 0.55, 0.30, 1)
            ),

            (
                "COUNSELING",
                "🧠",
                [
                    ("Counseling Requests", True),
                    ("Appointments", True),
                    ("Student Counseling", False),
                    ("Counseling Reports", False),
                ],
                (0.55, 0.30, 0.65, 1)
            ),

            (
                "PARENTS",
                "👨‍👩‍👧",
                [
                    ("Announcements", True),
                    ("Parent Feedback", True),
                    ("Teacher Communication", False),
                    ("Meetings", False),
                ],
                (0.65, 0.35, 0.25, 1)
            ),

            (
                "STUDENTS",
                "🎓",
                [
                    ("Student Profile", True),
                    ("Homework", True),
                    ("Attendance", False),
                    ("Grades", False),
                    ("Educational Progress", False),
                ],
                (0.30, 0.55, 0.65, 1)
            ),

            (
                "QUESTION BANK",
                "📚",
                [
                    ("Browse Questions", True),
                    ("Sample Questions", True),
                    ("Create Question", False),
                    ("Question Categories", False),
                ],
                (0.60, 0.35, 0.25, 1)
            ),

            (
                "VIRTUAL CLASSES",
                "💻",
                [
                    ("Active Classes", True),
                    ("Class Schedule", True),
                    ("Join Class", False),
                    ("Recorded Classes", False),
                ],
                (0.20, 0.50, 0.65, 1)
            ),

            (
                "FINANCE",
                "💰",
                [
                    ("Financial Overview", True),
                    ("Payment Status", True),
                    ("Payment History", False),
                    ("Online Payment", False),
                ],
                (0.50, 0.35, 0.20, 1)
            ),

            (
                "SMART BOARD",
                "📺",
                [
                    ("School Announcements", True),
                    ("Daily Schedule", True),
                    ("Important Messages", False),
                    ("Emergency Notices", False),
                ],
                (0.30, 0.45, 0.70, 1)
            ),

            (
                "ARTIFICIAL INTELLIGENCE",
                "🤖",
                [
                    ("AI Assistant", True),
                    ("Educational Assistant", True),
                    ("Smart Analysis", False),
                    ("AI Reports", False),
                ],
                (0.55, 0.25, 0.60, 1)
            ),
        ]

        # ====================================================
        # Create Panels
        # ====================================================

        for title, icon, items, color in panel_data:

            panel = BoxLayout(
                orientation="vertical",
                size_hint_y=None,
                height=78,
                spacing=5,
                padding=[5, 5, 5, 5]
            )

            # ------------------------------------------------
            # Background
            # ------------------------------------------------

            with panel.canvas.before:

                Color(
                    color[0],
                    color[1],
                    color[2],
                    1
                )

                background = RoundedRectangle(
                    pos=panel.pos,
                    size=panel.size,
                    radius=[16]
                )

            panel.bind(
                pos=lambda instance, value,
                bg=background:
                self.update_background(instance, bg)
            )

            panel.bind(
                size=lambda instance, value,
                bg=background:
                self.update_background(instance, bg)
            )

            # ------------------------------------------------
            # Main Button
            # ------------------------------------------------

            main_button = Button(
                text=icon + "   " + title,
                font_size=22,
                bold=True,
                size_hint_y=None,
                height=70,
                background_normal="",
                background_color=(
                    color[0] * 0.75,
                    color[1] * 0.75,
                    color[2] * 0.75,
                    1
                )
            )

            panel.add_widget(main_button)

            # ------------------------------------------------
            # Submenu
            # ------------------------------------------------

            submenu = GridLayout(
                cols=1,
                spacing=5,
                size_hint_y=None,
                height=0
            )

            submenu.bind(
                minimum_height=submenu.setter("height")
            )

            for item_name, active in items:

                if active:
                    prefix = "✓  "
                else:
                    prefix = "•  "

                item_button = Button(
                    text=prefix + item_name,
                    font_size=19,
                    size_hint_y=None,
                    height=62,
                    background_normal="",
                    background_color=(
                        0.94,
                        0.94,
                        0.94,
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
                        78 +
                        submenu.minimum_height +
                        10
                    )

                else:

                    submenu.height = 0
                    panel.height = 78

            main_button.bind(
                on_press=toggle
            )

            panels.add_widget(panel)

        scroll.add_widget(panels)

        root.add_widget(scroll)

        # ====================================================
        # Logout
        # ====================================================

        logout_button = Button(
            text="🚪   LOGOUT",
            font_size=20,
            bold=True,
            size_hint_y=None,
            height=65,
            background_normal="",
            background_color=(0.65, 0.12, 0.12, 1)
        )

        logout_button.bind(
            on_press=self.logout
        )

        root.add_widget(logout_button)

        self.add_widget(root)

    # ========================================================
    # Background
    # ========================================================

    def update_background(self, instance, background):

        background.pos = instance.pos
        background.size = instance.size

    # ========================================================
    # Section Click
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
