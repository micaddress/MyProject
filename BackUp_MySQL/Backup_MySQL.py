# encoding='utf-8'
#########################################################
#将根目录加入sys.path中,解决命令行找不到包的问题
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
#########################################################
import datetime
import os
import sys
sys.path.extend(['D:\\workspace\\MyProject\\BackUp_MySQL\\delete_Old_Backup'])
import BackUp_MySQL.delete_Old_Backup as dob
import BackUp_MySQL.create_New_Backup as createBK
import BackUp_MySQL.start_Backup as start_backup


def get_backup_mysql():
    # 备份路径
    base_path = 'd:' + os.path.sep + 'Mysqlbackup' + os.path.sep
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    # 获取当前时间
    backup_time = datetime.datetime.now().strftime("_%Y-%m-%d_%H-%M-%S")
    # 需要备份的库名
    backup_databasename_list = [
                         'michael_gold_price'
                        , 'michael_huilv'
                        , 'michael_lianjia'
                        , 'michael_lianjia_country'
                        , 'michael_lianjia_newhouse'
                        ]
    backup_whole_databasename_list = [
                         'michael_gold_price' + backup_time
                        , 'michael_huilv' + backup_time
                        , 'michael_lianjia' + backup_time
                        , 'michael_lianjia_country' + backup_time
                        , 'michael_lianjia_newhouse' + backup_time
                        ]

    # base_path, backup_wholename_list = createBK.get_ready(base_path, backup_databasename_list, backup_time)

    start_backup.start_backup(base_path, backup_databasename_list, backup_time)

    dob.delete_all_old_backup(base_path, backup_whole_databasename_list)
    dob.delete_all_old_backup(base_path, backup_whole_databasename_list)


if __name__ == '__main__':
    get_backup_mysql()
    #start_time = '01:07:00'
    #print(datetime.datetime.now().strftime("%H:%M:%S") +'重新获取数据倒计时...')
    #while True:
        #if start_time == (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").split(' ')[-1]):
            #get_backup_mysql()



