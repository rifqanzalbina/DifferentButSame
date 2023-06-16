# Import Library
import numpy as np

# === Codes ===
class LinearRegression:
    def __init__(self):
        self.weights = None
        self.bias = None
    
    def fit(self, X, y):
        X = np.concatenate((np.ones((X.shape[0], 1)), X), axis=1)        
        self.weights = np.linalg.pinv(X.T.dot(X)).dot(X.T).dot(y)
        self.bias = self.weights[0]
        self.weights = self.weights[1:]
    
    def predict(self, X):
        X = np.concatenate((np.ones((X.shape[0], 1)), X), axis=1)
        y_pred = X.dot(np.concatenate(([self.bias], self.weights)))
        return y_pred

X = np.array([[1, 2], [2, 4], [3, 6], [4, 8]])
y = np.array([2, 4, 6, 8])

regressor = LinearRegression()

regressor.fit(X, y)


X_test = np.array([[5, 10], [6, 12]])
y_pred = regressor.predict(X_test)

print("Prediction Result", y_pred)
# === EndCodes ===