import os,time,csv
from os import path


def ENV(keyname):
    '''获取公共变量'''
    value = os.environ.get(keyname, '')
    return value

def slepp_t(t):
    '''设置用例等待时长'''
    time.sleep(t)

def get_csv(a,num1,num2):
    d = path.dirname(__file__)
    path1=d+"/data/"+a
    with open(path1, 'r') as csvfile:
        reader = csv.reader(csvfile)
        rows=[row for row in reader]
        # print(rows)
        # print(rows[num1][num2])
        return rows[num1][num2]
