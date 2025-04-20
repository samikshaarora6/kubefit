from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load models
cpu_model = joblib.load('cpu_model.pkl')
memory_model = joblib.load('memory_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Convert input data to DataFrame for prediction
    new_data = pd.DataFrame(data)
    
    # Make predictions
    cpu_prediction = cpu_model.predict(new_data)
    memory_prediction = memory_model.predict(new_data)

    # Return predictions as JSON
    return jsonify({
        'cpu_usage': cpu_prediction[0],
        'memory_usage': memory_prediction[0]
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
