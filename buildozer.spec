[app]

title = Frahoosh Mobile
package.name = frahoosh
package.domain = ir.frahoosh

source.dir = mobile
source.include_exts = py,png,jpg,jpeg,kv,json

version = 1.0.0

requirements = python3==3.11,kivy,requests

orientation = portrait
fullscreen = 0


[android]

android.api = 35
android.minapi = 23

android.ndk = 27c

android.archs = arm64-v8a

android.permissions = INTERNET


[buildozer]

log_level = 2
warn_on_root = 1
