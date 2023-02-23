# -*- coding: utf-8 -*-
import time
import re


# 表名称
def table_name():
    date_time = time.strftime("%Y-%m-%d", time.localtime())
    data = re.split(r'-', date_time)
    name = "oil" + data[0] + data[1] + data[2]
    return name