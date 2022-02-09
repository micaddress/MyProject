# -- coding: utf-8 --
import os


def start_backup(base_path, backup_databasename_list, backup_time):
    for index in range(len(backup_databasename_list)):
        filepath = base_path
        backup_filename = filepath + backup_databasename_list[index] + backup_time + '.sql'
        backup_str = 'mysqldump -u%s -p%s %s > %s' % ('root',
                                                         'zh850113',
                                                         backup_databasename_list[index],
                                                         backup_filename)
        print(backup_str)
        os.system(backup_str)

        # 将 备份文件sql 压缩成7zip格式压缩包并且删掉原来的 备份文件sql
        # zipstr = '7z.exe a ' + filepath +backup_databasename_list[index]
        # os.system(zipstr)
        # os.remove(backup_filename)


