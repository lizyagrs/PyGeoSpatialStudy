# _*_ coding: cp936 _*_
# 导入geopandas
import geopandas,os
from fiona.crs import from_epsg
from geopandas import GeoSeries
import matplotlib.pyplot as plt
from shapely.geometry import Polygon

#输入矢量数据
#半径radius,单位：m
def ShpBuffer(strVectorFile,radius):
    #geopandas打开数据，如有中文，则加上中文编码方式，如有特殊字符，如网站链接等，则用utf-8方式
    vector = geopandas.read_file(strVectorFile,encoding ="GB2312")
    print('------------输入数据-----------------')
    print(vector.crs)
    #ESPG:3857:WGS 84 / Pseudo-Mercator -- Spherical Mercator, Google Maps, OpenStreetMap, Bing, ArcGIS, ESRI
    vector_CGCS=TransferProjByEPSG(vector,3857)

    print('------------转投影后数据-----------------')
    #打印输出数据属性列
    print(vector_CGCS.head())
    #打印输出数据投影信息
    print(vector_CGCS.crs)
    #获取输入矢量数据的几何信息
    g = GeoSeries(vector_CGCS['geometry'])

    print('----------------------buffer-------------------------------')
    #缓冲区分析，半径为函数的输入参数radius
    buffer=g.buffer(radius)

    #绘图的底图设置，黑色外框，白色内部
    base = vector_CGCS.plot(color='white',edgecolor='black')
    #原始输入的矢量文件制图，绿色
    buffer.plot(ax=base, color='green')
    #上述两个图层统一制图，对比缓冲前后结果
    plt.show()

    #缓冲区数据设置缓冲后的几何信息
    vector_buffer = vector_CGCS.set_geometry(buffer)

    print(vector_buffer.head())
    #给缓冲区后的矢量数据定义投影=输入矢量文件投影
    vector_buffer.crs = "EPSG:3857"
    print(vector_buffer.crs)
    #获取文件名【不包含后缀名】
    shorFilename = strVectorFile.split('.')[0]
    #输出缓冲区后矢量文件名
    bufferVectorFile= shorFilename+"_buffer_"+str(radius)+"m.shp"
    #缓冲区文件输出指定文件夹
    vector_buffer.to_file(bufferVectorFile,'ESRI Shapefile',encoding ="utf-8")

def overlay():
    polys1 = geopandas.GeoSeries([Polygon([(0,0), (2,0), (2,2), (0,2)]),
                                  Polygon([(2,2), (4,2), (4,4), (2,4)])])
    polys2 = geopandas.GeoSeries([Polygon([(1,1), (3,1), (3,3), (1,3)]),
                                  Polygon([(3,3), (5,3), (5,5), (3,5)])])
    df1 = geopandas.GeoDataFrame({'geometry': polys1, 'df1':[1,2]})
    df2 = geopandas.GeoDataFrame({'geometry': polys2, 'df2':[1,2]})

    #原始叠加显示
    ax = df1.plot(color='red')
    df2.plot(ax=ax, color='green', alpha=0.5)
    plt.title('data')

    #联合
    res_union = geopandas.overlay(df1, df2, how='union')

    ax = res_union.plot(alpha=0.5, cmap='tab10')
    df1.plot(ax=ax, facecolor='none', edgecolor='k')
    df2.plot(ax=ax, facecolor='none', edgecolor='k')
    plt.title('union')

    #相交
    res_intersection = geopandas.overlay(df1, df2, how='intersection')

    ax = res_intersection.plot(alpha=0.5, cmap='tab10')
    df1.plot(ax=ax, facecolor='none', edgecolor='k')
    df2.plot(ax=ax, facecolor='none', edgecolor='k')
    plt.title('intersection')

    #交集取反
    res_symdiff = geopandas.overlay(df1, df2, how='symmetric_difference')

    ax = res_symdiff.plot(alpha=0.5, cmap='tab10')
    df1.plot(ax=ax, facecolor='none', edgecolor='k')
    df2.plot(ax=ax, facecolor='none', edgecolor='k')
    plt.title('symmetric_difference')
    plt.show()



#叠加分析
def interacte(shp_a,shp_b):
    df_a = geopandas.read_file(shp_a,encoding ="GB2312")
    print(df_a)
    df_a=TransferProjByEPSG(df_a,4326)
    df_b = geopandas.read_file(shp_b,encoding ="utf-8")
    print(df_b)
    df_b=TransferProjByEPSG(df_b,4326)
    ax = df_a.plot(color='white', edgecolor='black')
    df_b.plot(ax=ax, color='green',edgecolor='red', alpha=0.5)
    #plt.show()
    #给数据B增加一个字段same，并定义相同的属性值dissolveall，为融合全部要素做准备
    df_b['same'] = 'dissolveall'
    #把全部要素融合
    df_b_CGCS_dissolve = df_b.dissolve(by='same')
    df_b_CGCS_dissolve.plot(alpha=0.5, cmap='tab10')
    # plt.show()
    print('------------dissolve结果---------')
    print(df_b_CGCS_dissolve.head())

    res_intersection = geopandas.overlay(df_a, df_b_CGCS_dissolve, how='intersection')
    print('-----------------------相交结果----------------------------')
    print(res_intersection)
    #先定义缓冲区数据，放在下面
    ax = df_b.plot( alpha=0.7,facecolor='lime')
    #再定义相交结果图层，放在上层
    res_intersection.plot(ax=ax,alpha=0.5, facecolor='tomato')#,marker='o', markersize=5

    plt.title('intersection')
    plt.show()

#坐标转换函数
def TransferProjByEPSG(df,code):
    result = df.to_crs(from_epsg(code))
    return result

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
    strVectorFile ="SpecialTown.shp"

    #ShpBuffer(strVectorFile,50000)
    shp_a='GIAHS_buffer_10000m.shp'
    shp_b='SpecialTown_buffer_50000m.shp'
    interacte(shp_a,shp_b)
    #overlay()