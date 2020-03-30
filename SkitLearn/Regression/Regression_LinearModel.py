# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

#一元线性回归模型
#Linear Regression Example
def LinearModel():
    # Load the diabetes dataset
    db= datasets.load_diabetes()
    #
    db_X=db.data
    db_y=db.target
    #X_train, X_test, y_train, y_test = train_test_split(db_X,db_y,test_size=0.3)
    print(db_X[:5])
    print(db_y[:5])
    print('---------------------------------')
    #Use only one feature,:表示所有行，2表示第3列
    db_X = db_X[:, np.newaxis, 2]
    print(db_X[:5])
    # Split the data into training/testing sets
    X_train = db_X[:-20]
    X_test = db_X[-20:]

    # Split the targets into training/testing sets
    y_train = db_y[:-20]
    y_test = db_y[-20:]

    # print(X_train[:5])
    # print(y_train[:5])
    regr = linear_model.LinearRegression()
    regr.fit(X_train, y_train)
    db_y_pred = regr.predict(X_test)
    coefficients=regr.coef_
    intercept=regr.intercept_
    print('coefficients: %.2f'%coefficients)
    print('intercept: %.2f'%intercept)
    mse= mean_squared_error(y_test, db_y_pred)
    print('Mean squared error: %.2f'%mse)
    r2=r2_score(y_test, db_y_pred)
    print('r2_score: %.2f'%r2)
    # Plot outputs
    plt.scatter(X_test, y_test,  color='black')
    plt.plot(X_test, db_y_pred, color='blue', linewidth=3)
    plt.xticks(())
    plt.yticks(())

    plt.show()

#Linear Regression Example
def LinearModel1():
    # Load the dataset
    db= datasets.load_boston()
    #
    db_X=db.data

    db_y=db.target
    print(db_X[:5])
    print(db_y[:5])
    #线性回归模型
    model_LR = linear_model.LinearRegression()
    #模型拟合
    model_LR.fit(db_X,db_y)

    #系数
    print(model_LR.coef_)
    #常数项
    print(model_LR.intercept_)
    #相关系数R^2
    print(model_LR.score(db_X,db_y))



#主函数
if __name__ == '__main__':
    #获取工程根目录的路径
    #LinearModel()
    LinearModel1()