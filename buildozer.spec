[app]

title = Frahoosh Mobile
package.name = frahoosh
package.domain = ir.frahoosh

source.dir = mobile
source.include_exts = py,png,jpg,jpeg,svg,kv,json,txt

version = 1.0.0

requirements = python3,kivy,requests

orientation = portrait
fullscreen = 0


# --------------------------------
# Android
# --------------------------------

android.api = 33
android.minapi = 24

android.ndk = 28c
android.ndk_api = 24

android.archs = arm64-v8a

android.permissions = INTERNET

android.accept_sdk_license = True

# Use GitHub Actions system Android SDK
android.sdk_path = /usr/local/lib/android/sdk

# Do not let Buildozer update/download another SDK
android.skip_update = True


[buildozer]

log_level = 2
warn_on_root = 0
