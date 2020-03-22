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
    #print(type(all_vars_info)) #输出为： odict_items 。这里将其转化为 list列表
    #print(len(all_vars_info)) #长度为18
    all_vars_info = list(all_vars_info) #此时每个变量的信息为其中一个列表
    lons = f.variables['longitude'][:]#获取经度的变量值
    lats = f.variables['latitude'][:]##获取纬度的变量值
    t2m = f.variables['t2m'][:]##获取温度的变量值
    #print(t2m)
    time = f.variables['time'][:]##获取时间的变量值
    print(time)
    print(len(time))
    t2m_units = f.variables['t2m'].units ##获取经度的变量值的单位
    print(t2m_units)

    # 经纬度平均值
    lon_0 = lons.mean()
    lat_0 = lats.mean()

    m = Basemap(lat_0=lat_0, lon_0=lon_0) #定义底图
    lon, lat = np.meshgrid(lons, lats)#经纬网
    xi, yi = m(lon, lat) #X轴，Y轴

    # Plot Data
    # 数据是24小时的，这里只绘制第1小时的（t2m_0）
    t2m_0 = t2m[0:1:, ::, ::]
    #t2m_0= t2m_0-273.15 #K和摄氏度的转换K=t+273.15，T = K- 273.15
    print(t2m_0)

    t2m_1 = t2m[1:2:, ::, ::]
    print(t2m_1)
    cs = m.pcolor(xi, yi, np.squeeze(t2m_0))#插值成grid

    # Add Grid Lines
    # 绘制经纬线
    m.drawparallels(np.arange(-90., 91., 20.), labels=[1,0,0,0], fontsize=10)
    m.drawmeridians(np.arange(-180., 181., 40.), labels=[0,0,0,1], fontsize=10)

    # Add Coastlines, and Country Boundaries
    m.drawcoastlines()
    m.drawcountries()

    # Add Colorbar
    cbar = m.colorbar(cs, location='bottom', pad="10%")
    cbar.set_label(t2m_units)

    # Add Title
    plt.title('Surface 2m Air Temperature')
    plt.show()

    f.close()


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