# _*_ coding: cp936 _*_
import numpy as np
import os
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

def shpmap(data):
    with open('CN-border-La.dat') as src:
        context = src.read()
    blocks = [cnt for cnt in context.split('>') if len(cnt) > 0]
    borders = [np.fromstring(block, dtype=float, sep=' ') for block in blocks]

    # Set figure size
    fig = plt.figure(figsize=[10, 8])
    # Set projection and plot the main figure
    ax = plt.axes(projection=ccrs.LambertConformal(central_latitude=90,
                                                   central_longitude=105))
    # Add ocean, land, rivers and lakes
    ax.add_feature(cfeature.OCEAN.with_scale('50m'))
    ax.add_feature(cfeature.LAND.with_scale('50m'))
    ax.add_feature(cfeature.RIVERS.with_scale('50m'))
    ax.add_feature(cfeature.LAKES.with_scale('50m'))
    # Plot border lines
    for line in borders:
        ax.plot(line[0::2], line[1::2], '-', lw=1, color='k',
                transform=ccrs.Geodetic())
    # Plot gridlines
    ax.gridlines(linestyle='--')
    # Set figure extent
    ax.set_extent([80, 130, 13, 55])

    # Plot South China Sea as a subfigure
    sub_ax = fig.add_axes([0.741, 0.11, 0.14, 0.155],
                          projection=ccrs.LambertConformal(central_latitude=90,
                                                           central_longitude=115))
    # Add ocean, land, rivers and lakes
    sub_ax.add_feature(cfeature.OCEAN.with_scale('50m'))
    sub_ax.add_feature(cfeature.LAND.with_scale('50m'))
    sub_ax.add_feature(cfeature.RIVERS.with_scale('50m'))
    sub_ax.add_feature(cfeature.LAKES.with_scale('50m'))
    # Plot border lines
    for line in borders:
        sub_ax.plot(line[0::2], line[1::2], '-', lw=1, color='k',
                    transform=ccrs.Geodetic())
    # Set figure extent
    sub_ax.set_extent([105, 125, 0, 25])
    # Show figure
    plt.show()

#主函数
if __name__ == '__main__':

    #获取工程根目录的路径
    rootPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    #print('rootPath:'+rootPath)
    #数据文件路径
    dataPath = os.path.abspath(rootPath + r'\ShpData')
    #print('dataPath:'+dataPath)
    #切换目录
    os.chdir(dataPath)
    #指定数据文件
    data ="CN-border-La.dat"
    shpmap(data)