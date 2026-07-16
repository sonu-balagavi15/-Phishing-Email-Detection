import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix


# Load Dataset
data = pd.read_csv("dataset/emails.csv")

print("Dataset Loaded Successfully")


X = data["text"]
y = data["label"]


# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Text Feature Extraction
vectorizer = TfidfVectorizer()

X_train_vector = vectorizer.fit_transform(X_train)
X_test_vector = vectorizer.transform(X_test)


# Train Model
model = LogisticRegression()

model.fit(
    X_train_vector,
    y_train
)


# Prediction
prediction = model.predict(X_test_vector)


# Accuracy
accuracy = accuracy_score(
    y_test,
    prediction
)

print("\nModel Accuracy:", accuracy)


# Confusion Matrix
cm = confusion_matrix(
    y_test,
    prediction
)

print("\nConfusion Matrix:")
print(cm)


# Save Model
joblib.dump(model, "phishing_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")


# Create Confusion Matrix Image

plt.figure(figsize=(5,4))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues"
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Phishing Email Detection Confusion Matrix")

plt.savefig("confusion_matrix.png")

plt.close()


print("\nModel Saved Successfully!")
print("Confusion Matrix Image Created!")