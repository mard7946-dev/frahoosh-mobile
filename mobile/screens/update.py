# ============================================================
# Frahoosh Mobile
# صفحه به‌روزرسانی فراهوش
# ============================================================

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup

from config import APP_NAME, APP_VERSION
from services.update_service import UpdateService


class UpdateScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.update_service = UpdateService()

        root = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=18
        )

        root.add_widget(
            Label(
                text="به‌روزرسانی فراهوش",
                font_size=28,
                bold=True,
                size_hint_y=None,
                height=70
            )
        )

        root.add_widget(
            Label(
                text=APP_NAME,
                font_size=20,
                size_hint_y=None,
                height=45
            )
        )

        root.add_widget(
            Label(
                text=f"نسخه فعلی: {APP_VERSION}",
                font_size=18,
                size_hint_y=None,
                height=50
            )
        )

        self.status_label = Label(
            text="برای بررسی نسخه جدید، دکمه زیر را بزنید.",
            font_size=16
        )

        root.add_widget(self.status_label)

        self.check_button = Button(
            text="بررسی به‌روزرسانی",
            size_hint_y=None,
            height=60
        )

        self.check_button.bind(
            on_press=self.check_update
        )

        root.add_widget(self.check_button)

        self.download_button = Button(
            text="دریافت نسخه جدید",
            size_hint_y=None,
            height=60,
            disabled=True
        )

        self.download_button.bind(
            on_press=self.download_update
        )

        root.add_widget(self.download_button)

        back_button = Button(
            text="بازگشت",
            size_hint_y=None,
            height=55
        )

        back_button.bind(
            on_press=self.go_back
        )

        root.add_widget(back_button)

        self.add_widget(root)

        self.latest_update = None

    # ========================================================
    # بررسی نسخه جدید
    # ========================================================

    def check_update(self, instance):

        self.check_button.disabled = True

        self.status_label.text = (
            "در حال بررسی نسخه جدید..."
        )

        result = self.update_service.check_update()

        self.check_button.disabled = False

        if not result.get("success"):

            self.status_label.text = result.get(
                "message",
                "بررسی به‌روزرسانی انجام نشد."
            )

            return

        if not result.get("update_available"):

            self.status_label.text = (
                "نسخه شما به‌روز است. ✓"
            )

            self.download_button.disabled = True
            return

        self.latest_update = result

        version = result.get(
            "version",
            "نامشخص"
        )

        title = result.get(
            "title",
            "به‌روزرسانی جدید"
        )

        description = result.get(
            "description",
            ""
        )

        self.status_label.text = (
            f"{title}\n"
            f"نسخه جدید: {version}\n"
            f"{description}"
        )

        self.download_button.disabled = False

        if result.get("mandatory"):

            self.show_message(
                "به‌روزرسانی ضروری",
                "برای ادامه استفاده از فراهوش، "
                "باید نسخه جدید را دریافت کنید."
            )

    # ========================================================
    # دانلود APK
    # ========================================================

    def download_update(self, instance):
        if not self.latest_update:
            return

        download_url = self.latest_update.get(
            "download_url",
            ""
        )

        if not download_url:

            self.show_message(
                "خطا",
                "لینک دریافت نسخه جدید موجود نیست."
            )

            return

        self.download_button.disabled = True

        self.status_label.text = (
            "در حال دریافت نسخه جدید..."
        )

        destination = (
            "frahoosh_update.apk"
        )

        result = self.update_service.download_apk(
            download_url,
            destination
        )

        self.download_button.disabled = False

        if result.get("success"):

            self.status_label.text = (
                "نسخه جدید با موفقیت دریافت شد."
            )

            self.show_message(
                "آماده نصب",
                "نسخه جدید فراهوش دریافت شد.\n\n"
                "مرحله نصب APK را در بخش مخصوص اندروید "
                "به این سیستم اضافه می‌کنیم."
            )

        else:

            self.status_label.text = result.get(
                "message",
                "دریافت نسخه جدید ناموفق بود."
            )

    # ========================================================
    # پیام
    # ========================================================

    def show_message(self, title, message):

        popup = Popup(
            title=title,
            content=Label(
                text=message
            ),
            size_hint=(0.85, 0.45)
        )

        popup.open()

    # ========================================================
    # بازگشت
    # ========================================================

    def go_back(self, instance):

        self.manager.current = "dashboard"