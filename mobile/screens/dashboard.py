# ============================================================
# Frahoosh Mobile
# Main Dashboard
# Demo Version
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
        # Main Layout
        # ====================================================

        root = BoxLayout(
            orientation="vertical",
            padding=[15, 15, 15, 15],
            spacing=10
        )

        # ====================================================
        # Header
        # ====================================================

        root.add_widget(
            Label(
                text="🏫 Welcome to Frahoosh",
                font_size=27,
                bold=True,
                size_hint_y=None,
                height=55
            )
        )

        root.add_widget(
            Label(
                text="Smart Educational Management System",
                font_size=16,
                size_hint_y=None,
                height=35
            )
        )

        # ====================================================
        # Scroll Area
        # ====================================================

        scroll = ScrollView(
            size_hint=(1, 1)
        )

        panels_layout = GridLayout(
            cols=1,
            spacing=10,
            padding=[5, 5, 5, 20],
            size_hint_y=None
        )

        panels_layout.bind(
            minimum_height=panels_layout.setter("height")
        )

        # ====================================================
        # Frahoosh Panels
        # ====================================================

        panels = [

            {
                "title": "🏢 Management",
                "items": [
                    ("📊 School Overview", True),
                    ("📢 Announcements", True),
                    ("📅 School Calendar", True),
                    ("📈 Reports", False),
                    ("👥 Staff Management", False),
                ]
            },

            {
                "title": "👥 Executive Staff",
                "items": [
                    ("📋 Attendance", True),
                    ("👨‍🎓 Student Records", False),
                    ("📝 Daily Tasks", True),
                    ("📊 Administrative Reports", False),
                ]
            },

            {
                "title": "👨‍🏫 Teachers",
                "items": [
                    ("📝 Homework", True),
                    ("📊 Grades", True),
                    ("📅 Class Schedule", True),
                    ("📈 Student Performance", False),
                    ("📚 Question Bank", False),
                ]
            },

            {
                "title": "🧠 Counseling",
                "items": [
                    ("💬 Counseling Requests", True),
                    ("📅 Appointments", True),
                    ("👨‍🎓 Student Counseling", False),
                    ("📊 Counseling Reports", False),
                ]
            },

            {
                "title": "👨‍👩‍👧 Parents",
                "items": [
                    ("📢 Announcements", True),
                    ("💬 Parent Feedback", True),
                    ("👨‍🏫 Teacher Communication", False),
                    ("📅 Meetings", False),
                ]
            },

            {
                "title": "🎓 Students",
                "items": [
                    ("👤 Student Profile", True),
                    ("📝 Homework", True),
                    ("📋 Attendance", False),
                    ("📊 Grades", False),
                    ("📈 Educational Progress", False),
                ]
            },

            {
                "title": "📚 Question Bank",
                "items": [
                    ("🔎 Browse Questions", True),
                    ("📝 Sample Questions", True),
                    ("➕ Create Question", False),
                    ("🗂️ Question Categories", False),
                ]
            },

            {
                "title": "💻 Virtual Classes",
                "items": [
                    ("🎥 Active Classes", True),
                    ("📅 Class Schedule", True),
                    ("🚀 Join Class", False),
                    ("🎬 Recorded Classes", False),
                ]
            },

            {
                "title": "💰 Finance",
                "items": [
                    ("📊 Financial Overview", True),
                    ("💳 Payment Status", True),
                    ("📜 Payment History", False),
                    ("💳 Online Payment", False),
                ]
            },

            {
                "title": "📺 Smart Board",
                "items": [
                    ("📢 School Announcements", True),
                    ("📅 Daily Schedule", True),
                    ("⚠️ Important Messages", False),
                    ("🚨 Emergency Notices", False),
                ]
            },

            {
                "title": "🤖 Artificial Intelligence",
                "items": [
                    ("💬 AI Assistant", True),
                    ("🎓 Educational Assistant", True),
                    ("📊 Smart Analysis", False),
                    ("📈 AI Reports", False),
                ]
            },

        ]

        # ====================================================
        # Create Panels
        # ====================================================

        for panel in panels:

            panel_box = BoxLayout(
                orientation="vertical",
                spacing=5,
                size_hint_y=None,
                padding=[5, 5, 5, 5]
            )

            panel_box.bind(
                minimum_height=panel_box.setter("height")
            )

            # ------------------------------------------------
            # Panel Title
            # ------------------------------------------------

            panel_box.add_widget(
                Label(
                    text=panel["title"],
                    font_size=21,
                    bold=True,
                    size_hint_y=None,
                    height=50
                )
            )

            # ------------------------------------------------
            # Submenus
            # ------------------------------------------------

            for item_name, active in panel["items"]:

                button = Button(
                    text=item_name,
                    font_size=16,
                    size_hint_y=None,
                    height=50
                )

                button.bind(
                    on_press=lambda btn,
                    active=active: self.open_section(
                        btn.text,
                        active
                    )
                )

                panel_box.add_widget(button)

            panels_layout.add_widget(panel_box)

        scroll.add_widget(panels_layout)

        root.add_widget(scroll)

        # ====================================================
        # Logout
        # ====================================================

        logout_button = Button(
            text="🚪 Logout",
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
                "🚧 Coming Soon\n\n"
                "This section is currently being updated.\n"
                "It will be available soon."
            )

    # ========================================================
    # Message Popup
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
                font_size=17
            )
        )

        close_button = Button(
            text="OK",
            size_hint_y=None,
            height=50
        )

        content.add_widget(close_button)

        popup = Popup(
            title=title,
            content=content,
            size_hint=(0.85, 0.4),
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
