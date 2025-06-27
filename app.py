from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open("model/xgb_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    input_values = [float(x) for x in request.form.values()]
    input_array = np.array([input_values])
    prediction = model.predict(input_array)
    result = "Fraudulent" if prediction[0] == 1 else "Legitimate"
    return render_template("index.html", prediction_text=f"Transaction is: {result}")

if __name__ == "__main__":
    app.run(debug=True)
