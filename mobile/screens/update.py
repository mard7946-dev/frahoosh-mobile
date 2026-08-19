from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from config import APP_VERSION
from services.update_service import UpdateService

class UpdateScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service = UpdateService()
        self.latest = None
        root = BoxLayout(orientation="vertical", padding=25, spacing=12)
        root.add_widget(Label(text="به‌روزرسانی فراهوش", font_size=27,
                              size_hint_y=None, height=60))
        root.add_widget(Label(text=f"نسخه فعلی: {APP_VERSION}",
                              size_hint_y=None, height=45))
        self.status = Label(text="برای بررسی نسخه جدید اقدام کنید.")
        root.add_widget(self.status)

        check = Button(text="بررسی به‌روزرسانی", size_hint_y=None, height=56)
        check.bind(on_press=self.check)
        root.add_widget(check)

        download = Button(text="دریافت APK جدید", size_hint_y=None, height=56)
        download.bind(on_press=self.download)
        root.add_widget(download)

        back = Button(text="بازگشت", size_hint_y=None, height=56)
        back.bind(on_press=lambda *_: setattr(self.manager, "current", "dashboard"))
        root.add_widget(back)
        self.add_widget(root)

    def check(self, _):
        result = self.service.check_update()
        self.latest = result if result.get("update_available") else None
        if result.get("success"):
            self.status.text = (
                f"نسخه جدید: {result['version']}\n{result.get('description','')}"
                if result.get("update_available")
                else "برنامه به‌روز است. ✓"
            )
        else:
            self.status.text = result.get("message", "خطا")

    def download(self, _):
        if not self.latest:
            Popup(title="به‌روزرسانی", content=Label(text="ابتدا نسخه جدید را بررسی کنید."),
                  size_hint=(0.85, 0.35)).open()
            return
        result = self.service.download_apk(self.latest.get("download_url",""),
                                           "frahoosh_update.apk")
        self.status.text = "APK دریافت شد." if result.get("success") else result.get("message","خطا")
