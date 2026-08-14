- name: Build APK
        run: |
          docker run --rm \
            --volume "$HOME/.buildozer:/home/user/.buildozer" \
            --volume "$GITHUB_WORKSPACE:/home/user/hostcwd" \
            kivy/buildozer:latest \
            bash -lc '
              cd /home/user/hostcwd

              export ANDROID_HOME="$HOME/.buildozer/android/platform/android-sdk"
              export ANDROID_SDK_ROOT="$ANDROID_HOME"

              export PATH="$ANDROID_HOME/platform-tools:$ANDROID_HOME/build-tools/35.0.0:$PATH"

              echo "ANDROID_HOME=$ANDROID_HOME"

              echo "Checking AIDL..."
              "$ANDROID_HOME/build-tools/35.0.0/aidl" --version

              echo "Starting Buildozer..."

              printf "y\n" | buildozer android debug
            '
