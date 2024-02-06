# deploy_script.py

from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model during initialization
model = joblib.load("model.joblib")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the request
        data = request.get_json()

        # Convert input data to a DataFrame
        input_data = pd.DataFrame(data)

        # Make predictions using the loaded model
        predictions = model.predict(input_data)

        # Return the predictions as JSON
        return jsonify(predictions.tolist())

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(port=5000)
