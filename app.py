#dependencies
from flask import Flask, jsonify
from data_fetcher import fetch_meteorology_data
from model import load_model
from alert import send_alert


app = Flask(__name__)
@app.route('/predict_flood', methods=['GET'])
def predict_flood():
    data = fetch_meteorology_data()
    model = load_model()
    prediction = model.predict(data)[0]  # Predicts flood risk
    
    if prediction == 1:
        send_alert(prediction)
    
    response = {
        "flood_risk": "High" if prediction == 1 else "Low",
        "data": data.to_dict()
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
