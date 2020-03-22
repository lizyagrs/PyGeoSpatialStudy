# -*- coding: utf-8 -*-
import fiona
import numpy as np
import os
import rasterio
import rasterio.mask
from rasterio.plot import show
from rasterio.warp import calculate_default_transform, reproject, Resampling
from rasterio import crs

#获取栅格数据基本信息
def getTIFFInfo(imagepath):
    with rasterio.open(imagepath) as ds:

        print(f'数据格式：{ds.driver}')
        print(f'波段数目：{ds.count}')
        print(f'影像宽度：{ds.width}')
        print(f'影像高度：{ds.height}')
        print(f'地理范围：{ds.bounds}')
        print(f'反射变换参数（六参数模型）：\n {ds.transform}')
        print(f'投影定义：{ds.crs}')

        num_bands= ds.count
        print('波段数为：'+str(num_bands))
        for index in range(num_bands):
            band=index+1
            show((ds,band),cmap='Greys_r')

def showTiFF(imagepath):
    with rasterio.open(imagepath) as ds:
        show(ds)

#获取影像的指定波段
def getBand(imagepath,bandnum):
    with rasterio.open(imagepath) as ds:
        if(bandnum in len(ds.count)):
            band = ds.read(bandnum)
    return band
    ds.close()


#矢量裁剪栅格
def TIF_ClipbyShp(TIFFile,shpFile):

    #打开矢量文件，r为read,读数据
    with fiona.open(shpFile, "r") as shapefile:
        shapes = [feature["geometry"] for feature in shapefile]#获取几何信息

    #打开被裁剪栅格
    with rasterio.open(TIFFile) as src:
        showTiFF(TIFFile)
        #crop=True，按照矢量多边形的形状来裁剪影像,mask掩膜处理，这里注意，要import rasterio.mask
        out_image, out_transform = rasterio.mask.mask(src, shapes, crop=True)
        out_meta = src.meta #输入栅格的元数据赋值给输出影像
        out_meta.update({"driver": "GTiff", #数据驱动类型，GTiff
                         "height": out_image.shape[1], #行
                         "width": out_image.shape[2], #列
                         "transform": out_transform}) #反射变换参数

    shorFilename = TIFFile.split('.')[0] #获取文件名【不包含后缀名】
    out_TIFF= shorFilename+"_clip.tif" #组装输出的clip栅格文件名
    print('out_TIFF:'+out_TIFF)
    #输出裁剪后栅格，w为write，写
    with rasterio.open(out_TIFF, "w", **out_meta) as dest:
        dest.write(out_image) #输出裁剪后的影像数据
    showTiFF(out_TIFF)

#栅格转投影
#参考博客：https://blog.csdn.net/theonegis/article/details/80663218
#官方参考：https://www.osgeo.cn/rasterio/topics/reproject.html
def TransferRasterProject(src_img,epsg_name):

    dst_crs = crs.CRS.from_epsg(epsg_name) #目标投影
    with rasterio.open(src_img) as src_ds: #打开输入影像
        profile = src_ds.profile #获取输入影像的基本信息

        # 计算在新空间参考系下的仿射变换参数，图像行列数
        dst_transform, dst_width, dst_height = calculate_default_transform(
            src_ds.crs, dst_crs, src_ds.width, src_ds.height, *src_ds.bounds)

        # 更新数据集的元数据信息
        profile.update({
            'crs': dst_crs, #目标投影信息
            'transform': dst_transform, #仿射变换参数
            'width': dst_width, #列
            'height': dst_height, #高
            'nodata': 0 #无效值赋值为0
        })

        shorFilename = src_img.split('.')[0] #获取文件名【不包含后缀名】
        dst_img= shorFilename+"_"+epsg_name+".tif" #组装输出的clip栅格文件名
        print('dst_img:'+dst_img)

        # 重投影并输出数据
        with rasterio.open(dst_img, 'w', **profile) as dst_ds:
            band = src_ds.count+1
            for i in range(1, band): #波段从1开始计数
                src_array = src_ds.read(i) # 读取各波段数据
                dst_array = np.empty((dst_height, dst_width), dtype=profile['dtype']) #数据类型
                reproject( #重投影
                    # 源文件参数
                    source=src_array, #数据源
                    src_crs=src_ds.crs, #投影坐标系
                    src_transform=src_ds.transform, #仿射变换参数
                    # 目标文件参数
                    destination=dst_array,
                    dst_transform=dst_transform,
                    dst_crs=dst_crs,
                    # 其它配置
                    resampling=Resampling.cubic, #三次卷积重采样
                    num_threads=2)

                dst_ds.write(dst_array, i)#写数据
    showTiFF(dst_img)

#主函数
if __name__ == '__main__':
    #获取工程根目录的路径
    rootPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    #矢量数据文件路径
    ShpdataPath = os.path.abspath(rootPath + r'\ShpData')
    shpfile =ShpdataPath+'\hubu.shp'
    #栅格数据文件路径
    RdataPath = os.path.abspath(rootPath + r'\RasterData')
    #print('dataPath:'+dataPath)
    #切换目录
    os.chdir(RdataPath)
    #测试影像数据
    imagepath ='T50RKU_20200320T025541_2348.tif'

    #getTIFFInfo(imagepath)
    TIF_ClipbyShp(imagepath,shpfile)

    #TransferRasterProject(imagepath,"4326")


