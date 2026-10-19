import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import KFold
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Load dữ liệu Iris
data = load_iris()
X, y = data.data, data.target

# KFold (5 fold)
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# Model Naive Bayes
model = GaussianNB()

accuracies = []

# Thực hiện chia K-Fold thủ công để in từng fold
for fold, (train_idx, test_idx) in enumerate(kf.split(X), 1):
    X_train, X_test = X[train_idx], X[test_idx]
    y_train, y_test = y[train_idx], y[test_idx]
    
    print(f"=== FOLD {fold} ===")
    print(f"Vị trí dữ liệu Train (Tổng cộng {len(train_idx)} phần tử):\n", train_idx)
    print(f"Vị trí dữ liệu Test  (Tổng cộng {len(test_idx)} phần tử):\n", test_idx)
    print("-" * 50)
    
    # Train & Predict
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    # Tính accuracy
    acc = accuracy_score(y_test, y_pred)
    accuracies.append(acc)
    
    print(f"Fold {fold}: Accuracy = {acc:.4f}")

# In accuracy trung bình
print("\nAccuracy trung bình:", np.mean(accuracies))
