import pandas as pd
import joblib
import os
from sklearn.preprocessing import LabelEncoder, StandardScaler

COLS = [
    "duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes",
    "land", "wrong_fragment", "urgent", "hot", "num_failed_logins", "logged_in",
    "num_compromised", "root_shell", "su_attempted", "num_root",
    "num_file_creations", "num_shells", "num_access_files", "num_outbound_cmds",
    "is_host_login", "is_guest_login", "count", "srv_count", "serror_rate",
    "srv_serror_rate", "rerror_rate", "srv_rerror_rate", "same_srv_rate",
    "diff_srv_rate", "srv_diff_host_rate", "dst_host_count",
    "dst_host_srv_count", "dst_host_same_srv_rate", "dst_host_diff_srv_rate",
    "dst_host_same_src_port_rate", "dst_host_srv_diff_host_rate",
    "dst_host_serror_rate", "dst_host_srv_serror_rate", "dst_host_rerror_rate",
    "dst_host_srv_rerror_rate", "label", "difficulty"
]

def load_and_preprocess(path="../data/KDDTrain+.txt"):
    # Note: path is '../data/...' because we are running from inside the src folder
    os.makedirs("../models", exist_ok=True)

    print("📥 Loading dataset...")
    df = pd.read_csv(path, names=COLS)
    df = df.drop("difficulty", axis=1)

    for col in ["protocol_type", "service", "flag"]:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        joblib.dump(le, f"../models/le_{col}.pkl")

    le_label = LabelEncoder()
    df["label"] = le_label.fit_transform(df["label"])
    joblib.dump(le_label, "../models/le_label.pkl")

    X = df.drop("label", axis=1)
    y = df["label"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    joblib.dump(scaler, "../models/scaler.pkl")

    return X_scaled, y