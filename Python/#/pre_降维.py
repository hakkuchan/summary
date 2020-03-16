from sklearn import datasets
from sklearn import manifold
from sklearn import discriminant_analysis


""" MDS """
# Data: Iris
iris = datasets.load_iris()
X = iris.data
# MDS降维
mds = manifold.MDS(n_components=2)
Xr = mds.fit_transform(X)
print(Xr.shape)


""" Isomap """
# Data: Iris
iris = datasets.load_iris()
X = iris.data
# Isomap降维
isomap = manifold.Isomap(n_neighbors=3, n_components=2)
Xr = isomap.fit_transform(X)
print(Xr.shape)


""" LLE """
# Data: Iris
iris = datasets.load_iris()
X = iris.data
# LLE降维
lle = manifold.LocallyLinearEmbedding(n_neighbors=3, n_components=2)
Xr = lle.fit_transform(X)
print(Xr.shape)


""" LDA """
# Data: Iris
iris = datasets.load_iris()
X = iris.data
y = iris.target
# LDA降维
lda = discriminant_analysis.LinearDiscriminantAnalysis(solver='svd', n_components=2)
Xr = lda.fit_transform(X, y)
print(Xr.shape)