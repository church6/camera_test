# pylint: disable=C0301
"""
# @filename    :  nighthawk.py
# @author      :  Copyright (C) Church.ZHONG
"""

CAMERA_CLAIM = ("default camera", "back camera", "front camera")

CAMERA_ZOOM_RADIOS = {
    "night": {"back camera": ["zoom 1", "zoom 3"], "front camera": ["default"]},
    "portrait": {"back camera": ["default"], "front camera": ["zoom 1", "zoom 2"]},
    "photo": {"back camera": ["zoom 1", "zoom 3"], "front camera": ["zoom 1", "zoom 2"]},
    "burstshot": {"back camera": ["zoom 1", "zoom 3"], "front camera": ["zoom 1", "zoom 2"]},
    "flashshot": {"default camera": ["zoom 1", "zoom 3"]},
    "video": {"back camera": ["zoom 1", "zoom 3"], "front camera": ["default"]},
    "dualsight": {"back camera": ["default"], "front camera": ["default"]},
    "timelapse": {"back camera": ["default"], "front camera": ["default"]},
    "panorama": {"default camera": ["default"]},
    "slowmotion": {"back camera": ["default"], "front camera": ["default"]},
    "professional": {"default camera": ["default"]},
}

CAMERA_HDR_MODES = {
    "night": {"back camera": ["default"], "front camera": ["default"]},
    "portrait": {"back camera": ["hdr auto", "hdr on", "hdr off"], "front camera": ["hdr auto", "hdr on", "hdr off"]},
    "photo": {"back camera": ["hdr auto", "hdr on", "hdr off"], "front camera": ["hdr auto", "hdr on", "hdr off"]},
    "burstshot": {"back camera": ["hdr auto", "hdr on", "hdr off"], "front camera": ["hdr auto", "hdr on", "hdr off"]},
    "flashshot": {"default camera": ["default"]},
    "video": {"back camera": ["default"], "front camera": ["default"]},
    "dualsight": {"back camera": ["default"], "front camera": ["default"]},
    "timelapse": {"back camera": ["default"], "front camera": ["default"]},
    "panorama": {"default camera": ["default"]},
    "slowmotion": {"back camera": ["default"], "front camera": ["default"]},
    "professional": {"default camera": ["default"]},
}

CAMERA_FLASH_MODES = {
    "night": {"back camera": ["default"], "front camera": ["flash auto", "flash on", "flash off"]},
    "portrait": {"back camera": ["default"], "front camera": ["flash auto", "flash on", "flash off"]},
    "photo": {"back camera": ["flash auto", "flash on", "flash off"], "front camera": ["flash auto", "flash on", "flash off"]},
    "burstshot": {
        "back camera": ["flash auto", "flash on", "flash off"],
        "front camera": ["flash auto", "flash on", "flash off"],
    },
    "flashshot": {"default camera": ["default"]},
    "video": {"back camera": ["default"], "front camera": ["default"]},
    "dualsight": {"back camera": ["default"], "front camera": ["default"]},
    "timelapse": {"back camera": ["default"], "front camera": ["default"]},
    "panorama": {"default camera": ["default"]},
    "slowmotion": {"back camera": ["default"], "front camera": ["default"]},
    "professional": {"default camera": ["flash auto", "flash on", "flash off"]},
}

CAMERA_AIPORTRAIT_MODES = {
    "night": {"back camera": ["ai portrait on", "ai portrait off"], "front camera": ["ai portrait on", "ai portrait off"]},
    "portrait": {"back camera": ["ai portrait on", "ai portrait off"], "front camera": ["ai portrait on", "ai portrait off"]},
    "photo": {"back camera": ["ai portrait on", "ai portrait off"], "front camera": ["ai portrait on", "ai portrait off"]},
    "burstshot": {"back camera": ["ai portrait on", "ai portrait off"], "front camera": ["ai portrait on", "ai portrait off"]},
    "flashshot": {"default camera": ["default"]},
    "video": {"back camera": ["default"], "front camera": ["default"]},
    "dualsight": {"back camera": ["default"], "front camera": ["default"]},
    "timelapse": {"back camera": ["default"], "front camera": ["default"]},
    "panorama": {"default camera": ["default"]},
    "slowmotion": {"back camera": ["default"], "front camera": ["default"]},
    "professional": {"default camera": ["default"]},
}

CLASS_VIEW_VIEW = "android.view.View"
CLASS_WIDGET_CHECKEDTEXTVIEW = "android.widget.CheckedTextView"
CLASS_WIDGET_CHECKBOX = "android.widget.CheckBox"
CLASS_WIDGET_EDITTEXT = "android.widget.EditText"
CLASS_WIDGET_SPINNER = "android.widget.Spinner"
CLASS_WIDGET_TEXTVIEW = "android.widget.TextView"
CLASS_WIDGET_BUTTON = "android.widget.Button"
CLASS_WIDGET_IMAGEVIEW = "android.widget.ImageView"
CLASS_WIDGET_IMAGEBUTTON = "android.widget.ImageButton"
CLASS_WIDGET_SWITCH = "android.widget.Switch"
CLASS_WIDGET_FRAMELAYOUT = "android.widget.FrameLayout"
CLASS_WIDGET_CHECKEDTEXTVIEW = "android.widget.CheckedTextView"

ANDROID_LAUNCHER3_PACKAGE_NAME = "com.android.launcher3"
ANDROID_SETTINGS_PACKAGE_NAME = "com.android.settings"
GOOGLE_PERMISSION_CONTROLLER_PACKAGE_NAME = "com.google.android.permissioncontroller"
GOOGLE_ANDROID_PHOTOS_PACKAGE_NAME = "com.google.android.apps.photos"
HMD_CAMERA_PACKAGE_NAME = "com.hmdglobal.app.camera"
HMD_ACTIVATION_PACKAGE_NAME = "com.hmdglobal.app.activation"
QTI_CAMERA_PROVIDER_PROCESS_NAME = "vendor.qti.camera.provider@2.7-service_64"

NODE_KEY_TEXT = "text"
NODE_KEY_RESOURCEID = "resourceId"
NODE_KEY_CLASSNAME = "className"
NODE_KEY_PACKAGENAME = "packageName"
NODE_KEY_DESCRIPTION = "description"
NODES = {
    # [enter]add wifi network
    "wifi add button": {
        NODE_KEY_TEXT: "Add network",
        NODE_KEY_PACKAGENAME: ANDROID_SETTINGS_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: "android:id/title",
    },
    "wifi ssid edit": {
        NODE_KEY_TEXT: "Enter the SSID",
        NODE_KEY_PACKAGENAME: ANDROID_SETTINGS_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_EDITTEXT,
        NODE_KEY_RESOURCEID: f"{ANDROID_SETTINGS_PACKAGE_NAME}:id/ssid",
    },
    "wifi security spinner": {
        NODE_KEY_PACKAGENAME: ANDROID_SETTINGS_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_SPINNER,
        NODE_KEY_RESOURCEID: f"{ANDROID_SETTINGS_PACKAGE_NAME}:id/security",
    },
    "wifi security wpa/wpa2": {
        NODE_KEY_TEXT: "WPA/WPA2-Personal",
        NODE_KEY_PACKAGENAME: ANDROID_SETTINGS_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_CHECKEDTEXTVIEW,
        NODE_KEY_RESOURCEID: "android:id/text1",
    },
    "wifi password edit": {
        NODE_KEY_PACKAGENAME: ANDROID_SETTINGS_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_EDITTEXT,
        NODE_KEY_RESOURCEID: f"{ANDROID_SETTINGS_PACKAGE_NAME}:id/password",
    },
    "wifi save button": {
        NODE_KEY_TEXT: "Save",
        NODE_KEY_PACKAGENAME: ANDROID_SETTINGS_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_BUTTON,
        NODE_KEY_RESOURCEID: "android:id/button1",
    },
    # [leave]add wifi network
    "wakeup screen": {
        NODE_KEY_PACKAGENAME: "com.android.systemui",
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
        NODE_KEY_RESOURCEID: "com.android.systemui:id/lock_icon",
    },
    "home screen": {
        NODE_KEY_PACKAGENAME: ANDROID_LAUNCHER3_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_FRAMELAYOUT,
        NODE_KEY_RESOURCEID: f"{ANDROID_LAUNCHER3_PACKAGE_NAME}:id/overview_actions_view",
    },
    "atx keeps stopping": {
        NODE_KEY_TEXT: "ATX keeps stopping",
        NODE_KEY_PACKAGENAME: "android",
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: "android:id/alertTitle",
    },
    "close app button": {
        NODE_KEY_TEXT: "Close app",
        NODE_KEY_PACKAGENAME: "android",
        NODE_KEY_CLASSNAME: CLASS_WIDGET_BUTTON,
        NODE_KEY_RESOURCEID: "android:id/aerr_close",
    },
    "settings display": {
        NODE_KEY_TEXT: "Display",
        NODE_KEY_PACKAGENAME: ANDROID_SETTINGS_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: "android:id/title",
    },
    "dark theme toggle": {
        NODE_KEY_DESCRIPTION: "Dark theme",
        NODE_KEY_PACKAGENAME: ANDROID_SETTINGS_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_SWITCH,
        NODE_KEY_RESOURCEID: f"{ANDROID_SETTINGS_PACKAGE_NAME}:id/switchWidget",
    },
    # [enter][agenda]
    "location permission button allow": {
        NODE_KEY_PACKAGENAME: GOOGLE_PERMISSION_CONTROLLER_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_BUTTON,
        NODE_KEY_RESOURCEID: "com.android.permissioncontroller:id/permission_allow_foreground_only_button",
    },
    "notifications permission button allow": {
        NODE_KEY_PACKAGENAME: GOOGLE_PERMISSION_CONTROLLER_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_BUTTON,
        NODE_KEY_RESOURCEID: "com.android.permissioncontroller:id/permission_allow_button",
    },
    "agenda button": {
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEBUTTON,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/agenda_button",
    },
    "next button": {
        # "common" next button
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEBUTTON,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/button_next",
    },
    # [leave][agenda]
    # bottom
    "front camera": {
        NODE_KEY_DESCRIPTION: "Front camera",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/camera_toggle_button",
    },
    "back camera": {
        NODE_KEY_DESCRIPTION: "Back camera",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/camera_toggle_button",
    },
    "shutter": {
        NODE_KEY_DESCRIPTION: "Shutter",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/shutter_button",
    },
    "photos": {
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_VIEW_VIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/rounded_thumbnail_view",
    },
    "edit button": {
        NODE_KEY_TEXT: "Edit",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_BUTTON,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/mode_edit_btn",
    },
    # [enter]RecyclerView
    "more functions": {
        NODE_KEY_DESCRIPTION: "More",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_VIEW_VIEW,
    },
    "video": {
        NODE_KEY_DESCRIPTION: "Video",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_VIEW_VIEW,
    },
    "photo": {
        NODE_KEY_DESCRIPTION: "Photo",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_VIEW_VIEW,
    },
    "portrait": {
        NODE_KEY_DESCRIPTION: "Portrait",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_VIEW_VIEW,
    },
    "night": {
        NODE_KEY_DESCRIPTION: "Night",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_VIEW_VIEW,
    },
    # [leave]RecyclerView
    # [enter]dropdown settings
    "more settings closed button": {
        NODE_KEY_DESCRIPTION: "More settings closed",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/more_settings_button",
    },
    "more settings opened button": {
        NODE_KEY_DESCRIPTION: "More settings opened",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/more_settings_button",
    },
    "watermark toggle": {
        NODE_KEY_TEXT: "Watermark",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/txt_list_more_settings",
    },
    "high resolution toggle": {
        NODE_KEY_TEXT: "High resolution",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/txt_list_more_settings",
    },
    "focus peaking toggle": {
        NODE_KEY_TEXT: "Focus peaking",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/txt_list_more_settings",
    },
    "eyes tracking toggle": {
        NODE_KEY_TEXT: "Eyes tracking",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/txt_list_more_settings",
    },
    "selfie gesture toggle": {
        NODE_KEY_TEXT: "Selfie gesture",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/txt_list_more_settings",
    },
    "grid toggle": {
        NODE_KEY_TEXT: "Grid",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/txt_list_more_settings",
    },
    "level meter toggle": {
        NODE_KEY_TEXT: "Level meter",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/txt_list_more_settings",
    },
    # [enter][screen width/height ratio]
    "legacy radio": {
        NODE_KEY_DESCRIPTION: "Camera",  # Tomcat/V0.430
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/img_list_more_settings",
    },
    "screen ratio 1:1": {
        NODE_KEY_DESCRIPTION: "1:1",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/img_list_more_settings",
    },
    "screen ratio 4:3": {
        NODE_KEY_DESCRIPTION: "4:3",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/img_list_more_settings",
    },
    "screen ratio 16:9": {
        NODE_KEY_DESCRIPTION: "16:9",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/img_list_more_settings",
    },
    "screen ratio full": {
        NODE_KEY_DESCRIPTION: "Full",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/img_list_more_settings",
    },
    # [leave][screen width/height ratio]
    # [enter][camera timer]
    "camera timer off": {
        NODE_KEY_DESCRIPTION: "Off",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/img_list_more_settings",
    },
    "camera timer 3s": {
        NODE_KEY_DESCRIPTION: "3s",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/img_list_more_settings",
    },
    "camera timer 10s": {
        NODE_KEY_DESCRIPTION: "10s",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/img_list_more_settings",
    },
    # [leave][camera timer]
    # [enter][video dropdown settings]
    "video setting 1080p": {
        NODE_KEY_DESCRIPTION: "1080P",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/img_list_more_settings",
    },
    "video setting 4k": {
        NODE_KEY_DESCRIPTION: "4K",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/img_list_more_settings",
    },
    "video setting 30fps": {
        NODE_KEY_DESCRIPTION: "30fps",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/img_list_more_settings",
    },
    "video setting 60fps": {
        NODE_KEY_DESCRIPTION: "60fps",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/img_list_more_settings",
    },
    # [leave][video dropdown settings]
    # [leave]dropdown settings
    "settings lefttop": {
        NODE_KEY_DESCRIPTION: "Settings",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/settings_button",
    },
    "settings imageview": {
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/settings_img",
    },
    "navigate up": {
        NODE_KEY_DESCRIPTION: "Navigate up",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEBUTTON,
    },
    "shutter sound toggle": {
        NODE_KEY_TEXT: "Shutter sound",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/switch_preference_title2",
    },
    "mirror front camera toggle": {
        NODE_KEY_TEXT: "Mirror front camera",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/switch_preference_title2",
    },
    "location tag toggle": {
        NODE_KEY_TEXT: "Location tag",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/switch_preference_title2",
    },
    "haptic feedback toggle": {
        NODE_KEY_TEXT: "Haptic feedback",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/switch_preference_title3",
    },
    "brightness enhancement toggle": {
        NODE_KEY_TEXT: "Brightness enhancement",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/switch_preference_title3",
    },
    "scan qrcode toggle": {
        NODE_KEY_TEXT: "Scan QR Code",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/switch_preference_title3",
    },
    "heif format toggle": {
        NODE_KEY_TEXT: "HEIF format",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/switch_preference_title2",
    },
    "ozo audio toggle": {
        NODE_KEY_TEXT: "OZO Audio",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/switch_preference_title2",
    },
    "long press on shutter": {
        NODE_KEY_TEXT: "Long press on shutter",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: "android:id/title",
    },
    "burst shots radio button": {
        NODE_KEY_TEXT: "Burst shots",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_CHECKEDTEXTVIEW,
    },
    # [enter][feature]HDR
    "hdr auto toggle": {
        NODE_KEY_DESCRIPTION: "HDR auto",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/hdr_toggle_button",
    },
    "hdr on toggle": {
        NODE_KEY_DESCRIPTION: "HDR on",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/hdr_toggle_button",
    },
    "hdr off toggle": {
        NODE_KEY_DESCRIPTION: "HDR off",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/hdr_toggle_button",
    },
    "hdr auto": {
        NODE_KEY_DESCRIPTION: "HDR auto",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
    },
    "hdr on": {
        NODE_KEY_DESCRIPTION: "HDR on",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
    },
    "hdr off": {
        NODE_KEY_DESCRIPTION: "HDR off",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
    },
    # [leave][feature]HDR
    # [enter][feature]zoom radio
    "zoom 0.5": {
        NODE_KEY_DESCRIPTION: "Wide Angle lens",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
    },
    "zoom 1": {
        NODE_KEY_DESCRIPTION: "Normal lens",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
    },
    "zoom 2": {
        NODE_KEY_DESCRIPTION: "Zoom in to 2x",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
    },
    "zoom 3": {
        NODE_KEY_DESCRIPTION: "Zoom in to 3x",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
    },
    "zoom 4": {
        NODE_KEY_DESCRIPTION: "Zoom in to 4x",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
    },
    "zoom ix": {
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/label_text",
    },
    # [leave][feature]zoom radio
    # [enter][feature]flash
    "flash off toggle": {
        NODE_KEY_DESCRIPTION: "Flash off",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/flash_toggle_button",
    },
    "flash auto toggle": {
        NODE_KEY_DESCRIPTION: "Flash auto",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/flash_toggle_button",
    },
    "flash on toggle": {
        NODE_KEY_DESCRIPTION: "Flash on",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/flash_toggle_button",
    },
    "torch on toggle": {
        NODE_KEY_DESCRIPTION: "Torch on",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/flash_toggle_button",
    },
    "flash off": {
        NODE_KEY_DESCRIPTION: "Flash off",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
    },
    "flash auto": {
        NODE_KEY_DESCRIPTION: "Flash auto",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
    },
    "flash on": {
        NODE_KEY_DESCRIPTION: "Flash on",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
    },
    "torch on": {
        NODE_KEY_DESCRIPTION: "Torch on",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
    },
    # [leave][feature]flash
    # [enter][feature]ai portrait
    "ai portrait on": {
        NODE_KEY_DESCRIPTION: "AI Portrait on",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
        # NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/ai_portrait_button",
    },
    "ai portrait off": {
        NODE_KEY_DESCRIPTION: "AI Portrait off",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
        # NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/ai_portrait_button",
    },
    # [leave][feature]ai portrait
    # recording
    "recording time": {
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: "android.widget.TextView",
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/recording_time",
    },
    # button
    "recording pause button": {
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/recording_pause_button",
    },
    # [enter][more functions]
    "gotit button": {
        NODE_KEY_TEXT: "Got it",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_BUTTON,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/button_next",
    },
    # SpeedWarp
    "leave speedwarp": {
        NODE_KEY_TEXT: "SpeedWarp",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/mode_text_view",
    },
    "enter speedwarp": {
        NODE_KEY_TEXT: "SpeedWarp",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/item_text",
    },
    # Astrophoto
    "leave astrophoto": {
        NODE_KEY_TEXT: "Handheld Astrophoto",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/mode_text_view",
    },
    "enter astrophoto": {
        NODE_KEY_TEXT: "Handheld Astrophoto",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/item_text",
    },
    # Ultra steady video
    "leave ultrasteadyvideo": {
        NODE_KEY_TEXT: "Ultra steady video",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/mode_text_view",
    },
    "enter ultrasteadyvideo": {
        NODE_KEY_TEXT: "Ultra steady video",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/item_text",
    },
    # Dual Sight
    "leave dualsight": {
        NODE_KEY_TEXT: "Dual Sight",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/mode_text_view",
    },
    "enter dualsight": {
        NODE_KEY_TEXT: "Dual Sight",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/item_text",
    },
    # Time-lapse
    "leave timelapse": {
        NODE_KEY_TEXT: "Time-lapse",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/mode_text_view",
    },
    "enter timelapse": {
        NODE_KEY_TEXT: "Time-lapse",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/item_text",
    },
    # Flash shot
    "leave flashshot": {
        NODE_KEY_TEXT: "Flash shot",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/mode_text_view",
    },
    "enter flashshot": {
        NODE_KEY_TEXT: "Flash shot",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/item_text",
    },
    # Panorama
    "leave panorama": {
        NODE_KEY_TEXT: "Panorama",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/mode_text_view",
    },
    "enter panorama": {
        NODE_KEY_TEXT: "Panorama",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/item_text",
    },
    # Slow Motion
    "leave slowmotion": {
        NODE_KEY_TEXT: "Slow Motion",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/mode_text_view",
    },
    "enter slowmotion": {
        NODE_KEY_TEXT: "Slow Motion",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/item_text",
    },
    # Professional
    "leave professional": {
        NODE_KEY_TEXT: "Pro",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/mode_text_view",
    },
    "enter professional": {
        NODE_KEY_TEXT: "Pro",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/item_text",
    },
    # [leave][more functions]
    # [enter][album]
    "leave album": {
        NODE_KEY_DESCRIPTION: "Back to Camera",
        NODE_KEY_PACKAGENAME: GOOGLE_ANDROID_PHOTOS_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEBUTTON,
    },
    "enter album": {
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_VIEW_VIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/rounded_thumbnail_view",
    },
    "album more options": {
        NODE_KEY_DESCRIPTION: "More options",
        NODE_KEY_PACKAGENAME: GOOGLE_ANDROID_PHOTOS_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
        NODE_KEY_RESOURCEID: f"{GOOGLE_ANDROID_PHOTOS_PACKAGE_NAME}:id/photos_overflow_icon",
    },
    "album delete from device": {
        NODE_KEY_TEXT: "Delete from device",
        NODE_KEY_PACKAGENAME: GOOGLE_ANDROID_PHOTOS_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{GOOGLE_ANDROID_PHOTOS_PACKAGE_NAME}:id/photos_pager_menu_remove_from_device",
    },
    "album delete from device confirm": {
        NODE_KEY_TEXT: "Delete from device",
        NODE_KEY_PACKAGENAME: GOOGLE_ANDROID_PHOTOS_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{GOOGLE_ANDROID_PHOTOS_PACKAGE_NAME}:id/delete_confirmation_button",
    },
    "album delete all 5 photos confirm": {
        NODE_KEY_TEXT: "All 5 photos",
        NODE_KEY_PACKAGENAME: GOOGLE_ANDROID_PHOTOS_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{GOOGLE_ANDROID_PHOTOS_PACKAGE_NAME}:id/photos_burst_actionsheet_delete_all_name",
    },
    # [leave][album]
    "qrcode action text": {
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/infocard_action_text",
    },
    # [enter][beauty]
    "beauty menu button": {
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_IMAGEVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/secondary_button",
    },
    "beauty mode": {
        NODE_KEY_TEXT: "Beauty",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/beauty_title_beauty_text",
    },
    "skintone mode": {
        NODE_KEY_TEXT: "Skin tone",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/beauty_title_skin_tone_text",
    },
    "skintone natural mode": {
        NODE_KEY_TEXT: "Natural",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/beauty_skin_tone_natural_text",
    },
    "skintone bright mode": {
        NODE_KEY_TEXT: "Bright",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/beauty_skin_tone_bright_text",
    },
    "bokeh mode": {
        NODE_KEY_TEXT: "Bokeh",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/bokeh_table_text",
    },
    "beautify mode": {
        NODE_KEY_TEXT: "Beautify",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/beauty_table_text",
    },
    # [leave][beauty]
    # [enter][toast tips]
    "try portrait mode": {
        NODE_KEY_TEXT: "Try Portrait mode",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/toast_scene_action_tips_label",
    },
    "try night mode": {
        NODE_KEY_TEXT: "Try Night mode",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{HMD_CAMERA_PACKAGE_NAME}:id/toast_scene_action_tips_label",
    },
    # [leave][toast tips]
    # [enter][save network by qrcode]
    "save network menu": {
        NODE_KEY_TEXT: "Save this network?",
        NODE_KEY_PACKAGENAME: ANDROID_SETTINGS_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: f"{ANDROID_SETTINGS_PACKAGE_NAME}:id/app_title",
    },
    "save network button": {
        NODE_KEY_TEXT: "Save",
        NODE_KEY_PACKAGENAME: ANDROID_SETTINGS_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_BUTTON,
        NODE_KEY_RESOURCEID: f"{ANDROID_SETTINGS_PACKAGE_NAME}:id/save",
    },
    # [leave][save network by qrcode]
    # [enter][camera error]
    "camera error title": {
        NODE_KEY_TEXT: "Camera error",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: "android:id/alertTitle",
    },
    "camera error message": {
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_TEXTVIEW,
        NODE_KEY_RESOURCEID: "android:id/message",
    },
    "camera error dismiss button": {
        NODE_KEY_TEXT: "DISMISS",
        NODE_KEY_PACKAGENAME: HMD_CAMERA_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_BUTTON,
        NODE_KEY_RESOURCEID: "android:id/button1",
    },
    # [leave][camera error]
    # [enter][activation]
    "activation scoreseekbar": {
        NODE_KEY_PACKAGENAME: HMD_ACTIVATION_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_VIEW_VIEW,
        NODE_KEY_RESOURCEID: f"{HMD_ACTIVATION_PACKAGE_NAME}:id/scoreSeekBar",
    },
    "activation next button": {
        NODE_KEY_TEXT: "NEXT",
        NODE_KEY_PACKAGENAME: HMD_ACTIVATION_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_BUTTON,
        NODE_KEY_RESOURCEID: f"{HMD_ACTIVATION_PACKAGE_NAME}:id/positiveButton",
    },
    "activation donot again": {
        # NODE_KEY_TEXT: "Don't ask for feedback again",
        NODE_KEY_PACKAGENAME: HMD_ACTIVATION_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_CHECKBOX,
        NODE_KEY_RESOURCEID: f"{HMD_ACTIVATION_PACKAGE_NAME}:id/commentCheckBox",
    },
    "activation done button": {
        NODE_KEY_TEXT: "DONE",
        NODE_KEY_PACKAGENAME: HMD_ACTIVATION_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_BUTTON,
        NODE_KEY_RESOURCEID: f"{HMD_ACTIVATION_PACKAGE_NAME}:id/positiveButton",
    },
    "activation comment": {
        NODE_KEY_PACKAGENAME: HMD_ACTIVATION_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_EDITTEXT,
        NODE_KEY_RESOURCEID: f"{HMD_ACTIVATION_PACKAGE_NAME}:id/commentEdit",
    },
    "activation ok button": {
        NODE_KEY_TEXT: "OK",
        NODE_KEY_PACKAGENAME: HMD_ACTIVATION_PACKAGE_NAME,
        NODE_KEY_CLASSNAME: CLASS_WIDGET_BUTTON,
        NODE_KEY_RESOURCEID: f"{HMD_ACTIVATION_PACKAGE_NAME}:id/positiveButton",
    },
    # [leave][activation]
}
