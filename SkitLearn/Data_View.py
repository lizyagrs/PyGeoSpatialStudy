# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from sklearn import datasets
import seaborn as sns
import numpy as np
import pandas as pd


#BostonData_view
def BostonData_view():
    # Load the dataset
    db= datasets.load_boston()
    print("数据特征项:",db.feature_names)
    db_X=db.data
    print("X行列数:",db_X.shape)
    db_y=db.target
    print("y行列数:",db_y.shape)

    #构造pandas的Frame格式，X特征值
    df = pd.DataFrame(db_X)
    #特征值名称【列名】
    df.columns = db.feature_names
    #定义结果名称【列名】为Price，并且将target的值赋值给此列
    df['Price'] = db_y
    #显示前5前数据【包括表头】
    print("boston数据预览:\n",df.head())

    #制作组图，不同特征属性的散点图
    sns.set(style='whitegrid', context='notebook')
    cols = ['LSTAT', 'INDUS', 'NOX', 'RM', 'Price']
    sns.pairplot(df[cols], height=2)
    plt.show()

    #指定特征值与目标值的相关系数矩阵
    # 可视化相关系数矩阵，理论：皮尔逊相关系数
    cm = np.corrcoef(df[cols].values.T)
    sns.set(font_scale=1.3)
    hm = sns.heatmap(cm,
                     cbar=True,
                     annot=True,
                     square=True,
                     fmt='.2f',
                     annot_kws={'size':13},
                     yticklabels=cols,
                     xticklabels=cols)
    plt.show()

    #显示矩阵热力图的一半
    mask = np.zeros_like(cm)
    print(mask)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        ax = sns.heatmap(cm, mask=mask,
                         vmax=1,
                         annot=True,
                         square=True,
                         fmt='.2f',
                         annot_kws={'size':13},
                         yticklabels=cols,
                         xticklabels=cols)
    plt.show()

    #所有特征值的相关系数，取相关系数大于0.5的制作相关系数矩阵
    # 不用修改直接运行
    corrmat = df.corr().abs() #计算连续型特征之间的相关系数
    #将于SalePrice的相关系数大于5的特征取出来，并按照SalePrice降序排列，然后取出对应的特征名，保存在列表中
    top_corr = corrmat[corrmat["Price"]>0.5].sort_values(by = ["Price"], ascending = False).index
    cm = abs(np.corrcoef(df[top_corr].values.T)) #注意这里要转置，否则变成样本之间的相关系数，而我们要计算的是特征之间的相关系数
    #f, ax = plt.subplots(figsize=(20, 9))
    sns.set(font_scale=1.3)
    hm = sns.heatmap(cm, cbar=True, annot=True,cmap='YlGnBu',
                     square=True, fmt='.2f', annot_kws={'size': 13},
                     yticklabels=top_corr.values, xticklabels=top_corr.values);
    plt.show()

#主函数
if __name__ == '__main__':

    #LinearModel(CSVDatafile)
    BostonData_view()