from osgeo import gdal
import os
import numpy as np
import pandas as pd

#读图像文件函数
#输入参数：文件名
#返回参数im_data
def read_img(filename):
    #打开文件
    dataset=gdal.Open(filename)
    #栅格矩阵的列数
    im_width = dataset.RasterXSize
    print('-------栅格矩阵的列数---------')
    print (im_width)
    #栅格矩阵的行数
    im_height = dataset.RasterYSize
    print('-------栅格矩阵的行数---------')
    print (im_height)
    #地图投影信息
    im_proj = dataset.GetProjection()
    print('-------地图投影信息---------')
    print (im_proj)
    #将数据写成数组，对应栅格矩阵
    im_data = dataset.ReadAsArray(0,0,im_width,im_height)
    print('-------影像属性---波段数，行数，列数------')
    print (im_data.shape)
    print('-------栅格矩阵信息---------')
    print (im_data)
    #获取波段数量
    num_bands= dataset.ReadAsArray().shape[0]
    print('波段数为：'+str(num_bands))
    for index in range(num_bands):
        print('第'+str(index+1)+'波段')
        #获取各波段数据，索引是从0开始，0-3，而波段是从1开始，1-4，因此需要给index+1，否则GetRasterBand(0)会出错
        band = dataset.GetRasterBand(index+1)
        #转数组
        band_data=band.ReadAsArray()
        print('-------波段矩阵信息---------')
        print (band_data)
        # DataArrayToExcel(band_data,band)
    #清除数据集缓存
    del im_data
    #返回获取的参数
    return dataset

def DataArrayToExcel(Raster_Filename):

    #打开文件
    dataset=gdal.Open(Raster_Filename)
    #栅格矩阵的列数
    im_width = dataset.RasterXSize
    print('-------栅格矩阵的列数---------')
    print (im_width)
    #栅格矩阵的行数
    im_height = dataset.RasterYSize
    print('-------栅格矩阵的行数---------')
    print (im_height)
    #地图投影信息
    im_proj = dataset.GetProjection()
    print('-------地图投影信息---------')
    print (im_proj)
    #将数据写成数组，对应栅格矩阵
    im_data = dataset.ReadAsArray(0,0,im_width,im_height)
    print('-------影像属性---波段数，行数，列数------')
    print (im_data.shape)
    print('-------栅格矩阵信息---------')
    print (im_data)
    # prepare for data
    # data = np.arange(1,101).reshape((10,10))

    # change the index and column name
    # data_df.columns = ['A','B','C','D','E','F','G','H','I','J']
    # data_df.index = ['a','b','c','d','e','f','g','h','i','j']

    # create and writer pd.DataFrame to excel
    # writer = pd.ExcelWriter('Save_Excel.xlsx')

    #获取波段数量
    num_bands= dataset.ReadAsArray().shape[0]
    print('波段数为：'+str(num_bands))
    for index in range(num_bands):
        print('第'+str(index+1)+'波段')
        #获取各波段数据，索引是从0开始，0-3，而波段是从1开始，1-4，因此需要给index+1，否则GetRasterBand(0)会出错
        band = dataset.GetRasterBand(index+1)
        #转数组
        band_data=band.ReadAsArray()
        print('-------波段矩阵信息---------')
        print (band_data)
        data_df = pd.DataFrame(band_data)
        writer = pd.ExcelWriter('Band'+str(index+1)+'.xlsx')
        data_df.to_excel(writer,index=False,header=False)
        writer.save()
        print('第'+str(index+1)+'波段---输出Excel--OK')
#读图像文件
def read_tif(filename):
    dataset=gdal.Open(filename) #打开文件
    im_width = dataset.RasterXSize #栅格矩阵的列数
    im_height = dataset.RasterYSize #栅格矩阵的行数
    im_geotrans = dataset.GetGeoTransform() #仿射矩阵
    im_proj = dataset.GetProjection() #地图投影信息
    im_data = dataset.ReadAsArray(0,0,im_width,im_height) #将数据写成数组，对应栅格矩阵
    del dataset #关闭对象，文件dataset
    return im_proj,im_geotrans,im_data,im_width,im_height

#其他格式转tif
#支持的影像格式可参考：https://blog.csdn.net/theonegis/article/details/80358983
def transfertype(input,output,imagetype):
    ds = gdal.Open(input)
    ds = gdal.Translate(output, ds, format=imagetype)
    print('ok')
    ds = None

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
    #读数据并获取影像信息
    Raster_Filename='S2_20190727San.tif'
    # data = read_img(Raster_Filename)
    DataArrayToExcel(Raster_Filename)
    # input=r'D:\tmpdata\RS\S2A_MSIL1C20200320_T50RKU\GRANULE\L1C_T50RKU_A024768_20200320T030130\IMG_DATA\T50RKU_20200320T025541_B10.jp2'
    # output=r'D:\tmpdata\RS\S2A_MSIL1C20200320_T50RKU\GRANULE\L1C_T50RKU_A024768_20200320T030130\IMG_DATA\T50RKU_20200320T025541_B10.tif'
    # imagetype = 'GTiff'
    # transfertype(input,output,imagetype)
