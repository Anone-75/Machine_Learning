import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_csv('tennis.csv')

X = data.iloc[:, :-1]
y = data.iloc[:, -1]

le_outlook = LabelEncoder()
X.Outlook = le_outlook.fit_transform(X.Outlook)
X.Temp = LabelEncoder().fit_transform(X.Temp)
X.Humidity = LabelEncoder().fit_transform(X.Humidity)
X.Windy = LabelEncoder().fit_transform(X.Windy)
y = LabelEncoder().fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

classifier = GaussianNB()
classifier.fit(X_train, y_train)

print("Accuracy is:", accuracy_score(classifier.predict(X_test), y_test))