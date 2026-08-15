from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screens.login import LoginScreen

class FrahooshMobileApp(App):

```
def build(self):
    manager = ScreenManager()

    manager.add_widget(
        LoginScreen(name="login")
    )

    manager.current = "login"

    return manager
```

if **name** == "**main**":
FrahooshMobileApp().run()
