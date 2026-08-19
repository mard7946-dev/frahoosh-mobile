import requests
from config import API_BASE_URL, API_TIMEOUT, PUBLIC_API_KEY

class APIError(Exception):
    pass

class APIClient:
    def __init__(self, base_url=None, token=None):
        self.base_url = (base_url if base_url is not None else API_BASE_URL).rstrip("/")
        self.token = token

    @property
    def enabled(self):
        return bool(self.base_url)

    def set_token(self, token):
        self.token = token

    def _headers(self):
        headers = {"Accept": "application/json"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        if PUBLIC_API_KEY:
            headers["X-API-Key"] = PUBLIC_API_KEY
        return headers

    def request(self, method, path, **kwargs):
        if not self.enabled:
            raise APIError("آدرس سرور فراهوش تنظیم نشده است.")
        url = f"{self.base_url}/{path.lstrip('/')}"
        headers = self._headers()
        headers.update(kwargs.pop("headers", {}) or {})
        try:
            response = requests.request(
                method, url, headers=headers, timeout=API_TIMEOUT, **kwargs
            )
            if response.status_code == 401:
                raise APIError("نشست کاربری منقضی شده است.")
            if not response.ok:
                try:
                    detail = response.json().get("message", response.text)
                except Exception:
                    detail = response.text
                raise APIError(f"خطای سرور ({response.status_code}): {detail}")
            if not response.content:
                return {}
            return response.json()
        except requests.RequestException as exc:
            raise APIError(f"عدم دسترسی به سرور: {exc}") from exc

    def login(self, username, password):
        data = self.request("POST", "/api/v1/auth/login",
                             json={"username": username, "password": password})
        token = data.get("access_token") or data.get("token")
        user = data.get("user") or {}
        if not token:
            raise APIError("پاسخ ورود فاقد توکن معتبر است.")
        return token, user

    def me(self):
        return self.request("GET", "/api/v1/me")

    def notifications(self, limit=50):
        return self.request("GET", "/api/v1/notifications", params={"limit": limit})

    def dashboard(self):
        return self.request("GET", "/api/v1/dashboard")

    def classes(self):
        return self.request("GET", "/api/v1/classes")

    def class_detail(self, class_id):
        return self.request("GET", f"/api/v1/classes/{class_id}")

    def attendance(self, class_id=None):
        params = {"class_id": class_id} if class_id else {}
        return self.request("GET", "/api/v1/attendance", params=params)

    def generic(self, path, method="GET", **kwargs):
        return self.request(method, path, **kwargs)
