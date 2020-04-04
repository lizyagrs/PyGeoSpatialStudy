# -*- coding: utf-8 -*-
import os

import numpy as np
import pandas as pd

#方法一：默认读取第一个表单
def readExcelbyFileName(filename):
    #这个会直接默认读取到这个Excel的第一个表单
    df=pd.read_excel(filename)
    data=df.head()#默认读取前5行的数据
    print("获取到所有的值:\n{0}".format(data))#格式化输出
    #读取第1行到第4行，第1列到第22列的值，包括表头
    data=df.iloc[0:3,:]
    print("读取指定行的数据：\n{0}".format(data))#格式化输出
    return data

#方法二：通过指定表单名的方式来读取
def readExcelbyFileNameAndSheetName(filename,sheetname):
    #可以通过sheet_name来指定读取的表单
    df=pd.read_excel(filename,sheet_name=sheetname)
    print("输出列标题",df.columns.values)
    data=df.values#读取全部数据
    print("获取到所有的值:\n{0}".format(data))#格式化输出
    return data

def deleteNull(filename):
    #这个会直接默认读取到这个Excel的第一个表单
    df=pd.read_csv(filename,encoding ="GB2312")
    print('原始数据：',df.shape)
    data=df.head()#默认读取前5行的数据
    print(data)
    df.dropna()#删除空值行
    print('删除空值行后：',df.shape)

    err_line = df[df['GDP'].str.contains('&')]
    print('err_line:\n',err_line)

    df.drop(err_line.index,inplace=True) #inplace=True改变面板数据的值
    print('删除特殊字符行后：',df.shape)
    print('df:err_line\n',df.iloc[err_line.index])# 打印看第161行是否已删除

    df=df[(df['GDP'].astype(float) > 0.00)&(df['POP'].astype(float) > 0.00)]#删除GDP和POP为0的行
    print('删除GDP以及POP为0的行后：',df.shape)
    print(df[20:60])


#主函数
if __name__ == '__main__':
    #LinearModel_coef()
    #获取工程根目录的路径
    rootPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    #CSV文件路径
    CSVDataPath = os.path.abspath(rootPath + r'\CSVData')
    #切换目录
    os.chdir(CSVDataPath)
    CSVDatafile =CSVDataPath+'\GDP_Pop_2018_RawData.csv'
    deleteNull(CSVDatafile)


# #测试
# filename='ProvinceFruit_1999_2018.xlsx'
# #方法一调用
# data=readExcelbyFileName(filename)
# print('--------------计算df计算所有行的平均值--------------')
# allrowmean=data.mean(axis = 1)# 计算所有行的平均值
# print(allrowmean)
#
# #sheet名称
# sheetname = '分省年度数据'
# #读取指定文件名和sheet的数据列表
# #readExcelbyFileNameAndSheetName(filename,sheetname)