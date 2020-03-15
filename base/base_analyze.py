import os

import yaml


def analyze_file(file_name, data_key):
    with open("." + os.sep + "data" + os.sep + file_name, "r") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        # return data
        dict_data = data[data_key]
        # return (dict_data.values())
        list_data = list()
        for i in dict_data.values():
            list_data.append(i)
        return list_data
