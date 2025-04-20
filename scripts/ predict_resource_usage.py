import pandas as pd
import joblib

# Load the trained models
cpu_model = joblib.load('cpu_model.pkl')
memory_model = joblib.load('memory_model.pkl')

# Example new data (this could be from an API, Prometheus data, etc.)
new_data = pd.DataFrame({
    'hour': [15],  # Example: 3 PM
    'previous_cpu_usage': [0.75],  # Example: 75% CPU usage previously
    'previous_memory_usage': [1500]  # Example: 1500 MB memory usage previously
})

# Use the model to predict CPU and Memory usage
cpu_prediction = cpu_model.predict(new_data)
memory_prediction = memory_model.predict(new_data)

print(f"Predicted CPU usage: {cpu_prediction[0]} cores")
print(f"Predicted Memory usage: {memory_prediction[0]} MB")
