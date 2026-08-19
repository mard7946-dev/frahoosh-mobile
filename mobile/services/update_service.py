import json
import os
import requests
from config import APP_VERSION, UPDATE_SERVER_URL

class UpdateService:
    @staticmethod
    def _version(value):
        try:
            return tuple(int(x) for x in str(value).split("."))
        except Exception:
            return (0,)

    def check_update(self):
        if not UPDATE_SERVER_URL:
            return {"success": False, "update_available": False,
                    "message": "سرور به‌روزرسانی هنوز تنظیم نشده است."}
        try:
            r = requests.get(UPDATE_SERVER_URL, timeout=10)
            r.raise_for_status()
            data = r.json()
            version = str(data.get("version", "")).strip()
            if not version:
                return {"success": False, "update_available": False,
                        "message": "اطلاعات نسخه معتبر نیست."}
            return {
                "success": True,
                "update_available": self._version(version) > self._version(APP_VERSION),
                "version": version,
                "title": data.get("title", "به‌روزرسانی جدید فراهوش"),
                "description": data.get("description", ""),
                "download_url": data.get("download_url", ""),
                "mandatory": bool(data.get("mandatory", False)),
            }
        except Exception as exc:
            return {"success": False, "update_available": False,
                    "message": f"خطا در بررسی نسخه: {exc}"}

    def download_apk(self, url, destination):
        if not url:
            return {"success": False, "message": "لینک APK موجود نیست."}
        try:
            folder = os.path.dirname(destination)
            if folder:
                os.makedirs(folder, exist_ok=True)
            with requests.get(url, stream=True, timeout=60) as r:
                r.raise_for_status()
                with open(destination, "wb") as out:
                    for chunk in r.iter_content(1024 * 64):
                        if chunk:
                            out.write(chunk)
            return {"success": True, "path": destination}
        except Exception as exc:
            return {"success": False, "message": f"خطا در دریافت APK: {exc}"}
