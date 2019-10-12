import os


def ENV(keyname):
    '''获取公共变量'''
    value = os.environ.get(keyname, '')
    return value
