
import os
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import xgboost as xgb
import tensorflow as tf
from tensorflow.keras import layers, models

from preprocess import load_and_preprocess

def build_cnn_cbam(input_shape, num_classes):
    inputs = layers.Input(shape=input_shape)
    x = layers.Reshape((input_shape[0], 1))(inputs)
    x = layers.Conv1D(32, kernel_size=3, padding='same', activation='relu')(x)


    gap = layers.GlobalAveragePooling1D()(x)
    channel_att = layers.Dense(32 // 4, activation='relu')(gap)
    channel_att = layers.Dense(32, activation='sigmoid')(channel_att)
    channel_att = layers.Reshape((1, 32))(channel_att)
    x = layers.Multiply()([x, channel_att])

    avg_pool = layers.Lambda(lambda z: tf.reduce_mean(z, axis=-1, keepdims=True))(x)
    max_pool = layers.Lambda(lambda z: tf.reduce_max(z, axis=-1, keepdims=True))(x)
    concat = layers.Concatenate(axis=-1)([avg_pool, max_pool])
    spatial_att = layers.Conv1D(1, kernel_size=7, padding='same', activation='sigmoid')(concat)
    x = layers.Multiply()([x, spatial_att])


    x = layers.Flatten()(x)
    x = layers.Dense(64, activation='relu')(x)
    x = layers.Dropout(0.3)(x)
    outputs = layers.Dense(num_classes, activation='softmax')(x)

    model = models.Model(inputs, outputs)
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

def compare():
    print("\n" + "═"*60)
    print("🚀 STARTING NIDS MODEL COMPARISON")
    print("═"*60)

    print("📥 Loading and preprocessing data...")
    X, y = load_and_preprocess()
    num_classes = len(set(y))
    print(f"✅ Detected {num_classes} unique attack classes.")

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    X_train_cnn = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
    X_test_cnn = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

    results = []


    print("\n🌳 Training Decision Tree...")
    dt = DecisionTreeClassifier(random_state=42)
    start = time.time()
    dt.fit(X_train, y_train)
    dt_time = time.time() - start
    dt_pred = dt.predict(X_test)


    print("🌲 Training Random Forest...")
    rf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    start = time.time()
    rf.fit(X_train, y_train)
    rf_time = time.time() - start
    rf_pred = rf.predict(X_test)


    print("⚡ Training XGBoost...")
    xgb_model = xgb.XGBClassifier(n_estimators=200, max_depth=6, learning_rate=0.1, n_jobs=-1, num_class=num_classes)
    start = time.time()
    xgb_model.fit(X_train, y_train)
    xgb_time = time.time() - start
    xgb_pred = xgb_model.predict(X_test)


    print("🧠 Training CNN-CBAM (This may take a minute)...")
    cnn_model = build_cnn_cbam((X_train.shape[1], 1), num_classes)
    start = time.time()
    cnn_model.fit(X_train_cnn, y_train, epochs=5, batch_size=256, validation_split=0.1, verbose=0)
    cnn_time = time.time() - start
    cnn_pred = np.argmax(cnn_model.predict(X_test_cnn, verbose=0), axis=1)


    models_data = [
        ("Decision Tree", dt_pred, dt_time),
        ("Random Forest", rf_pred, rf_time),
        ("XGBoost", xgb_pred, xgb_time),
        ("CNN-CBAM", cnn_pred, cnn_time)
    ]

    for name, pred, train_time in models_data:
        results.append({
            "Model": name,
            "Accuracy (%)": round(accuracy_score(y_test, pred) * 100, 2),
            "Precision (%)": round(precision_score(y_test, pred, average="weighted", zero_division=0) * 100, 2),
            "Recall (%)": round(recall_score(y_test, pred, average="weighted", zero_division=0) * 100, 2),
            "F1-Score (%)": round(f1_score(y_test, pred, average="weighted", zero_division=0) * 100, 2),
            "Train Time (s)": round(train_time, 2)
        })

    df = pd.DataFrame(results)

    print("\n" + "═"*80)
    print("🏆 FINAL MODEL COMPARISON RESULTS")
    print("═"*80)

    print(tabulate(df, headers='keys', tablefmt='heavy_grid', showindex=False))
    print("═"*80 + "\n")

    os.makedirs("../models", exist_ok=True)
    df.to_csv("../models/model_comparison.csv", index=False)

    print(" Generating professional comparison chart...")

    sns.set_theme(style="darkgrid")
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#F9CA24']

    sns.barplot(ax=axes[0], x="Model", y="Accuracy (%)", data=df, palette=colors)
    axes[0].set_title("Model Accuracy Comparison", fontsize=14, fontweight='bold')
    axes[0].set_ylim(90, 100.5)
    for p in axes[0].patches:
        axes[0].annotate(f"{p.get_height():.1f}%", (p.get_x() + p.get_width() / 2., p.get_height()),
                         ha='center', va='center', xytext=(0, 9), textcoords='offset points', fontweight='bold')

    sns.barplot(ax=axes[1], x="Model", y="Train Time (s)", data=df, palette=colors)
    axes[1].set_title("Training Time Comparison (Lower is Better)", fontsize=14, fontweight='bold')
    for p in axes[1].patches:
        axes[1].annotate(f"{p.get_height():.1f}s", (p.get_x() + p.get_width() / 2., p.get_height()),
                         ha='center', va='center', xytext=(0, 9), textcoords='offset points', fontweight='bold')

    plt.suptitle("NIDS Algorithm Benchmarking", fontsize=18, fontweight='bold', y=1.05)
    plt.tight_layout()

    plt.savefig("../models/model_comparison_chart.png", dpi=300, bbox_inches='tight')
    print("✅ Saved high-res chart to models/model_comparison_chart.png")

    plt.show()

if __name__ == "__main__":
    compare()