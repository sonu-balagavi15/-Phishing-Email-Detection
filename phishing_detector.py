import joblib


# Load trained model
model = joblib.load("phishing_model.pkl")

# Load vectorizer
vectorizer = joblib.load("vectorizer.pkl")


print("=" * 50)
print("      PHISHING EMAIL DETECTION MODEL")
print("=" * 50)


while True:

    email = input("\nEnter Email Text (type exit to stop): ")

    if email.lower() == "exit":
        print("Exiting...")
        break


    # Convert text into features
    email_vector = vectorizer.transform([email])


    # Prediction
    prediction = model.predict(email_vector)


    print("\nPrediction Result:")

    if prediction[0] == 1:
        print("🚨 PHISHING EMAIL DETECTED")
    else:
        print("✅ SAFE EMAIL")