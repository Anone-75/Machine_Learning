import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree

# Load the CSV file
df = pd.read_csv("decisiontree_csv.csv")  # Replace "your_file.csv" with the path to your CSV file

# Define features (X) and target variable (y)
X = df.drop(columns=["Go"])  # Features
y = df["Go"]  # Target variable

# Convert categorical variables to dummy variables
X = pd.get_dummies(X)

# Define the decision tree model
model = DecisionTreeClassifier(random_state=42)

# Fit the model to the data
model.fit(X, y)

# Plot the decision tree
fig, ax = plt.subplots(figsize=(10, 10))
plot_tree(model, feature_names=X.columns, class_names=y.unique(), filled=True, ax=ax)
plt.show()
