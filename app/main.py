import os
import logging
import joblib
import flask
import numpy as np
from werkzeug.exceptions import BadRequest

app = flask.Flask(__name__, template_folder='templates')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    model_data = joblib.load("model/car_price_model.pkl")
    logger.info("✅ Model loaded successfully.")
except Exception as e:
    logger.error(f"❌ Failed to load model: {e}")
    raise

def predict_car_price(input_data, model_data):
    """
    Predict car price based on input features.
    """
    model = model_data['model']
    scaler = model_data['scaler']
    le_dict = model_data['le_dict']
    feature_cols = model_data['feature_cols']

    processed_data = []
    for col in feature_cols:
        if col not in input_data:
            raise BadRequest(f"Missing required field: {col}")
        if col in le_dict:  # categorical
            try:
                encoded_val = le_dict[col].transform([input_data[col]])[0]
            except ValueError:
                logger.warning(f"Unseen label '{input_data[col]}' for column '{col}'. Using default=0.")
                encoded_val = 0
            processed_data.append(encoded_val)
        else:
            try:
                processed_data.append(float(input_data[col]))
            except (ValueError, TypeError):
                raise BadRequest(f"Invalid value for numerical field: {col}")

    sample = np.array(processed_data).reshape(1, -1)
    sample_scaled = scaler.transform(sample)

    pred_log_price = model.predict(sample_scaled)[0]
    return float(np.exp(pred_log_price))

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = flask.request.get_json(force=True)
        predicted_price = predict_car_price(data, model_data)
        return flask.jsonify({'price': round(predicted_price, 2)})
    except BadRequest as e:
        return flask.jsonify({"error": str(e)}), 400
    except Exception as e:
        logger.error(f"Prediction error: {e}", exc_info=True)
        return flask.jsonify({"error": "Internal Server Error"}), 500

@app.route('/health', methods=['GET'])
def health():
    return flask.jsonify({"status": "ok"}), 200

@app.route('/')
def home():
    return flask.render_template('index.html')

if __name__ == '__main__':
    
    example_car = {
    'year': 2018,
    'km_driven': 35000,
    'engine': 1498,
    'max_power': 110,
    'brand': 'Honda',
    'mileage': 17.0
}
    print(predict_car_price(example_car, model_data))
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)  # no debug in prod
