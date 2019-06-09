from sklearn import datasets
from sklearn import tree
from sklearn.tree import export_graphviz
from sklearn import model_selection
import pydotplus

""" datasets for classification """
db = datasets.load_iris()
X = db.data
y = db.target

""" build models """
model = tree.DecisionTreeClassifier(
                                   criterion='gini',
                                   splitter='best',
                                   max_depth=None,
                                   min_samples_split=2,
                                   min_samples_leaf=1,
                                   min_weight_fraction_leaf=0.,
                                   max_features=None,
                                   random_state=None,
                                   max_leaf_nodes=None,
                                   min_impurity_decrease=0.,
                                   class_weight=None,
                                   presort=False
                                   )


model.fit(X,y)
dot_data = tree.export_graphviz(model, out_file=None) 
graph = pydotplus.graph_from_dot_data(dot_data) 
graph.write_png('E:\Work\Jupyter\Data\Out/DT_iris.png') 