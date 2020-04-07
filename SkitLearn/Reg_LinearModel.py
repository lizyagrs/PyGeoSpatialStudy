# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import os
import pandas as pd

from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

#一元线性回归模型
#Linear Regression Example

#读取本地EXCEL或者CSV文件进行回归
def LinearModel(filename):
    # Load the filename dataset，中文编码
    db=pd.read_csv(filename,encoding ="GB2312")
    print(db.head())
    # print(db['POP'])

    # 行列转置
    db_X=db['POP'].values.reshape(-1, 1)
    #db_X = db['POP'][:, np.newaxis]
    print(db_X)

    #行列转置
    db_y=db['GDP'].values.reshape(-1, 1)
    #db_y=db['GDP'][:, np.newaxis]
    print(db_y)

    #拆分数据集为训练集与测试集，7/3开，30%为测试数据集
    X_train, X_test, y_train, y_test = train_test_split(db_X,db_y,test_size=0.3)

    #定义模型
    regr = linear_model.LinearRegression()
    #模型训练
    regr.fit(X_train, y_train)

    #用训练好的模型进行预测
    db_y_pred = regr.predict(X_test)

    #--------------------------模型交叉验证------------------------------
    #系数
    coefficients=regr.coef_
    #常数项
    intercept=regr.intercept_
    print('系数: %.2f'%coefficients)
    print('常数项: %.2f'%intercept)
    #均方根误差
    mse= mean_squared_error(y_test, db_y_pred)
    print('Mean squared error: %.2f'%mse)
    #R方，决定系数
    r2=r2_score(y_test, db_y_pred)
    print('R^2_score: %.2f'%r2)

    #-------------------------------绘图-------------------------------
    # Plot outputs
    plt.scatter(X_test, y_test,  color='green')
    plt.plot(X_test, db_y_pred, color='blue', linewidth=3)
    plt.xlabel('POP')
    plt.ylabel('GDP')
    plt.rcParams['font.sans-serif']=['Times New Roman']
    plt.show()

#Linear Regression Example
def LinearModel_coef():
    # Load the dataset
    db= datasets.load_boston()
    print("数据特征项:",db.feature_names)
    db_X=db.data
    print("X行列数:",db_X.shape)
    db_y=db.target
    print("y行列数:",db_y.shape)

    #构造pandas的Frame格式，X特征值
    boston = pd.DataFrame(db_X)
    #特征值名称【列名】
    boston.columns = db.feature_names
    #定义结果名称【列名】为Price，并且将target的值赋值给此列
    boston['Price'] = db_y
    #显示前5前数据【包括表头】
    print("boston数据预览:\n",boston.head())
    #print("数据集信息：\n",boston.info())

    #线性回归模型
    model_LR = linear_model.LinearRegression()
    #模型拟合
    model_LR.fit(db_X,db_y)
    #系数
    print("各因子系数：\n",model_LR.coef_)
    #常数项
    print("常数项：",model_LR.intercept_)
    #相关系数R^2
    print("R方：",model_LR.score(db_X,db_y))




#主函数
if __name__ == '__main__':
    #LinearModel_coef()
    #获取工程根目录的路径
    rootPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    #CSV文件路径
    CSVDataPath = os.path.abspath(rootPath + r'\CSVData')
    #切换目录
    os.chdir(CSVDataPath)
    CSVDatafile =CSVDataPath+'\GDP_Pop_2018.csv'

    LinearModel(CSVDatafile)
