# _*_ coding: cp936 _*_
# 导入geopandas
import geopandas,os
from fiona.crs import from_epsg
from geopandas import GeoSeries
import matplotlib.pyplot as plt

#用EPSG编码转投影
def TransferProjByEPSG(strVectorFile,code):
    vector = geopandas.read_file(strVectorFile)
    result = vector.to_crs(from_epsg(code))
    print('转投影后的投影信息：'+str(result.crs))
    return result

#输出矢量文件
def OutputShp(vector,strVectorFile):

    #缓冲区文件输出指定文件夹
    vector.to_file(strVectorFile,'ESRI Shapefile',encoding ="GB2312")
    #原始输入的矢量文件制图，绿色
    vector.plot(color='green')
    #上述两个图层统一制图，对比缓冲前后结果
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
    strVectorFile ="GIAHS.shp"
    result=TransferProjByEPSG(strVectorFile,3857)
    strVectorFile_3857="GIAHS3857.shp"
    OutputShp(result,strVectorFile_3857)
    strVectorFile_4326="GIAHS4326.shp"
    result_4326=TransferProjByEPSG(strVectorFile_3857,4326)
    OutputShp(result_4326,strVectorFile_4326)
