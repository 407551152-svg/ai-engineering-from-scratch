from sklearn.datasets import make_regression, make_classification
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, accuracy_score
from sklearn.model_selection import train_test_split


def linear_regression_demo():
    print("=" * 60)
    print("LINEAR REGRESSION DEMO")
    print("=" * 60)

    X, y = make_regression(
        n_samples=100,
        n_features=1,
        noise=10,
        random_state=42,
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)

    print("模型任务：根据一个特征预测连续数值")
    print("训练样本数:", len(X_train))
    print("测试样本数:", len(X_test))
    print("模型斜率:", round(model.coef_[0], 4))
    print("模型截距:", round(model.intercept_, 4))
    print("均方误差 MSE:", round(mse, 4))
    print()

    for i in range(5):
        print(
            f"真实值: {round(y_test[i], 2):>8} | "
            f"预测值: {round(predictions[i], 2):>8}"
        )

    print()


def logistic_regression_demo():
    print("=" * 60)
    print("LOGISTIC REGRESSION DEMO")
    print("=" * 60)

    X, y = make_classification(
        n_samples=200,
        n_features=2,
        n_redundant=0,
        n_informative=2,
        n_clusters_per_class=1,
        random_state=42,
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
    )

    model = LogisticRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    probabilities = model.predict_proba(X_test)
    accuracy = accuracy_score(y_test, predictions)

    print("模型任务：根据两个特征判断类别 0 或 1")
    print("训练样本数:", len(X_train))
    print("测试样本数:", len(X_test))
    print("准确率 Accuracy:", round(accuracy, 4))
    print()

    for i in range(5):
        print(
            f"真实类别: {y_test[i]} | "
            f"预测类别: {predictions[i]} | "
            f"属于类别1的概率: {round(probabilities[i][1], 4)}"
        )

    print()


def main():
    linear_regression_demo()
    logistic_regression_demo()

    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print("线性回归：用于预测连续值，比如房价、成绩、销量。")
    print("逻辑回归：用于分类，比如是否通过、是否垃圾邮件、是否点击。")
    print("训练集：模型学习用的数据。")
    print("测试集：检查模型有没有真的学会。")
    print("评估指标：用数字判断模型效果好不好。")


if __name__ == "__main__":
    main()