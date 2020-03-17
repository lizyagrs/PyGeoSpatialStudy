import numpy as np
import matplotlib.pyplot as plt
import netCDF4 as nc
import os
from mpl_toolkits.basemap import Basemap

def getNetCDFData(filename):
    f = nc.Dataset(filename)
    all_vars = f.variables.keys() #获取所有变量名称
    print(all_vars) #长度为18

    all_vars_info = f.variables.items() #获取所有变量信息

    print(type(all_vars_info)) #输出为： odict_items 。这里将其转化为 list列表

    print(len(all_vars_info)) #长度为18

    all_vars_info = list(all_vars_info) #此时每个变量的信息为其中一个列表

#主函数
if __name__ == '__main__':

    #获取工程根目录的路径
    rootPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    #print('rootPath:'+rootPath)
    #数据文件路径
    dataPath = os.path.abspath(rootPath + r'\RasterData')
    #print('dataPath:'+dataPath)
    #切换目录
    os.chdir(dataPath)

    #SHP文件路径
    filename ="201908ECMWF_TPE.nc"
    getNetCDFData(filename)