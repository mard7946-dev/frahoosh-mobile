from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup

from config import APP_NAME, SYSTEM_TITLE, APP_VERSION, ROLE_TITLES
from services.api import APIError

class DashboardScreen(Screen):
    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        root = BoxLayout(orientation="vertical", padding=18, spacing=8)

        header = BoxLayout(size_hint_y=None, height=70)
        self.title = Label(text=APP_NAME, font_size=25, bold=True)
        header.add_widget(self.title)
        root.add_widget(header)

        self.status = Label(text=SYSTEM_TITLE, size_hint_y=None, height=48)
        root.add_widget(self.status)

        scroll = ScrollView()
        self.grid = GridLayout(cols=1, spacing=8, size_hint_y=None)
        self.grid.bind(minimum_height=self.grid.setter("height"))
        scroll.add_widget(self.grid)
        root.add_widget(scroll)

        bottom = BoxLayout(size_hint_y=None, height=58, spacing=8)
        refresh = Button(text="تازه‌سازی")
        refresh.bind(on_press=lambda *_: self.refresh())
        logout = Button(text="خروج")
        logout.bind(on_press=self.logout)
        bottom.add_widget(refresh)
        bottom.add_widget(logout)
        root.add_widget(bottom)

        self.add_widget(root)

    def _add(self, title, path):
        b = Button(text=title, size_hint_y=None, height=54)
        b.bind(on_press=lambda *_: self.open_module(title, path))
        self.grid.add_widget(b)

    def refresh(self):
        self.grid.clear_widgets()
        user = self.app.session.user
        role = self.app.session.role
        self.title.text = f"{APP_NAME} — {ROLE_TITLES.get(role, role)}"
        name = user.get("name") or user.get("full_name") or user.get("username", "")
        self.status.text = f"کاربر: {name}"

        self._add("اطلاعیه‌ها", "/api/v1/notifications")
        self._add("کلاس‌های من", "/api/v1/classes")
        self._add("حضور و غیاب", "/api/v1/attendance")

        role_modules = {
            "admin": ["مدیریت", "/api/v1/admin/summary"],
            "vice": ["معاونت آموزشی", "/api/v1/vice/summary"],
            "teacher": ["پنل دبیر", "/api/v1/teacher/summary"],
            "student": ["پنل دانش‌آموز", "/api/v1/student/summary"],
            "parent": ["پنل اولیا", "/api/v1/parent/summary"],
            "counselor": ["پنل مشاوره", "/api/v1/counselor/summary"],
            "finance": ["پنل مالی", "/api/v1/finance/summary"],
            "cultural": ["پنل فرهنگی", "/api/v1/cultural/summary"],
            "smartboard": ["تابلوی هوشمند", "/api/v1/smartboard/summary"],
            "ai": ["هوش مصنوعی", "/api/v1/ai/summary"],
        }
        item = role_modules.get(role)
        if item:
            self._add(*item)

        self._add("کلاس مجازی", "/api/v1/virtual-classes")
        self._add("به‌روزرسانی", "__update__")

    def open_module(self, title, path):
        if path == "__update__":
            self.manager.current = "update"
            return
        try:
            data = self.app.api.generic(path)
            self.show_json(title, data)
        except APIError as exc:
            self.show_json(title, {"error": str(exc)})

    def show_json(self, title, data):
        import json
        text = json.dumps(data, ensure_ascii=False, indent=2)
        Popup(title=title, content=Label(text=text),
              size_hint=(0.92, 0.8)).open()

    def logout(self, _):
        self.app.session.clear()
        self.app.api.set_token(None)
        self.manager.current = "login"
