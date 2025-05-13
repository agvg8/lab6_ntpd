from flask import Flask, jsonify, request
from sklearn.linear_model import LinearRegression
import numpy as np

app = Flask(__name__)

# Trenowanie modelu przy starcie
X_train = np.array([[1], [2], [3], [4], [5]])
y_train = np.array([1, 3, 2, 3, 5])
model = LinearRegression()
model.fit(X_train, y_train)

@app.route("/")
def home():
    return jsonify(message="Witaj w API!")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if "values" not in data:
        return jsonify(error="Brak wymaganych danych!"), 400
    try:
        X_input = np.array(data["values"]).reshape(-1, 1)
        prediction = model.predict(X_input).tolist()
        return jsonify(prediction=prediction)
    except Exception as e:
        return jsonify(error=str(e)), 400

@app.route("/info")
def info():
    return jsonify(model="Linear Regression", features=1)

@app.route("/health")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    app.run(debug=True)