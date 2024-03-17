from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.tree import plot_tree

iris = load_iris()
removed = range(0, 101, 50)
new_target = np.delete(iris.target, removed)
new_data = np.delete(iris.data, removed, axis=0)

clf = tree.DecisionTreeClassifier().fit(new_data, new_target)

fig = plt.figure(figsize=(15,10))
plot_tree(clf, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.show()