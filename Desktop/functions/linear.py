# -*- coding:utf-8 -*-
"""This program implement a regression"""
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

data1 = pd.read_csv('train.csv')
data = data1.dropna()

X = data[['Age']]
y = data[['Survived']]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)



model = LinearRegression()
model.fit(X_train,y_train)
#模型拟合测试集
y_pred = model.predict(X_test)
from sklearn import metrics
# 用scikit-learn计算MSE
print "MSE:",metrics.mean_squared_error(y_test, y_pred)
# 用scikit-learn计算RMSE
print "RMSE:",np.sqrt(metrics.mean_squared_error(y_test, y_pred))
print  model.coef_,y_pred


