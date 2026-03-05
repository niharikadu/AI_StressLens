from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib

app = Flask(__name__)
CORS(app)

# Load model and vectorizer
model = joblib.load("model.pkl")
tfidf = joblib.load("tfidf.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    text = data["text"]

    # Transform text using TF-IDF
    vector = tfidf.transform([text])

    # Predict
    prediction = model.predict(vector)[0]

    labels = ["Low", "Moderate", "High"]

    result = labels[prediction]

    return jsonify({
        "anxiety_level": result
    })


if __name__ == "__main__":
    app.run(debug=True)