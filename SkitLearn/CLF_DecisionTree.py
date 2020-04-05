#Classification:DecisionTree
# -*- coding: utf-8 -*-

from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import *

#决策树
def Clf_DecisionTree():
    #--------------1.加载数据---------------------
    iris = load_iris() #数据集
    data=iris.data #特征集
    target=iris.target #结果目标集
    #拆分数据集为训练集与测试集，7/3开，30%为测试数据集
    X_train, X_test, y_train, y_test = train_test_split(data,target,test_size=0.3)

    #--------------2.调用模型---------------------
    clf = tree.DecisionTreeClassifier() #定义模型
    #利用训练特征集和训练结果目标集进行模型拟合
    clf = clf.fit(X_train, y_train)

    #--------------3.交叉验证---------------------
    scores = cross_val_score(clf, X_test, y_test, cv=10,scoring='accuracy')
    print('平均scores:',scores.mean())

    #--------------4.预测---------------------
    y_pred = clf.predict(X_test)
    print('y_预测值:',y_pred)
    print('y_实际值:',y_test)

    #--------------5.混淆矩阵--------------------
    c_matrix=confusion_matrix(y_test, y_pred)
    print('confusion_matrix:\n',c_matrix)

    #--------------混淆矩阵绘图--------------------------
    import matplotlib.pyplot as plt

    disp = plot_confusion_matrix(clf, X_test, y_test)
    plt.show()

    #----------------kappa系数---------------------------
    kappa = cohen_kappa_score(y_test, y_pred)
    print('kappa:',kappa)

    #--------------6.精度报告--------------------
    c_report=classification_report(y_test, y_pred, target_names=iris.target_names)
    print('精度报告：\n',c_report)



#主函数
if __name__ == '__main__':
    Clf_DecisionTree()
