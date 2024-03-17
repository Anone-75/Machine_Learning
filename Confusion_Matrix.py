from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming 'true_labels' are the true labels and 'predicted_labels' are the predicted labels
true_labels = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
predicted_labels = [0, 1, 0, 1, 0, 1, 0, 1, 0, 0]

# Compute confusion matrix
cm = confusion_matrix(true_labels, predicted_labels)

# Plot confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap="Blues")
plt.xlabel('Predicted'), plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
