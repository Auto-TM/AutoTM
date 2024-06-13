import auto_test_migrator
from auto_test_migrator import Gpt

if __name__ == "__main__":
    source_test_code_dir_path = '../source_app_test_code/shopping_list'

    target_package_name = "pfl.s.o.pfls"
    target_launch_activity = "pfl.s.o.pfls/.ui.main.MainActivity"

    openai_api_config = Gpt("sk-UDfiw8YTTN0IzxUsB79931F1228434eB545DaA7C027079e", "gpt-4")

    auto_test_migrator.migrate(source_test_code_dir_path, target_package_name, target_launch_activity, openai_api_config)
