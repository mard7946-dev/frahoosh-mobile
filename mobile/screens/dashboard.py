# ============================================================
# Frahoosh Mobile
# Professional Dashboard
# Accordion Panels
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
        # Main
        # ====================================================

        root = BoxLayout(
            orientation="vertical",
            padding=[15, 15, 15, 15],
            spacing=12
        )

        # ====================================================
        # Header
        # ====================================================

        root.add_widget(
            Label(
                text="🏫 FRAHOOSH",
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

        panels_layout = GridLayout(
            cols=1,
            spacing=10,
            padding=[5, 5, 5, 15],
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
                ]
            ),

            (
                "👥  EXECUTIVE STAFF",
                [
                    ("📋  Attendance", True),
                    ("📝  Daily Tasks", True),
                    ("👨‍🎓  Student Records", False),
                    ("📊  Administrative Reports", False),
                ]
            ),

            (
                "👨‍🏫  TEACHERS",
                [
                    ("📝  Homework", True),
                    ("📊  Grades", True),
                    ("📅  Class Schedule", True),
                    ("📈  Student Performance", False),
                    ("📚  Question Bank", False),
                ]
            ),

            (
                "🧠  COUNSELING",
                [
                    ("💬  Counseling Requests", True),
                    ("📅  Appointments", True),
                    ("👨‍🎓  Student Counseling", False),
                    ("📊  Counseling Reports", False),
                ]
            ),

            (
                "👨‍👩‍👧  PARENTS",
                [
                    ("📢  Announcements", True),
                    ("💬  Parent Feedback", True),
                    ("👨‍🏫  Teacher Communication", False),
                    ("📅  Meetings", False),
                ]
            ),

            (
                "🎓  STUDENTS",
                [
                    ("👤  Student Profile", True),
                    ("📝  Homework", True),
                    ("📋  Attendance", False),
                    ("📊  Grades", False),
                    ("📈  Educational Progress", False),
                ]
            ),

            (
                "📚  QUESTION BANK",
                [
                    ("🔎  Browse Questions", True),
                    ("📝  Sample Questions", True),
                    ("➕  Create Question", False),
                    ("🗂️  Question Categories", False),
                ]
            ),

            (
                "💻  VIRTUAL CLASSES",
                [
                    ("🎥  Active Classes", True),
                    ("📅  Class Schedule", True),
                    ("🚀  Join Class", False),
                    ("🎬  Recorded Classes", False),
                ]
            ),

            (
                "💰  FINANCE",
                [
                    ("📊  Financial Overview", True),
                    ("💳  Payment Status", True),
                    ("📜  Payment History", False),
                    ("💳  Online Payment", False),
                ]
            ),

            (
                "📺  SMART BOARD",
                [
                    ("📢  School Announcements", True),
                    ("📅  Daily Schedule", True),
                    ("⚠️  Important Messages", False),
                    ("🚨  Emergency Notices", False),
                ]
            ),

            (
                "🤖  ARTIFICIAL INTELLIGENCE",
                [
                    ("💬  AI Assistant", True),
                    ("🎓  Educational Assistant", True),
                    ("📊  Smart Analysis", False),
                    ("📈  AI Reports", False),
                ]
            ),
        ]

        # ====================================================
        # Create Accordion Panels
        # ====================================================

        for title, items in panels:

            panel_box = BoxLayout(
                orientation="vertical",
                size_hint_y=None,
                spacing=5
            )

            # ------------------------------------------------
            # Main Panel Button
            # ------------------------------------------------

            panel_button = Button(
                text=title,
                font_size=20,
                bold=True,
                size_hint_y=None,
                height=75
            )

            panel_box.add_widget(panel_button)

            # ------------------------------------------------
            # Submenu container
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

            # ------------------------------------------------
            # Submenus
            # ------------------------------------------------

            for item_name, active in items:

                item_button = Button(
                    text=item_name,
                    font_size=17,
                    size_hint_y=None,
                    height=58
                )

                item_button.bind(
                    on_press=lambda btn,
                    active=active: self.open_section(
                        btn.text,
                        active
                    )
                )

                submenu.add_widget(item_button)

            panel_box.add_widget(submenu)

            # ------------------------------------------------
            # Accordion function
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
                    panel_button.height +
                    submenu.height +
                    5
                )

            panel_button.bind(
                on_press=toggle_panel
            )

            # Initially collapsed
            panel_box.height = panel_button.height + 5

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
            height=60
        )

        logout_button.bind(
            on_press=self.logout
        )

        root.add_widget(logout_button)

        self.add_widget(root)

    # ========================================================
    # Section
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
                "🚧  COMING SOON\n\n"
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
            font_size=17,
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
