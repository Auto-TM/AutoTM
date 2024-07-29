import auto_test_migrator
from constants import Gpt

if __name__ == "__main__":
    device_name = 'emulator-5554'

    source_test_code_dir_path = '../source_app_test_code/a1'

    target_package_name = "com.android.browser"
    target_launch_activity = "com.android.browser/com.android.browser.BrowserActivity"

    auto_test_migrator.migrate(source_test_code_dir_path, target_package_name, target_launch_activity, device_name)
