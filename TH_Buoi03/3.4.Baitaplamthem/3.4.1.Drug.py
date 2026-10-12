'''
Số phần tử (mẫu): 200 dòng (bệnh nhân).
Số thuộc tính: 6 cột tổng cộng, trong đó có 5 thuộc tính đầu vào
và 1 cột nhãn mục tiêu (target):
1. Age: Tuổi của bệnh nhân (kiểu số nguyên)
2. Sex: Giới tính (M/F)
3. BP: Huyết áp (HIGH, NORMAL, LOW)
4. Cholesterol: Nồng độ cholesterol (HIGH, NORMAL)
5. Na_to_K: Tỷ lệ Natri và Kali trong máu (kiểu số thực)
Nhãn (Target): Cột Drug (loại thuốc được chỉ định cho bệnh nhân),
gồm 5 nhãn phân loại: DrugY, drugA, drugB, drugC và drugX.
'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

data = pd.read_csv('3.4.Baitaplamthem/drug200.csv')
print(data.head())

# xác định các đặc trưng
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# mã hóa dữ liệu dạng chữ
X = pd.get_dummies(X)

le = LabelEncoder()
y_encoded = le.fit_transform(y)

# chia tập dữ liệu và xây dựng mô hình
results = []

for test_size in [0.4, 0.2]:
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded,
        test_size=test_size,
        random_state=42,
        stratify=y_encoded
    )

    print(f'\nTỷ lệ Train/Test: {int((1-test_size)*100)}/{int(test_size*100)}')

    for min_samples_leaf in [5, 10, 15, 20]:
        # xây dựng mô hình cây quyết định
        classifier = DecisionTreeClassifier(
            criterion='gini',
            min_samples_leaf=min_samples_leaf,
            random_state=42
        )

        classifier.fit(X_train, y_train)

        # dự đoán
        y_pred = classifier.predict(X_test)

        # đánh giá mô hình
        accuracy = accuracy_score(y_test, y_pred)

        print(f'\nmin_samples_leaf = {min_samples_leaf}')
        print(f'Accuracy: {accuracy:.4f}')

        print('Classification Report:')
        print(classification_report(
            y_test, y_pred,
            labels=range(len(le.classes_)),
            target_names=le.classes_,
            zero_division=0
        ))

        print('Confusion Matrix:')
        print(confusion_matrix(
            y_test, y_pred,
            labels=range(len(le.classes_))
        ))

        results.append({
            'Train/Test': f'{int((1-test_size)*100)}/{int(test_size*100)}',
            'min_samples_leaf': min_samples_leaf,
            'Accuracy': accuracy,
            'Model': classifier
        })

# tổng hợp kết quả
results_df = pd.DataFrame([
    {
        'Train/Test': r['Train/Test'],
        'min_samples_leaf': r['min_samples_leaf'],
        'Accuracy': r['Accuracy']
    }
    for r in results
])

print('\nBẢNG SO SÁNH KẾT QUẢ:')
print(results_df.to_string(index=False))

# tìm cấu hình có độ chính xác cao nhất
best_result = max(results, key=lambda r: r['Accuracy'])

print('\nCẤU HÌNH TỐT NHẤT:')
print(f"Train/Test: {best_result['Train/Test']}")
print(f"min_samples_leaf: {best_result['min_samples_leaf']}")
print(f"Accuracy: {best_result['Accuracy']:.4f}")

# vẽ cây quyết định của mô hình tốt nhất
plt.figure(figsize=(18, 10))
plot_tree(
    best_result['Model'],
    feature_names=X.columns,
    class_names=le.classes_,
    filled=True,
    rounded=True
)
plt.title('Cây quyết định phân loại thuốc')
plt.show()