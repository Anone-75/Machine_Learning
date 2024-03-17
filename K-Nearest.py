from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import numpy as np

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
plt.figure(figsize=(10, 6))
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap='viridis', label='Actual')
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, cmap='plasma', marker='x', label='Predicted')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.legend()
plt.title('k-Nearest Neighbour Classification of Iris Dataset')
print("Correct predictions:\n", iris.target_names[y_test[np.where(y_pred == y_test)]])
print("\nWrong predictions:\n", iris.target_names[y_test[np.where(y_pred != y_test)]])
print(classification_report(y_test, y_pred))
plt.show()