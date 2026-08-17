# ============================================================
# Frahoosh Mobile
# Main - Safe Startup Diagnostic
# ============================================================

import os
import traceback

# جلوگیری از بعضی مشکلات اولیه SDL / صوت
os.environ.setdefault("KIVY_GL_BACKEND", "gles2")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

LOG_FILE = "/sdcard/frahoosh_startup.log"


def write_log(message):
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(message + "\n")
    except Exception:
        pass


write_log("========================================")
write_log("FRAHOOSH START")
write_log("========================================")

try:

    write_log("STEP 1: importing kivy")

    from kivy.app import App
    from kivy.uix.screenmanager import ScreenManager

    write_log("STEP 2: importing login")

    from screens.login import LoginScreen

    write_log("STEP 3: importing dashboard")

    from screens.dashboard import DashboardScreen

    write_log("STEP 4: imports completed")


    class FrahooshMobileApp(App):

        def build(self):

            write_log("STEP 5: build started")

            manager = ScreenManager()

            write_log("STEP 6: creating LoginScreen")

            manager.add_widget(
                LoginScreen(name="login")
            )

            write_log("STEP 7: LoginScreen created")

            manager.add_widget(
                DashboardScreen(name="dashboard")
            )

            write_log("STEP 8: DashboardScreen created")

            manager.current = "login"

            write_log("STEP 9: login selected")

            return manager


    write_log("STEP 10: starting application")

    FrahooshMobileApp().run()

    write_log("STEP 11: application ended normally")


except Exception as e:

    write_log("========================================")
    write_log("FRAHOOSH CRASH")
    write_log("========================================")

    write_log(
        "ERROR: " + repr(e)
    )

    write_log(
        traceback.format_exc()
    )

    raise
