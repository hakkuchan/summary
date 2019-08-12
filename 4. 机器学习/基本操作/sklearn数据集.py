""" sklearn 数据集 """
import pandas as pd
from sklearn import datasets

''' 鸢尾花数据集 '''
iris_dataset = datasets.load_iris()
X = iris_dataset.data
Y = iris_dataset.target
iris_df = pd.DataFrame(X)
iris_df.columns = iris_dataset.feature_names
iris_df['CLASS'] = Y
iris_df

''' 波士顿房价数据集 '''
boston_dataset = datasets.load_boston()
X = boston_dataset.data
Y = boston_dataset.target
boston_df = pd.DataFrame(X)
boston_df.columns = boston_dataset.feature_names
boston_df['PRICE'] = Y
boston_df

dir(datasets)