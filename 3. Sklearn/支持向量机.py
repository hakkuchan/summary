import numpy as np
import pandas as pd
from sklearn import svm
from sklearn import model_selection

db = pd.read_csv('E:\Work\Jupyter\Data\char_data.csv').values
X = db[:, 1:11]
y = db[:, 11].astype('int')

model = svm.SVC(C=1.0,
                kernel='linear',
                degree=3,
                gamma='auto',
                coef0=0.0,
                shrinking=True,
                probability=False,
                tol=0.001,
                cache_size=200,
                class_weight=None,
                verbose=False,
                max_iter=-1,
                decision_function_shape='ovr',
                random_state=None)

results = []
kfold = model_selection.KFold(n_splits=10, random_state=1)
for train, test in kfold.split(X):
    X_train, X_test = X[train], X[test]
    y_train, y_test = y[train], y[test]
    model.fit(X_train, y_train)
    results.append(model.score(X_test, y_test))
results = np.array(results)
print('Accuracy (10 Fold): {:.4f} ± {:.4f}'.format(results.mean(),
                                                   results.std()))