# ============================================================
# Frahoosh Mobile
# سرویس مدیریت به‌روزرسانی
# ============================================================

import os
import json
import requests

from config import APP_VERSION, UPDATE_SERVER_URL


class UpdateService:

    def __init__(self):
        self.current_version = APP_VERSION
        self.server_url = UPDATE_SERVER_URL

    # ========================================================
    # مقایسه نسخه‌ها
    # ========================================================

    @staticmethod
    def is_newer_version(current_version, new_version):

        try:
            current = tuple(
                int(x) for x in current_version.split(".")
            )

            new = tuple(
                int(x) for x in new_version.split(".")
            )

            return new > current

        except Exception:
            return False

    # ========================================================
    # بررسی نسخه جدید
    # ========================================================

    def check_update(self):

        if not self.server_url:
            return {
                "success": False,
                "update_available": False,
                "message": "آدرس سرور به‌روزرسانی هنوز تنظیم نشده است."
            }

        try:

            response = requests.get(
                self.server_url,
                timeout=10
            )

            response.raise_for_status()

            data = response.json()

            latest_version = str(
                data.get("version", "")
            ).strip()

            if not latest_version:
                return {
                    "success": False,
                    "update_available": False,
                    "message": "اطلاعات نسخه جدید معتبر نیست."
                }

            update_available = self.is_newer_version(
                self.current_version,
                latest_version
            )

            return {
                "success": True,
                "update_available": update_available,
                "version": latest_version,
                "title": data.get(
                    "title",
                    "به‌روزرسانی جدید فراهوش"
                ),
                "description": data.get(
                    "description",
                    ""
                ),
                "download_url": data.get(
                    "download_url",
                    ""
                ),
                "mandatory": bool(
                    data.get("mandatory", False)
                )
            }

        except requests.RequestException as error:

            return {
                "success": False,
                "update_available": False,
                "message": f"خطا در ارتباط با سرور: {error}"
            }

        except (ValueError, json.JSONDecodeError):

            return {
                "success": False,
                "update_available": False,
                "message": "پاسخ سرور قابل خواندن نیست."
            }

        except Exception as error:

            return {
                "success": False,
                "update_available": False,
                "message": f"خطای غیرمنتظره: {error}"
            }

    # ========================================================
    # دانلود APK
    # ========================================================

    def download_apk(self, download_url, destination):

        if not download_url:
            return {
                "success": False,
                "message": "لینک دانلود APK موجود نیست."
            }

        try:

            os.makedirs(
                os.path.dirname(destination),
                exist_ok=True
            )

            with requests.get(
                download_url,
                stream=True,
                timeout=30
            ) as response:

                response.raise_for_status()

                with open(destination, "wb") as apk_file:

                    for chunk in response.iter_content(
                        chunk_size=8192):

                        if chunk:
                            apk_file.write(chunk)

            return {
                "success": True,
                "path": destination,
                "message": "دانلود نسخه جدید با موفقیت انجام شد."
            }

        except requests.RequestException as error:

            return {
                "success": False,
                "message": f"خطا در دانلود APK: {error}"
            }

        except Exception as error:

            return {
                "success": False,
                "message": f"خطا در ذخیره APK: {error}"
            }