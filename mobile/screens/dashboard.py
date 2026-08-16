# ============================================================
# Frahoosh Mobile
# Professional Mobile Dashboard
# Version 1 - Stable UI
# ============================================================

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup

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

        header = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            height=95,
            spacing=4
        )

        header.add_widget(
            Label(
                text="🏫  FRAHOOSH",
                font_size=30,
                bold=True,
                size_hint_y=None,
                height=52
            )
        )

        header.add_widget(
            Label(
                text="Smart Educational Management System",
                font_size=16,
                size_hint_y=None,
                height=35
            )
        )

        root.add_widget(header)

        # ====================================================
        # Scroll Area
        # ====================================================

        scroll = ScrollView(
            size_hint=(1, 1),
            bar_width=6
        )

        panels_layout = GridLayout(
            cols=1,
            spacing=12,
            padding=[2, 2, 2, 15],
            size_hint_y=None
        )

        panels_layout.bind(
            minimum_height=panels_layout.setter("height")
        )

        # ====================================================
        # Panels
        # ====================================================

        panels = [

            (
                "🏢  MANAGEMENT",
                [
                    ("📊  School Overview", True),
                    ("📢  Announcements", True),
                    ("📅  School Calendar", True),
                    ("📈  Reports", False),
                    ("👥  Staff Management", False),
                ],
                (0.12, 0.32, 0.65, 1)
            ),

            (
                "👥  EXECUTIVE STAFF",
                [
                    ("📋  Attendance", True),
                    ("📝  Daily Tasks", True),
                    ("👨‍🎓  Student Records", False),
                    ("📊  Administrative Reports", False),
                ],
                (0.18, 0.50, 0.35, 1)
            ),

            (
                "👨‍🏫  TEACHERS",
                [
                    ("📝  Homework", True),
                    ("📊  Grades", True),
                    ("📅  Class Schedule", True),
                    ("📈  Student Performance", False),
                    ("📚  Question Bank", False),
                ],
                (0.20, 0.55, 0.28, 1)
            ),

            (
                "🧠  COUNSELING",
                [
                    ("💬  Counseling Requests", True),
                    ("📅  Appointments", True),
                    ("👨‍🎓  Student Counseling", False),
                    ("📊  Counseling Reports", False),
                ],
                (0.45, 0.25, 0.60, 1)
            ),

            (
                "👨‍👩‍👧  PARENTS",
                [
                    ("📢  Announcements", True),
                    ("💬  Parent Feedback", True),
                    ("👨‍🏫  Teacher Communication", False),
                    ("📅  Meetings", False),
                ],
                (0.65, 0.30, 0.35, 1)
            ),

            (
                "🎓  STUDENTS",
                [
                    ("👤  Student Profile", True),
                    ("📝  Homework", True),
                    ("📋  Attendance", False),
                    ("📊  Grades", False),
                    ("📈  Educational Progress", False),
                ],
                (0.25, 0.55, 0.55, 1)
            ),

            (
                "📚  QUESTION BANK",
                [
                    ("🔎  Browse Questions", True),
                    ("📝  Sample Questions", True),
                    ("➕  Create Question", False),
                    ("🗂️  Question Categories", False),
                ],
                (0.55, 0.35, 0.20, 1)
            ),

            (
                "💻  VIRTUAL CLASSES",
                [
                    ("🎥  Active Classes", True),
                    ("📅  Class Schedule", True),
                    ("🚀  Join Class", False),
                    ("🎬  Recorded Classes", False),
                ],
                (0.15, 0.45, 0.60, 1)
            ),

            (
                "💰  FINANCE",
                [
                    ("📊  Financial Overview", True),
                    ("💳  Payment Status", True),
                    ("📜  Payment History", False),
                    ("💳  Online Payment", False),
                ],
                (0.45, 0.40, 0.20, 1)
            ),

            (
                "📺  SMART BOARD",
                [
                    ("📢  School Announcements", True),
                    ("📅  Daily Schedule", True),
                    ("⚠️  Important Messages", False),
                    ("🚨  Emergency Notices", False),
                ],
                (0.30, 0.45, 0.65, 1)
            ),

            (
                "🤖  ARTIFICIAL INTELLIGENCE",
                [
                    ("💬  AI Assistant", True),
                    ("🎓  Educational Assistant", True),
                    ("📊  Smart Analysis", False),
                    ("📈  AI Reports", False),
                ],
                (0.55, 0.25, 0.55, 1)
            ),
        ]

        # ====================================================
        # Build Accordion Panels
        # ====================================================

        for title, items, panel_color in panels:

            panel_box = BoxLayout(
                orientation="vertical",
                size_hint_y=None,
                spacing=5,
                padding=[8, 8, 8, 8]
            )

            # ------------------------------------------------
            # Colored Background
            # ------------------------------------------------

            with panel_box.canvas.before:
                Color(
                    panel_color[0],
                    panel_color[1],
                    panel_color[2],
                    panel_color[3]
                )

                panel_box.background = RoundedRectangle(
                    pos=panel_box.pos,
                    size=panel_box.size,
                    radius=[18]
                )

            panel_box.bind(
                pos=lambda instance, value:
                self.update_background(instance),
                size=lambda instance, value:
                self.update_background(instance)
            )

            # ------------------------------------------------
            # Panel Header
            # ------------------------------------------------

            panel_button = Button(
                text=title,
                font_size=20,
                bold=True,
                size_hint_y=None,
                height=72,
                background_normal="",
                background_color=(
                    panel_color[0] * 0.75,
                    panel_color[1] * 0.75,
                    panel_color[2] * 0.75,
                    1
                )
            )

            panel_box.add_widget(panel_button)

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

                item_button = Button(
                    text=item_name,
                    font_size=17,
                    size_hint_y=None,
                    height=58,
                    background_normal="",
                    background_color=(
                        0.92,
                        0.92,
                        0.92,
                        1
                    )
                )

                item_button.bind(
                    on_press=lambda btn,
                    active=active:
                    self.open_section(
                        btn.text,
                        active
                    )
                )

                submenu.add_widget(item_button)

            panel_box.add_widget(submenu)

            # ------------------------------------------------
            # Accordion
            # ------------------------------------------------

            def toggle_panel(
                button,
                submenu=submenu,
                panel_box=panel_box
            ):

                if submenu.height == 0:

                    submenu.height = submenu.minimum_height

                else:

                    submenu.height = 0

                panel_box.height = (
                    72 +
                    submenu.height +
                    25
                )

            panel_button.bind(
                on_press=toggle_panel
            )

            # Initially closed
            panel_box.height = 95

            panels_layout.add_widget(panel_box)

        scroll.add_widget(panels_layout)

        root.add_widget(scroll)

        # ====================================================
        # Logout
        # ====================================================

        logout_button = Button(
            text="🚪  LOGOUT",
            font_size=18,
            bold=True,
            size_hint_y=None,
            height=60,
            background_normal="",
            background_color=(0.65, 0.15, 0.15, 1)
        )

        logout_button.bind(
            on_press=self.logout
        )

        root.add_widget(logout_button)

        self.add_widget(root)

    # ========================================================
    # Update Panel Background
    # ========================================================

    def update_background(self, instance):

        if hasattr(instance, "background"):
            instance.background.pos = instance.pos
            instance.background.size = instance.size

    # ========================================================
    # Open Section
    # ========================================================

    def open_section(self, section_name, active):

        if active:

            self.show_message(
                section_name,
                "This section is active.\n\n"
                "Demo content will be available here."
            )

        else:

            self.show_message(
                section_name,
                "COMING SOON\n\n"
                "This section is currently being updated.\n"
                "It will be available soon."
            )

    # ========================================================
    # Popup
    # ========================================================

    def show_message(self, title, message):

        content = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        content.add_widget(
            Label(
                text=message,
                font_size=18
            )
        )

        close_button = Button(
            text="OK",
            font_size=18,
            size_hint_y=None,
            height=55
        )

        content.add_widget(close_button)

        popup = Popup(
            title=title,
            content=content,
            size_hint=(0.88, 0.42),
            auto_dismiss=False
        )

        close_button.bind(
            on_press=popup.dismiss
        )

        popup.open()

    # ========================================================
    # Logout
    # ========================================================

    def logout(self, instance):

        if self.manager:
            self.manager.current = "login"
