#!/bin/bash

# 定义APK文件所在的目录
APK_DIR="path/autotm_apk/atm_apk"

# 遍历目录中的每个APK文件并安装
for apk in "$APK_DIR"/*.apk; do
    if [[ -f "$apk" ]]; then
        echo "Installing $apk ..."
        adb install "$apk"
        if [[ $? -eq 0 ]]; then
            echo "Successfully installed $apk"
        else
            echo "Failed to install $apk"
        fi
    fi
done

echo "All APKs have been processed."
