import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(output):
    return output * (1 - output)


def binary_cross_entropy(y_true, y_pred):
    epsilon = 1e-8
    return -np.mean(
        y_true * np.log(y_pred + epsilon)
        + (1 - y_true) * np.log(1 - y_pred + epsilon)
    )


def main():
    X = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1],
    ])

    y = np.array([
        [0],
        [0],
        [0],
        [1],
    ])

    np.random.seed(42)

    input_size = 2
    hidden_size = 4
    output_size = 1
    learning_rate = 0.5
    epochs = 5000

    W1 = np.random.randn(input_size, hidden_size)
    b1 = np.zeros((1, hidden_size))

    W2 = np.random.randn(hidden_size, output_size)
    b2 = np.zeros((1, output_size))

    for epoch in range(epochs):
        # Forward pass
        z1 = np.dot(X, W1) + b1
        a1 = sigmoid(z1)

        z2 = np.dot(a1, W2) + b2
        y_pred = sigmoid(z2)

        loss = binary_cross_entropy(y, y_pred)

        # Backward pass
        dz2 = y_pred - y
        dW2 = np.dot(a1.T, dz2) / len(X)
        db2 = np.mean(dz2, axis=0, keepdims=True)

        da1 = np.dot(dz2, W2.T)
        dz1 = da1 * sigmoid_derivative(a1)
        dW1 = np.dot(X.T, dz1) / len(X)
        db1 = np.mean(dz1, axis=0, keepdims=True)

        # Update parameters
        W2 -= learning_rate * dW2
        b2 -= learning_rate * db2
        W1 -= learning_rate * dW1
        b1 -= learning_rate * db1

        if epoch % 500 == 0:
            print(f"Epoch {epoch:4d} | Loss: {loss:.6f}")

    print()
    print("Final predictions:")

    for input_value, prediction in zip(X, y_pred):
        label = 1 if prediction[0] >= 0.5 else 0
        print(
            f"Input: {input_value.tolist()} | "
            f"Predicted probability: {prediction[0]:.4f} | "
            f"Predicted label: {label}"
        )


if __name__ == "__main__":
    main()