#coding=utf-8
import os,time,csv,sys
from os import path
import pymssql


def ENV(keyname):
    '''获取公共变量'''
    value = os.environ.get(keyname, '')
    return value

def slepp_t(t):
    time.sleep(t)

def get_csv(a,num1,num2):
    '''获取csv数据'''
    d = path.dirname(__file__)
    path1=d+"/data/"+a
    with open(path1, 'r') as csvfile:
        reader = csv.reader(csvfile)
        rows=[row for row in reader]
        return rows[num1][num2]
def mysql():
     print ()