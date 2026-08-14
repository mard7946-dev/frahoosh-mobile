import requests

from config import APP_VERSION, UPDATE_SERVER_URL


class UpdateService:

    def __init__(self):
        self.current_version = APP_VERSION
        self.server_url = UPDATE_SERVER_URL

    def check_for_update(self):
        try:
            response = requests.get(
                self.server_url,
                timeout=10
            )

            if response.status_code != 200:
                return {
                    "success": False,
                    "message": "خطا در دریافت اطلاعات به‌روزرسانی"
                }

            data = response.json()

            latest_version = data.get("version")

            if not latest_version:
                return {
                    "success": False,
                    "message": "نسخه جدید مشخص نشده است"
                }

            if latest_version != self.current_version:
                return {
                    "success": True,
                    "update_available": True,
                    "version": latest_version,
                    "download_url": data.get("download_url", ""),
                    "changelog": data.get("changelog", "")
                }

            return {
                "success": True,
                "update_available": False,
                "version": self.current_version
            }

        except Exception as e:
            return {
                "success": False,
                "message": str(e)
            }
