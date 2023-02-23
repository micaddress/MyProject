# -- coding: utf-8 --
import os

command='''kill -9 $(netstat -nlp | grep :'''+str(80)+''' | awk '{print $7}' | awk -F"/" '{ print $1 }')'''
print(command)
os.system(command)





