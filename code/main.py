import auto_test_migrator
import text_processor
import os
import sys
import migrate_subjects
import config
from app_info import get_apps_info
from auto_test_migrator import logger, get_test_case_files


def match_craftdroid_source_target_case():
    migrate_subject = "{}_{}_{}".format(source_test_code_file_name, function_id, target_app_info.app_number)
    if migrate_subject not in migrate_subjects.subjects \
            and migrate_subject not in migrate_subjects_argv:
        return
    logger.info("-----------")
    logger.info("beginning to migrate, source app: {}, target app: {}, function: {}, test case path: {}"
                .format(source_test_code_file_name, target_app_info.app_number, function_id, source_test_case_path))
    logger.info("-----------")
    # a11_b11_a12_AutoTM.md
    markdown_file_path = ("../dataset/result/" + source_app_info.dataset_affiliation
                          + "/" + source_app_info.classification
                          + "/" + source_test_code_file_name + "_" + function_id
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
    logger.info("finish migrating, source app: {}, target app: {}, function: {}, test case path: {}"
                .format(source_test_code_file_name, target_app_info.app_number, function_id, source_test_case_path))
    logger.info("---------------------finished-----------------------")


def match_atm_source_target_case():
    migrate_subject = "{}_{}_{}".format(source_test_code_file_name, function_id, target_app_info.app_number)
    if migrate_subject not in migrate_subjects.subjects \
            and migrate_subject not in migrate_subjects_argv:
        return
    logger.info("-----------")
    logger.info("beginning to migrate, source app: {}, test: {}, target app: {}, test case path: {}"
                .format(source_test_code_file_name, function_id, target_app_info.app_number, source_test_case_path))
    logger.info("-----------")
    # a11_b11_a12_AutoTM.md
    markdown_file_path = ("../dataset/result/" + source_app_info.dataset_affiliation
                          + "/" + source_app_info.classification
                          + "/" + source_test_code_file_name + "_" + function_id
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
    logger.info("finish migrating, source app: {}, test: {}, target app: {}, test case path: {}"
                .format(source_test_code_file_name, function_id, target_app_info.app_number, source_test_case_path))
    logger.info("---------------------finished-----------------------")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        # run by IDE, such as : pycharm
        device_name = config.device_name
        migrate_subjects_argv = ""
    else:
        # run by command line, first param is device_name and second is migrate subjects during this running time.
        # such as : python main.py emulator-5556  migrate_subjects_argv.txt
        device_name = sys.argv[1]
        migrate_subjects_file_path = sys.argv[2]
        with open(migrate_subjects_file_path, 'r', encoding='utf-8') as file:
            migrate_subjects_argv = file.read()

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
                    source_test_case_dir_path = ("../dataset/source_test_case/" + source_app_info.dataset_affiliation + "/"
                                                 + classification + "/" + function_id + "/base")

                    source_test_case_paths = get_test_case_files(source_test_case_dir_path)
                    for source_test_case_path in source_test_case_paths:
                        # a11.json a12.json a13.json a14.json a15.json
                        source_test_code_file_name = os.path.splitext(os.path.basename(source_test_case_path))[0]
                        for target_app_info in app_classification_list:
                            if source_test_code_file_name == target_app_info.app_number:
                                continue
                            match_craftdroid_source_target_case()
            else:
                # atm
                for source_app_info in app_classification_list:
                    source_test_case_dir_path = ("../dataset/source_test_case/" + source_app_info.dataset_affiliation + "/" + source_app_info.classification + "/"
                                                 + source_app_info.app_number )
                    source_test_case_paths = get_test_case_files(source_test_case_dir_path)
                    for source_test_case_path in source_test_case_paths:
                        # Test1.java Test2.java Test3.java ...
                        function_id = os.path.splitext(os.path.basename(source_test_case_path))[0]
                        source_test_code_file_name = source_test_case_path.split(os.sep)[-2]

                        for target_app_info in app_classification_list:
                            if source_test_code_file_name == target_app_info.app_number:
                                continue
                            match_atm_source_target_case()

