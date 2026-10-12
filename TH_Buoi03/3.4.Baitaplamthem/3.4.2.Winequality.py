import pandas as pd
from sklearn.model_selection import KFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.metrics import recall_score
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

#Đọc dữ liệu rượu vang trắng
data = pd.read_csv(
    '3.4.Baitaplamthem/winequality-white.csv',sep=';')
print(data.head())


#Xác định số thuộc tính và cột nhãn
print('\nSố mẫu:', data.shape[0])
print('Số thuộc tính đầu vào:', data.shape[1] - 1)
print('Cột nhãn:', data.columns[-1])
print('Các giá trị nhãn:', sorted(data['quality'].unique()))

# xác định các đặc trưng
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Chia dữ liệu bằng K-Fold với K=50
kf = KFold(n_splits=50, shuffle=True, random_state=42)

# xây dựng các mô hình
models = {
    'Decision Tree': DecisionTreeClassifier(
        criterion='entropy', random_state=42
    ),
    'KNN': make_pipeline(
        StandardScaler(),
        KNeighborsClassifier(n_neighbors=7)
    ),
    'Naive Bayes': GaussianNB()
}

# lưu kết quả
results = {name: [] for name in models}
last_results = {}

for fold, (train_index, test_index) in enumerate(kf.split(X), start=1):
    X_train, X_test = X.iloc[train_index], X.iloc[test_index]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]

    print(f'\nLần lặp {fold}')
    print('Số mẫu huấn luyện:', len(X_train))
    print('Số mẫu kiểm tra:', len(X_test))

    for name, model in models.items():
        # huấn luyện mô hình
        model.fit(X_train, y_train)

        # dự đoán
        y_pred = model.predict(X_test)

        # tính độ chính xác tổng thể
        accuracy = accuracy_score(y_test, y_pred)
        results[name].append(accuracy)

        print(f'{name} - Accuracy: {accuracy:.4f}')

        # lưu kết quả lần lặp cuối
        if fold == 50:
            last_results[name] = {
                'y_test': y_test,
                'y_pred': y_pred,
                'model': model
            }

# Đánh giá từng phân lớp ở lần lặp cuối
print('\nĐÁNH GIÁ TỪNG PHÂN LỚP Ở LẦN LẶP CUỐI')

for name, result in last_results.items():
    print(f'\nMô hình: {name}')

    print('Classification Report:')
    print(classification_report(
        result['y_test'],
        result['y_pred'],
        zero_division=0
    ))

    print('Confusion Matrix:')
    print(confusion_matrix(
        result['y_test'],
        result['y_pred'],
        labels=sorted(y.unique())
    ))

    # độ chính xác theo từng lớp (Recall)
    class_accuracy = recall_score(
        result['y_test'],
        result['y_pred'],
        labels=sorted(y.unique()),
        average=None,
        zero_division=0
    )

    print('Độ chính xác theo từng lớp (Recall):')
    for label, score in zip(sorted(y.unique()), class_accuracy):
        print(f'Quality {label}: {score:.4f}')

#Tính độ chính xác trung bình sau 50 lần lặp
print('\nBẢNG SO SÁNH ĐỘ CHÍNH XÁC TRUNG BÌNH')

for name, scores in results.items():
    print(f'{name}: {sum(scores) / len(scores):.4f}')

# in độ chính xác từng lần lặp
results_df = pd.DataFrame(results)
results_df.index = range(1, 51)
results_df.index.name = 'Lần lặp'

print('\nĐỘ CHÍNH XÁC CỦA TỪNG LẦN LẶP:')
print(results_df.to_string())

# vẽ cây quyết định của lần lặp cuối
tree_model = last_results['Decision Tree']['model']

plt.figure(figsize=(20, 10))
plot_tree(
    tree_model,
    feature_names=X.columns,
    class_names=[str(label) for label in sorted(y.unique())],
    filled=True,
    rounded=True,
    max_depth=3
)
plt.title('Cây quyết định phân loại chất lượng rượu vang trắng')
plt.show()