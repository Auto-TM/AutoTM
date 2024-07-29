import auto_test_migrator
import text_processor
import os
from app_info import get_apps_info
from auto_test_migrator import logger, get_test_case_files

if __name__ == "__main__":
    device_name = 'emulator-5554'

    app_info_list = get_apps_info('../dataset/app_info.xlsx')

    for app_dataset_affiliation_list in app_info_list:
        # atm/craft droid
        for app_classification_list in app_dataset_affiliation_list:
            # app_classification_list, such as a1 (five apps: a11, a12, a13, a14, a15)
            source_app_info = app_classification_list[0]

            if source_app_info.dataset_affiliation == "craftdroid":
                classification = source_app_info.classification.split('-')[0]
                # such as:b1x
                function_prefix = classification.replace("a", "b")
                for test_number_seq in range(int(source_app_info.test_number)):
                    function_suffix = test_number_seq + 1
                    function_id = function_prefix + str(function_suffix)
                    source_test_case_dir_path = ("../dataset/" + source_app_info.dataset_affiliation + "/"
                                                 + classification + "/" + function_id + "/base")

                    source_test_case_paths = get_test_case_files(source_test_case_dir_path)
                    for source_test_case_path in source_test_case_paths:
                        # a11.json a12.json a13.json a14.json a15.json
                        source_test_code_file_name = os.path.splitext(os.path.basename(source_test_case_path))[0]
                        for target_app_info in app_classification_list:
                            if source_test_code_file_name == target_app_info.app_number:
                                continue
                            logger.info("-----------")
                            logger.info("beginning to migrate, source test: {}, target test: {}, function: {}, "
                                        .format(source_test_code_file_name, target_app_info.app_number, function_id))
                            logger.info("-----------")

                            # a11_b11_a12_AutoTM_Success.md

                            markdown_file_path = ("../dataset/result/" + source_app_info.dataset_affiliation
                                                  + "/" + source_app_info.classification
                                                  + "/" + source_test_code_file_name + " to " + target_app_info.app_number
                                                  + "/" + source_test_code_file_name
                                                  + "_" + function_id
                                                  + "_" + target_app_info.app_number
                                                  + "_AutoTM.md")
                            if os.path.exists(markdown_file_path):
                                os.remove(markdown_file_path)
                            else:
                                os.makedirs(os.path.dirname(markdown_file_path), exist_ok=True)
                            markdown_file = open(markdown_file_path, "a")
                            logger.info("workflow markdown file path: " + markdown_file_path)
                            text_processor.generate_markdown_title(markdown_file, source_test_code_file_name
                                                                   + "'s " + function_id
                                                                   + " to " + target_app_info.app_number)
                            auto_test_migrator.migrate(source_test_case_path, markdown_file, target_app_info.packagename,
                                                       target_app_info.launch_activity, device_name)
                else:
                    # atm
                    pass

    # source_test_code_dir_path = '../source_app_test_code/a1'
    #
    # target_package_name = "com.android.browser"
    # target_launch_activity = "com.android.browser/com.android.browser.BrowserActivity"
    #
    # auto_test_migrator.migrate(source_test_code_dir_path, target_package_name, target_launch_activity, device_name)
