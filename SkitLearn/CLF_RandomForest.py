#Classification:CLF_RandomForest
# -*- coding: utf-8 -*-
import operator

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, cross_val_score,GridSearchCV
import numpy as np
import matplotlib.pyplot as plt


#随机森与决策树对比
def RForest_vs_DTree():
    #--------------1.加载数据---------------------
    wine = load_wine() #数据集
    data=wine.data #特征集
    target=wine.target #结果目标集
    #拆分数据集为训练集与测试集，7/3开，30%为测试数据集
    X_train, X_test, y_train, y_test = train_test_split(data,target,test_size=0.3)

    #--------------2.调用模型---------------------
    clf = DecisionTreeClassifier(random_state=0)
    rfc = RandomForestClassifier(random_state=0)

    #利用训练特征集和训练结果目标集进行模型拟合
    clf = clf.fit(X_train,y_train)
    rfc = rfc.fit(X_train,y_train)

    #--------------3.交叉验证---------------------
    score_c = cross_val_score(clf,X_test,y_test, cv=10,scoring='accuracy').mean()
    score_r = cross_val_score(rfc,X_test,y_test, cv=10,scoring='accuracy').mean()
    print("Decision Tree:{}".format(score_c)
          ,"\nRandom Forest:{}".format(score_r)
          )

#决策树个数对模型的精度影响分析
def RForest_n_estimators():
    #--------------1.加载数据---------------------
    wine = load_wine() #数据集
    data=wine.data #特征集
    target=wine.target #结果目标集
    #拆分数据集为训练集与测试集，7/3开，30%为测试数据集
    X_train, X_test, y_train, y_test = train_test_split(data,target,test_size=0.3)


    #n_estimators = [35,50,100,150,200,500]
    rfc_scores=[]
    for i in range(50,200,10):
        #--------------2.调用模型---------------------
        rfc = RandomForestClassifier(random_state=0,n_estimators=i,n_jobs=2)
        #利用训练特征集和训练结果目标集进行模型拟合
        rfc = rfc.fit(X_train,y_train)
        #--------------3.交叉验证---------------------
        score_r = cross_val_score(rfc,X_test,y_test, cv=10,scoring='accuracy').mean()
        print("决策树个数为【%s】 颗"%(i))
        print("Random Forest:{}".format(score_r))
        rfc_scores.append(score_r)

    plt.title('Random Forest Accuracy Analysis')
    plt.plot(range(50,200,10), rfc_scores, marker='o',color = 'c', mfc='w',label='Cross_val accuracy')
    plt.legend() # 显示图例
    plt.xlabel('n_estimators')
    plt.ylabel('accuracy')
    plt.show()

def RForest_max_depth():
    #--------------1.加载数据---------------------
    wine = load_wine() #数据集
    data=wine.data #特征集
    target=wine.target #结果目标集

    #调整max_depth
    param_grid = {'max_depth':np.arange(1, 20, 1)}

    rfc = RandomForestClassifier(n_estimators=160
                                 ,random_state=90
                                 )
    GS = GridSearchCV(rfc,param_grid,cv=10)
    GS.fit(data,target)
    print('best_params:',GS.best_params_)
    print('best_score:',GS.best_score_)

def RForest_max_features():
    #--------------1.加载数据---------------------
    wine = load_wine() #数据集
    data=wine.data #特征集
    target=wine.target #结果目标集
    n_samples,n_features=data.shape
    print("共有", n_samples, "个样本, 每个样本有", n_features, "个特征")
    #调整max_features
    param_grid = {'max_features':np.arange(1,n_features,1)}

    rfc = RandomForestClassifier(n_estimators=160
                                 ,random_state=90
                                 )
    GS = GridSearchCV(rfc,param_grid,cv=10)
    GS.fit(data,target)
    print('best_params:',GS.best_params_)
    print('best_score:',GS.best_score_)


def RForest_min_samples_leaf():
    #--------------1.加载数据---------------------
    wine = load_wine() #数据集
    data=wine.data #特征集
    target=wine.target #结果目标集
    n_samples,n_features=data.shape
    print("共有", n_samples, "个样本, 每个样本有", n_features, "个特征")

    #调整min_samples_leaf
    param_grid={'min_samples_leaf':np.arange(1, 1+10, 1)}

    rfc = RandomForestClassifier(n_estimators=160
                                 ,random_state=90
                                 )
    GS = GridSearchCV(rfc,param_grid,cv=10)
    GS.fit(data,target)
    print('best_params:',GS.best_params_)
    print('best_score:',GS.best_score_)

def RForest_min_samples_split():
    #--------------1.加载数据---------------------
    wine = load_wine() #数据集
    data=wine.data #特征集
    target=wine.target #结果目标集
    n_samples,n_features=data.shape
    print("共有", n_samples, "个样本, 每个样本有", n_features, "个特征")

    #调整min_samples_split
    param_grid={'min_samples_split':np.arange(2, 2+20, 1)}

    rfc = RandomForestClassifier(n_estimators=160
                                 ,random_state=90
                                 )
    GS = GridSearchCV(rfc,param_grid,cv=10)
    GS.fit(data,target)
    print('best_params:',GS.best_params_)
    print('best_score:',GS.best_score_)


def RForest_criterion():
    #--------------1.加载数据---------------------
    wine = load_wine() #数据集
    data=wine.data #特征集
    target=wine.target #结果目标集
    n_samples,n_features=data.shape
    print("共有", n_samples, "个样本, 每个样本有", n_features, "个特征")

    #调整criterion
    param_grid = {'criterion':['gini', 'entropy']}

    rfc = RandomForestClassifier(n_estimators=160
                                 ,random_state=90
                                 )
    GS = GridSearchCV(rfc,param_grid,cv=10)
    GS.fit(data,target)
    print('best_params:',GS.best_params_)
    print('best_score:',GS.best_score_)


def RForest_Score():
    #--------------1.加载数据---------------------
    wine = load_wine() #数据集
    data=wine.data #特征集
    target=wine.target #结果目标集
    n_samples,n_features=data.shape
    print("共有", n_samples, "个样本, 每个样本有", n_features, "个特征")

    rfc = RandomForestClassifier(n_estimators=160
                                 ,random_state=90
                                 )
    score = cross_val_score(rfc,data,target,cv=10).mean()
    print('score:',score)

def RF_Feature_Importances():
    #--------------1.加载数据---------------------
    wine = load_wine() #数据集
    data=wine.data #特征集
    target=wine.target #结果目标集
    n_samples,n_features=data.shape
    print("共有", n_samples, "个样本, 每个样本有", n_features, "个特征")

    rfc = RandomForestClassifier(n_estimators=160
                                 ,random_state=90
                                 )
    rfc.fit(data,target)

    features_names = wine['feature_names']
    feature_importances = rfc.feature_importances_
    print('features_names:',features_names)
    print('feature_importances:',feature_importances) #display importance of each variables

    plt.figure(figsize=(12,4))
    plt.barh(features_names, feature_importances, align =  'center')
    # plt.yticks(rotation=60) #坐标轴名称显示旋转角度
    plt.title('Feature Importances')
    plt.ylabel('feature_names')
    plt.xlabel('Importances (% )')
    plt.show()

    plt.figure(figsize=(12,8))
    plt.bar(features_names, feature_importances, align = 'center',width=0.2)
    plt.xticks(rotation=15) #坐标轴名称显示旋转角度
    plt.title('feature_names')
    plt.ylabel('Feature Importances')
    plt.xlabel('Importances (% )')
    plt.show()


    #重要性排序
    print(sorted(zip(wine['feature_names'], map(lambda x: round(x, 4),
                                                rfc.feature_importances_)),
                 key=operator.itemgetter(1), reverse=True))


#主函数
if __name__ == '__main__':
    #RForest_vs_DTree()
    #RForest_n_estimators()
    #RForest_max_depth()
    #RForest_max_features()
    #RForest_min_samples_leaf()
    #RForest_min_samples_split()
    #RForest_criterion()
    #RForest_Score()
    RF_Feature_Importances()