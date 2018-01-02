#  -*- coding:utf-8 -*-
# 这个程序是决策树的基本测试版

# import libraries
from sklearn import tree
import pandas as pd
import numpy as np

data = pd.read_csv('train.csv')
X_train = data.loc[:,'Pclass']
y_train = data.loc[:,'Survived']
print X_train
# print X_train.isnull(), \
    #y_train.isnull() # think about that how to print number of null values(1）

model = tree.DecisionTreeClassifier(criterion='gini')

model.fit([X_train],)
# model.score(X_train,y_train)

# X_test = data.loc[:,'Pclass']
# predicted =model.predict([X_test])
# print predicted