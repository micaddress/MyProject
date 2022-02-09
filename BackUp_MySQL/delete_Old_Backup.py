# encoding='utf-8'
import os


# 删除以前的备份文件
def delete_all_old_backup(base_path, backup_whole_databasename_list):
    all_path_list = os.listdir(base_path)
    for index in range(len(all_path_list)):
        a = all_path_list[index].split('.')[0]
        if a in backup_whole_databasename_list:
            continue
        path = base_path + all_path_list[index]
        delete_all_files(path)


# 删除paths路径下的所有文件
def delete_all_files(paths):
    # 删除文件
    if os.path.isfile(paths):
        os.remove(paths)
    # 删除空文件夹
    elif os.path.isdir(paths):
        if not os.listdir(paths):
            os.removedirs(paths)
        # 如果是非空文件夹则遍历自身继续查找删除文件和空文件夹
        else:
            lists = os.listdir(paths)
            for path in lists:
                p = paths + os.path.sep + path
                delete_all_files(p)


# # 删除paths路径下的所有文件
# def delete_all_files(paths):
#     # 删除文件
#     if os.path.isfile(paths):
#         os.remove(paths)
#     # 删除空文件夹
#     elif os.path.isdir(paths):
#         # 如果是非空文件夹则遍历自身继续查找删除文件和空文件夹
#         if os.listdir(paths):
#             lists = os.listdir(paths)
#             for path in lists:
#                 p = paths + os.path.sep + path
#                 delete_all_files(p)
#         os.removedirs(paths)




# 删除以前的备份文件
def delete_old_except7z_backup(base_path, backup_path_list):
    all_path_list = os.listdir(base_path)
    for path in all_path_list:
        if path in backup_path_list:
            continue
        else:
            file_path = base_path+path
            son_file_list = os.listdir(file_path)
            for son in son_file_list:
                sonend = son.split('.')[-1]
                # 文件尾缀为7z的压缩格式文件的话则不删除
                if sonend == '7z':
                    continue
                try:
                    os.remove(file_path+'/'+son)
                except:
                    os.removedirs(file_path+'/'+son)
            os.rmdir(file_path)


if __name__ == '__main__':
    delete_all_old_backup(r'D:' + os.path.sep + '1 - 副本' + os.path.sep, [])







