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


[android]

android.api = 33

android.minapi = 24

android.ndk = 28c

android.ndk_api = 24

android.archs = arm64-v8a

android.permissions = INTERNET

android.accept_sdk_license = True


[buildozer]

log_level = 2

warn_on_root = 0


# Pin python-for-android to the stable 2024.01.21 release.
p4a.branch = master

p4a.commit = 957a3e5
