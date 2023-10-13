import numpy as np

X = np.array([[1, 0], [0, 1], [1, 1], [0, 0]])
Y = np.array([[1], [1], [0], [0]])

W1 = np.random.randn(2, 2)
b1 = np.random.randn(2, 1)
W2 = np.random.randn(1, 2)
b2 = np.random.randn(1, 1)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Обучаем модель
for i in range(10000):
    Z1 = np.dot(W1, X.T) + b1
    A1 = sigmoid(Z1)
    Z2 = np.dot(W2, A1) + b2
    A2 = sigmoid(Z2)

    loss = np.mean((A2 - Y.T) ** 2)

    dZ2 = A2 - Y.T
    dW2 = np.dot(dZ2, A1.T) / X.shape[0]
    db2 = np.mean(dZ2, axis=1, keepdims=True)
    dZ1 = np.dot(W2.T, dZ2) * (A1 * (1 - A1))
    dW1 = np.dot(dZ1, X) / X.shape[0]
    db1 = np.mean(dZ1, axis=1, keepdims=True)

    W2 -= 0.7 * dW2
    b2 -= 0.7 * db2
    W1 -= 0.7 * dW1
    b1 -= 0.7 * db1

# Предсказываем значения
Z1 = np.dot(W1, X.T) + b1
A1 = sigmoid(Z1)
Z2 = np.dot(W2, A1) + b2
A2 = sigmoid(Z2)
predictions = np.round(A2)

print('Предсказание:', predictions)
print('Потери:', loss)