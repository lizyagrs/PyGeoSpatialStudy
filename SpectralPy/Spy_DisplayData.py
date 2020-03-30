# -*- coding: utf-8 -*-
from spectral import *
import matplotlib.pyplot as plt
import os

from spectral.io.envi import save_image

def DisplayData(imagepath):

    img = open_image(imagepath)
    data = img.load()
    print(data)

    #save_image('rgb.png', (data[29, 19, 9]), format='png')
    #view = imshow(img, (29, 19, 9))
    # data = img[0:144,0:144,29]
    # print(data)
    band29 = data.read_band(29)
    print(band29)
    #view = imshow(band120)
    plt.hist(band29)
    plt.title("band29")
    plt.show()
    gt = open_image('92AV3GT.GIS').read_band(0)
    # #view = imshow(classes=gt)
    plt.imshow(gt, cmap='Greys_r')
    plt.colorbar()
    plt.show()



#主函数
if __name__ == '__main__':

    #获取工程根目录的路径
    rootPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    RdataPath = os.path.abspath(rootPath + r'\SpectralData')
    #print('dataPath:'+dataPath)
    #切换目录
    os.chdir(RdataPath)
    #测试影像数据
    imagepath ='92AV3C.lan'

    # imagepath = r'D:\tmpdata\HubeiHpy\pinjieBIL.hdr'

    DisplayData(imagepath)