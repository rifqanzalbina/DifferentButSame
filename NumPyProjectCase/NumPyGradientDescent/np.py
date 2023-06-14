# Import Library
import numpy as np

# === Codes ===
def grd_descent(X,y,learning_rate = 0.01, num_iterations = 1000):
    num_sample, num_features = X.shape
    theta = np.zeros((num_features,1))
    for _ in range(num_iterations):
        prediction = np.dot(X, theta)
        errors = prediction - y
        gradients = np.dot(X.T,errors) / num_sample
        theta -= learning_rate * gradients
    return theta

def gnerate_data(num_samples , num_features):  
    X = np.random.rand(num_samples,num_features)
    true_theta = np.random.rand(num_features,1)
    noise = np.random.randn(num_samples,1) * 0.1
    y = np.dot(X, true_theta) * noise
    return X, y

def main():
    num_samples = 100
    num_features = 3

    X, y = gnerate_data(num_samples, num_features)
    
    X = np.concatenate((np.ones((num_samples, 1)), X), axis=1)

    theta = grd_descent(X,y)

    print("Estimated Theta : ")
    print(theta)

if __name__ == "__main__":
    main()
# === EndCodes ===


