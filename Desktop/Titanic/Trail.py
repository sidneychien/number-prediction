#  -*- coding:utf-8 -*-
# 这个程序是决策树的基本测试版

# import libraries
from sklearn import tree
import pandas as pd
import numpy as np

X_train = pd.read_csv('train',names =['Pclass'])
y_train = pd.read_csv('train',names=['Survived'])

model = tree.DecisionTreeClassifier(criterion='gini')

model.fit(X_train,y_train)
model.score(X_train,y_train)

X_test = pd.read_csv('train',names =['Pclass'])
predicted =model.predict(X_test)
print predicted