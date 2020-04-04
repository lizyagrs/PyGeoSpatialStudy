#Classification:SVM
# -*- coding: utf-8 -*-
from sklearn.metrics import cohen_kappa_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split

#支持向量机，SVM，不同kernels的精度对比
def Clf_SVM_Kernels():
    #--------------1.加载数据---------------------
    from sklearn.datasets import load_iris
    iris = load_iris() #数据集
    data=iris.data #特征集
    target=iris.target #结果目标集

    #拆分数据集为训练集与测试集，7/3开，30%为测试数据集
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(data,target,test_size=0.3)

    print('datas are loaded and splited ……')

    #--------------2.调用模型---------------------
    from sklearn import svm
    C = 1.0  # SVM regularization parameter
    kernels = ['linear','rbf','poly']
    svm_scores=[]
    for kern in kernels:
        model=svm.SVC(C=C,kernel=kern)
        #print('model',model)
        clf = model.fit(X_train, y_train)
        scores = cross_val_score(clf, X_test, y_test, cv=10,scoring='accuracy')
        print('平均scores:',scores.mean())
        svm_scores.append(scores.mean())

    import matplotlib.pyplot as plt

    plt.plot(kernels,svm_scores)
    plt.xlabel('Kernels')
    plt.ylabel('Cross_val accuracy')
    plt.show()

#支持向量机，SVM，不同gammar的精度对比
#gamma是选择RBF函数作为kernel后，该函数自带的一个参数
def Clf_SVM_Gamma():
    #--------------1.加载数据---------------------
    from sklearn.datasets import load_iris
    iris = load_iris() #数据集
    data=iris.data #特征集
    target=iris.target #结果目标集

    #拆分数据集为训练集与测试集，7/3开，30%为测试数据集

    X_train, X_test, y_train, y_test = train_test_split(data,target,test_size=0.3)

    print('datas are loaded and splited ……')

    #--------------2.调用模型---------------------
    from sklearn import svm
    C = 1.0  # SVM regularization parameter
    #gamma是选择RBF函数作为kernel后，该函数自带的一个参数
    gammas = [0.3,0.5,0.7,0.9,1.5,3]
    svm_scores=[]
    kappas = []
    for gamma in gammas:
        #遍历不同gamma值的模型精度
        model=svm.SVC(C=C,kernel='rbf',gamma=gamma)
        #print('model',model)
        clf = model.fit(X_train, y_train)
        scores = cross_val_score(clf, X_test, y_test, cv=10,scoring='accuracy')
        print('平均scores:',scores.mean())
        svm_scores.append(scores.mean())
        y_pred = clf.predict(X_test)
        print('y_预测值:',y_pred)
        print('y_实际值:',y_test)
        #----------------kappa系数---------------------------
        kappa = cohen_kappa_score(y_test, y_pred)
        print('kappa:',kappa)
        kappas.append(kappa)

    import matplotlib.pyplot as plt

    plt.title('Result Analysis')
    plt.plot(gammas, svm_scores, marker='o',color = 'c', mfc='w',label='Cross_val accuracy')
    plt.plot(gammas, kappas, marker='*', color = 'orange',label='kappa')

    plt.legend() # 显示图例
    plt.xlabel('gammas')
    plt.ylabel('accuracy')
    plt.show()

#主函数
if __name__ == '__main__':
    Clf_SVM_Kernels()
    Clf_SVM_Gamma()
