# Creator Hub

A personal creator-dashboard app with a clean, card-based look. Everything is editable: the app name and icon, the channel or store name and picture, fonts, currency, app size, stats, labels, status icons, comments and videos.

The whole app is one page, `web/index.html`. The Android and iOS apps are thin native shells around it.

## Folders

| Folder | What it is |
| --- | --- |
| `web/index.html` | The app itself (HTML, CSS and JS in one file). Open it in any browser. |
| `android/` | Android shell (Java WebView). `./build.sh` makes `bin/SmoreHub.apk`. |
| `ios/` | iOS shell (C on the Objective-C runtime, WKWebView). `./build.sh` makes `build/CreatorHub.ipa`. |
| `releases/` | Prebuilt `SmoreHub.apk` (Android) and `CreatorHub.ipa` (iOS, unsigned). |
| `tools/render-icons.js` | Renders the 90 iOS home-screen icons from the app's icon presets (Playwright). |

## Install

- **Android:** copy `releases/SmoreHub.apk` to the phone, open it, and allow installs from unknown sources.
- **iPhone:** open `releases/CreatorHub.ipa` in Sideloadly, sign with your Apple ID, then trust the profile under Settings → General → VPN & Device Management (and turn on Developer Mode on iOS 16+).

## Build

- **Android** (Ubuntu): `apt-get install aapt apksigner zipalign dalvik-exchange android-sdk-platform-23`, then `android/build.sh`. It creates a signing key (`android/smore.p12`) on first run. Keep that file to install updates over an existing install; it is git-ignored.
- **iOS** (Linux, no Xcode needed): `apt-get install clang lld-18`, then `ios/build.sh`.

After editing `web/index.html`, rebuild both shells so the apps get the change.

## Temporary branding

The phone display name is `Youtube studio` on Android and iOS. The supplied temporary icon is preserved in `branding/app-icon.png`.

To resize a replacement icon for both platforms, install Pillow (`python -m pip install Pillow`) and run `python tools/prepare-branding.py`. The alternate-icon renderer leaves these primary icons alone. The default in-app image is embedded in `web/index.html` so both native packages can load it offline; update that default too when replacing the image. Existing saved in-app customizations remain intact.

The refreshed iOS IPA is unsigned and still needs signing with Sideloadly. The refreshed Android APK uses a newly generated signing key because the original key is not in this repository. It cannot update an installation signed with the previous key; uninstalling that installation removes its saved settings. The new key is kept locally at the git-ignored `android/smore.p12` for subsequent builds.
