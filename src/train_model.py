import pandas as pd
import joblib
import os
import xgboost as xgb
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score


COLS = ["duration","protocol_type","service","flag","src_bytes","dst_bytes","land","wrong_fragment","urgent","hot","num_failed_logins","logged_in","num_compromised","root_shell","su_attempted","num_root","num_file_creations","num_shells","num_access_files","num_outbound_cmds","is_host_login","is_guest_login","count","srv_count","serror_rate","srv_serror_rate","rerror_rate","srv_rerror_rate","same_srv_rate","diff_srv_rate","srv_diff_host_rate","dst_host_count","dst_host_srv_count","dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_same_src_port_rate","dst_host_srv_diff_host_rate","dst_host_serror_rate","dst_host_srv_serror_rate","dst_host_rerror_rate","dst_host_srv_rerror_rate","label","difficulty"]


os.makedirs("models", exist_ok=True)

print(" Loading dataset...")
df = pd.read_csv("data/KDDTrain+.txt", names=COLS).drop("difficulty", axis=1)


for col in ["protocol_type", "service", "flag"]:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    joblib.dump(le, f"models/le_{col}.pkl")

le_label = LabelEncoder()
df["label"] = le_label.fit_transform(df["label"])
joblib.dump(le_label, "models/le_label.pkl")


X = df.drop("label", axis=1)
y = df["label"]


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
joblib.dump(scaler, "models/scaler.pkl")


X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)


print("\n Training Random Forest...")
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)
rf_acc = accuracy_score(y_test, rf_pred)
print(f" Random Forest Accuracy: {rf_acc * 100:.2f}%")

print("\n Training XGBoost...")
xgb_model = xgb.XGBClassifier(n_estimators=200, max_depth=6, learning_rate=0.1, objective="multi:softmax")
xgb_model.fit(X_train, y_train)
xgb_pred = xgb_model.predict(X_test)
xgb_acc = accuracy_score(y_test, xgb_pred)
print(f" XGBoost Accuracy: {xgb_acc * 100:.2f}%")

# Save the XGBoost model
joblib.dump(xgb_model, "models/xgb_nids_model.pkl")
print("\n XGBoost model successfully saved to models/xgb_nids_model.pkl")