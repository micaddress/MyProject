# encoding='utf-8'
import os


def get_ready(base_path, backup_name_list, backup_time):
    backup_wholename_list = []

    # 判断要创建的文件夹是否已经存在
    for filename in backup_name_list:
        filename = filename + '_' + backup_time
        filepath = base_path + filename
        flag = os.path.exists(filepath)
        if not flag:
            os.mkdir(filepath)
            backup_wholename_list.append(filename)

    return base_path, backup_wholename_list











