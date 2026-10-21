import joblib
import numpy as np
import warnings
from src.feature_extract import packet_to_features, features_to_list

# Hide Scikit-Learn feature name warnings for a clean terminal
warnings.filterwarnings("ignore", category=UserWarning)

try:
    model = joblib.load("models/xgb_nids_model.pkl")
    scaler = joblib.load("models/scaler.pkl")
    le_label = joblib.load("models/le_label.pkl")
except FileNotFoundError:
    print(" Model not found. Please run train_model.py first.")
    model = None


def ml_predict(packet):

    if model is None:
        return "Model Missing", 0.0

    # 1. Convert packet to features
    features_dict = packet_to_features(packet)
    vector = features_to_list(features_dict)

    # 2. Format and scale the data for the AI
    X = np.array(vector).reshape(1, -1)
    X_scaled = scaler.transform(X)

    # 3. Predict!
    prediction = model.predict(X_scaled)[0]
    label = le_label.inverse_transform([prediction])[0]

    # Get confidence score (probability)
    probabilities = model.predict_proba(X_scaled)[0]
    confidence = float(max(probabilities))

    return label, confidence