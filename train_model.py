import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

# Load dataset
df = pd.read_csv("plant_data.csv")

# Features and label
X = df[["sunlight", "space", "water"]]
y = df["suitable"]

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save trained model
joblib.dump(model, "plant_model.pkl")

print("Model trained and saved as plant_model.pkl")
