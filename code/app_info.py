import pandas as pd


class AppInfo:
    def __init__(self, classification, app_number, test_number, packagename, launch_activity, dataset_affiliation):
        self.classification = classification
        self.app_number = app_number
        self.test_number = test_number
        self.packagename = packagename
        self.launch_activity = launch_activity
        self.dataset_affiliation = dataset_affiliation


def get_apps_info(app_path):
    df = pd.read_excel(app_path)
    df = df.sort_values(by=['dataset_affiliation', 'classification', 'app_number'])
    result = []

    for dataset_affiliation, group in df.groupby('dataset_affiliation'):
        group_list = []
        for classification, sub_group in group.groupby('classification'):
            group_list.append(sub_group.to_dict(orient='records'))
        result.append(group_list)
    result[0], result[1] = result[1], result[0]

    app_info_list = []
    for classification_list in result:
        group = []
        for info in classification_list:
            sub_group = []
            for row in info:
                app_info = AppInfo(
                    classification=row['classification'],
                    app_number=row['app_number'],
                    test_number=row['test_number'],
                    packagename=row['packagename'],
                    launch_activity=row['launch_activity'],
                    dataset_affiliation=row['dataset_affiliation']
                )
                sub_group.append(app_info)
            group.append(sub_group)
        app_info_list.append(group)

    return app_info_list
