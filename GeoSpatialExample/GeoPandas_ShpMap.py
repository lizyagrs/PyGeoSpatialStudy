#官方网站：https://geopandas.org/mapping.html
#数据结构与基本方法：https://geopandas.org/data_structures.html
#空间分析：https://geopandas.org/geometric_manipulations.html
#空间分析功能索引：https://geopandas.org/reference.html
# _*_ coding: cp936 _*_
# 导入geopandas
import geopandas,os
import matplotlib.pyplot as plt
from shapely.geometry import Point

#用来正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False# 显示负号
plt.rcParams['figure.dpi'] = 100 #分辨率

#利用geopandas打开shp数据并绘图
def ShpMapWithLenged():
    #geopandas自带数据
    world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
    cities = geopandas.read_file(geopandas.datasets.get_path('naturalearth_cities'))
    #打印输出数据属性列
    print(world.head())
    #打印输出数据投影信息
    print(world.crs)
    # Plot by GDP per capta
    world = world[(world.pop_est>0) & (world.name!="Antarctica")]
    #计算人均GDP并赋值给gdp_per_cap
    world['gdp_per_cap'] = world.gdp_md_est / world.pop_est

    # Plot population estimates with an accurate legend
    fig, ax = plt.subplots(1, 1)

    #gdp_per_cap制图，有图例，图例在图下面水平摆放
    world.plot(column='gdp_per_cap', ax=ax, legend=True,legend_kwds={'label': "GDP per capita", 'orientation': "horizontal"})
    #Population by Country
    #world.plot(column='pop_est', ax=ax, legend=True,legend_kwds={'label': "Population by Country", 'orientation': "horizontal"})

    plt.show()

def ShpTwoLayersMap():
    #geopandas自带数据
    world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
    cities = geopandas.read_file(geopandas.datasets.get_path('naturalearth_cities'))
    #设置世界地图为底图，渲染颜色为黑色边框白色
    base = world.plot(color='white', edgecolor='black')
    #城市点地图显示参数设置，加载世界地底为底图，标记点大小为5，颜色为绿色
    cities.plot(ax=base, marker='o', color='green', markersize=5)
    plt.show()

#属性分级渲染及自定义图例
def ColorAttribute(strVectorFile):
    fig, ax = plt.subplots(figsize=(12, 12))
    # # 读入中国领土面数据
    # china = geopandas.read_file('zip://china-shapefiles.zip!china-shapefiles/china.shp',
    #                             encoding='utf-8')
    # # china.crs = "EPSG:4480" #China Geodetic Coordinate System 2000
    #
    # # 由于每行数据是单独的面，因此按照其省份列OWNER融合
    # china = china.dissolve(by='OWNER').reset_index(drop=False)
    #
    # # 读入南海九段线线数据
    # nine_lines = geopandas.read_file('zip://china-shapefiles.zip!china-shapefiles/china_nine_dotted_line.shp',
    #                                  encoding='utf-8')
    # nine_lines.crs = "EPSG:4480"
    specialTown = geopandas.read_file(strVectorFile)
    # specialTown.crs = "EPSG:4480"
    # ax = china.geometry.plot(ax=ax,facecolor='white',
    #                          edgecolor='black',
    #                          #linestyle='--',
    #                          #hatch='xxxx',
    #                          alpha=0.6)
    # ax = nine_lines.geometry.plot(ax=ax,
    #                               edgecolor='black',
    #                               alpha=0.6)

    ax = specialTown.plot(ax=ax,
                          column='GDP1Y',
                          cmap='Reds',
                          # missing_kwds={
                          #     "color": "lightgrey",
                          #     "edgecolor": "black",
                          #     "hatch": "////"
                          # },
                          legend=True,#添加图例
                          scheme='NaturalBreaks',#自然断点法
                          k=5)#分5级
    handles, labels = ax.get_legend_handles_labels()
    ax.legend(loc='lower left', fontsize=10, title='GDP(100 Million CNY)',  shadow=True, borderpad=0.6)
    #这里都是英文和数字，因此用Times New Roman字体
    plt.rcParams['font.sans-serif']=['Times New Roman']
    plt.show()


#代码来源于博客:https://blog.csdn.net/fengdu78/article/details/104624007/
#数据来源于网站：https://gitee.com/zhuliupiaoxue/china-shapefiles
#免责声明：中国地图数据来源于网络，并非测绘局官方权威发布，仅用于测试，不涉及任何国界国土等争议问题
def ShpChinaFullMap():

    # 定义CRS
    # 读入中国领土面数据
    china = geopandas.read_file('zip://china-shapefiles.zip!china-shapefiles/china.shp',
                          encoding='utf-8')
    china.crs = "EPSG:4480" #China Geodetic Coordinate System 2000

    # 由于每行数据是单独的面，因此按照其省份列OWNER融合
    china = china.dissolve(by='OWNER').reset_index(drop=False)

    # 读入南海九段线线数据
    nine_lines = geopandas.read_file('zip://china-shapefiles.zip!china-shapefiles/china_nine_dotted_line.shp',
                               encoding='utf-8')
    nine_lines.crs = "EPSG:4480"
    # 初始化图床
    fig, ax = plt.subplots(figsize=(12, 8))

    ax = china.geometry.plot(ax=ax,facecolor='white',
                             edgecolor='black',
                             #linestyle='--',
                             #hatch='xxxx',
                             alpha=0.6)
    ax = nine_lines.geometry.plot(ax=ax,
                                  edgecolor='black',
                                  alpha=0.6,
                                  label='南海十段线')
    # ax = china.geometry.representative_point()\
    #     .plot(ax=ax,
    #           facecolor='black',
    #           marker='p',
    #           markersize=200,
    #           label='省级单位')
    # 单独提前设置图例标题大小
    plt.rcParams['legend.title_fontsize'] = 14

    # 设置图例标题，位置，排列方式，是否带有阴影
    ax.legend(title="图例", loc='lower left', ncol=1, shadow=True)

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
    strVectorFile ="SpecialTownList.shp"
    #获取工程根目录的路径
    # ShpMapWithLenged()
    # ShpTwoLayersMap()
    # ShpChinaFullMap()
    ColorAttribute(strVectorFile)
