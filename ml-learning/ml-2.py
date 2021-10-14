import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()
test_ex = [0, 25, 50, 75, 100, 125]

# Training data
train_target = np.delete(iris.target, test_ex)
train_data = np.delete(iris.data, test_ex, axis=0)

# Testing data
test_target = iris.target[test_ex]
test_data = iris.data[test_ex]

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

print(test_target)
print(clf.predict(test_data))