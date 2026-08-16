# ============================================================
# Frahoosh Mobile
# Professional Accordion Dashboard
# Stable Version
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
                font_size=30,
                bold=True,
                size_hint_y=None,
                height=60
            )
        )

        root.add_widget(
            Label(
                text="Smart Educational Management System",
                font_size=17,
                size_hint_y=None,
                height=40
            )
        )

        # ====================================================
        # Scroll
        # ====================================================

        scroll = ScrollView(
            size_hint=(1, 1)
        )

        panels = GridLayout(
            cols=1,
            spacing=10,
            padding=[5, 5, 5, 20],
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
                "🏢  MANAGEMENT",
                [
                    ("School Overview", True),
                    ("Announcements", True),
                    ("School Calendar", True),
                    ("Reports", False),
                    ("Staff Management", False),
                ]
            ),

            (
                "👥  EXECUTIVE STAFF",
                [
                    ("Attendance", True),
                    ("Daily Tasks", True),
                    ("Student Records", False),
                    ("Administrative Reports", False),
                ]
            ),

            (
                "👨‍🏫  TEACHERS",
                [
                    ("Homework", True),
                    ("Grades", True),
                    ("Class Schedule", True),
                    ("Student Performance", False),
                    ("Question Bank", False),
                ]
            ),

            (
                "🧠  COUNSELING",
                [
                    ("Counseling Requests", True),
                    ("Appointments", True),
                    ("Student Counseling", False),
                    ("Counseling Reports", False),
                ]
            ),

            (
                "👨‍👩‍👧  PARENTS",
                [
                    ("Announcements", True),
                    ("Parent Feedback", True),
                    ("Teacher Communication", False),
                    ("Meetings", False),
                ]
            ),

            (
                "🎓  STUDENTS",
                [
                    ("Student Profile", True),
                    ("Homework", True),
                    ("Attendance", False),
                    ("Grades", False),
                    ("Educational Progress", False),
                ]
            ),

            (
                "📚  QUESTION BANK",
                [
                    ("Browse Questions", True),
                    ("Sample Questions", True),
                    ("Create Question", False),
                    ("Question Categories", False),
                ]
            ),

            (
                "💻  VIRTUAL CLASSES",
                [
                    ("Active Classes", True),
                    ("Class Schedule", True),
                    ("Join Class", False),
                    ("Recorded Classes", False),
                ]
            ),

            (
                "💰  FINANCE",
                [
                    ("Financial Overview", True),
                    ("Payment Status", True),
                    ("Payment History", False),
                    ("Online Payment", False),
                ]
            ),

            (
                "📺  SMART BOARD",
                [
                    ("School Announcements", True),
                    ("Daily Schedule", True),
                    ("Important Messages", False),
                    ("Emergency Notices", False),
                ]
            ),

            (
                "🤖  ARTIFICIAL INTELLIGENCE",
                [
                    ("AI Assistant", True),
                    ("Educational Assistant", True),
                    ("Smart Analysis", False),
                    ("AI Reports", False),
                ]
            ),
        ]

        # ====================================================
        # Create Accordion Panels
        # ====================================================

        for title, items in panel_data:

            panel = BoxLayout(
                orientation="vertical",
                size_hint_y=None,
                height=70,
                spacing=4
            )

            # ------------------------------------------------
            # Main Panel Button
            # ------------------------------------------------

            main_button = Button(
                text=title,
                font_size=20,
                bold=True,
                size_hint_y=None,
                height=70
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

            # ------------------------------------------------
            # Add Sub Items
            # ------------------------------------------------

            for item_name, active in items:

                if active:
                    text = "✓  " + item_name
                else:
                    text = "•  " + item_name

                item_button = Button(
                    text=text,
                    font_size=18,
                    size_hint_y=None,
                    height=58
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
            # Accordion Toggle
            # ------------------------------------------------

            def toggle(
                instance,
                submenu=submenu,
                panel=panel
            ):

                if submenu.height == 0:

                    submenu.height = submenu.minimum_height

                    panel.height = (
                        70 +
                        submenu.minimum_height +
                        4
                    )

                else:

                    submenu.height = 0

                    panel.height = 70

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
            text="LOGOUT",
            font_size=18,
            bold=True,
            size_hint_y=None,
            height=60
        )

        logout_button.bind(
            on_press=self.logout
        )

        root.add_widget(logout_button)

        self.add_widget(root)

    # ========================================================
    # Item Click
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
