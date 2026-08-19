import json
from pathlib import Path

SESSION_FILE = Path("frahoosh_session.json")

class SessionStore:
    def __init__(self):
        self.token = None
        self.user = {}
        self.load()

    def load(self):
        try:
            data = json.loads(SESSION_FILE.read_text(encoding="utf-8"))
            self.token = data.get("token")
            self.user = data.get("user") or {}
        except Exception:
            self.token, self.user = None, {}

    def save(self, token, user):
        self.token, self.user = token, user or {}
        SESSION_FILE.write_text(
            json.dumps({"token": token, "user": self.user}, ensure_ascii=False),
            encoding="utf-8"
        )

    def clear(self):
        self.token, self.user = None, {}
        try:
            SESSION_FILE.unlink()
        except FileNotFoundError:
            pass

    @property
    def role(self):
        return str(self.user.get("role") or "student").lower()
