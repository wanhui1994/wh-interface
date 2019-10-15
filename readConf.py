import os
import configparser


cofigpath=os.path.join(os.path.split(os.path.realpath(__file__))[0],"config.ini")
cf = configparser.ConfigParser()
cf.read(cofigpath)
def getvalue(data,value):
    return cf.get(data, value)