from sklearn import tree

features = [[160, 1], [180, 1], [130, 0], [150, 0]]
labels = [0, 0, 1, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print(clf.predict([[150, 1]]))