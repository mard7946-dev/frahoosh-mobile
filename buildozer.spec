[app]

# (str) Title of your application
title = Frahoosh Mobile

# (str) Package name
package.name = frahoosh

# (str) Package domain
package.domain = ir.frahoosh

# (str) Source code directory
source.dir = mobile

# (list) Source files to include
source.include_exts = py,png,jpg,jpeg,kv,json

# (str) Application version
version = 1.0.0

# (list) Application requirements
requirements = python3,kivy,requests==2.31.0,charset-normalizer==3.3.2

# (str) Supported orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 0


[android]

# (int) Android API
android.api = 35

# (int) Minimum Android API
android.minapi = 23

# (str) Android NDK version
android.ndk = 28b

# (bool) Accept Android SDK licenses
android.accept_sdk_license = True

# (str) Android architectures
android.archs = arm64-v8a, armeabi-v7a

# (list) Android permissions
android.permissions = INTERNET


[buildozer]

# (int) Log level
log_level = 2

# (bool) Warn when running as root
warn_on_root = 1
