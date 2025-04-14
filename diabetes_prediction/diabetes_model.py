# diabetes_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Load the dataset
data = pd.read_csv('data/diabetes.csv')

# Explore the data
print("First 5 rows:\n", data.head())
print("\nDataset Info:\n")
print(data.info())
print("\nMissing Values:\n", data.isnull().sum())

# Feature Selection
X = data.drop('Outcome', axis=1)  # Features
y = data['Outcome']              # Target label (0 = No diabetes, 1 = Diabetes)

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Train the model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print("\nAccuracy Score:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Predict using new data
def predict_diabetes(pregnancies, glucose, bp, skin_thickness, insulin, bmi, dpf, age):
    sample = pd.DataFrame([{
        'Pregnancies': pregnancies,
        'Glucose': glucose,
        'BloodPressure': bp,
        'SkinThickness': skin_thickness,
        'Insulin': insulin,
        'BMI': bmi,
        'DiabetesPedigreeFunction': dpf,
        'Age': age
    }])
    prediction = model.predict(sample)
    return "Diabetic" if prediction[0] == 1 else "Not Diabetic"
#Get input
if __name__ == "__main__":
    print("\n--- Diabetes Prediction ---")
    pregnancies = int(input("Enter number of pregnancies: "))
    glucose = float(input("Enter glucose level: "))
    bp = float(input("Enter diastolic blood pressure: "))
    skin_thickness = float(input("Enter skin thickness: "))
    insulin = float(input("Enter insulin level: "))
    bmi = float(input("Enter BMI: "))
    dpf = float(input("Enter Diabetes Pedigree Function: "))
    age = int(input("Enter age: "))

    result = predict_diabetes(pregnancies, glucose, bp, skin_thickness, insulin, bmi, dpf, age)
    print("\nPrediction Result:", result)