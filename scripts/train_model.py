import xgboost as xgb
import pandas as pd
from sklearn.metrics import mean_squared_error
import joblib

# Load preprocessed data
X_train = pd.read_csv("X_train.csv")
X_test = pd.read_csv("X_test.csv")
y_cpu_train = pd.read_csv("y_cpu_train.csv").squeeze()
y_cpu_test = pd.read_csv("y_cpu_test.csv").squeeze()
y_memory_train = pd.read_csv("y_memory_train.csv").squeeze()
y_memory_test = pd.read_csv("y_memory_test.csv").squeeze()

# Train XGBoost model for CPU usage prediction
cpu_model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=1000, max_depth=6)
cpu_model.fit(X_train, y_cpu_train)

# Train XGBoost model for Memory usage prediction
memory_model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=1000, max_depth=6)
memory_model.fit(X_train, y_memory_train)

# Predict and evaluate the models
y_cpu_pred = cpu_model.predict(X_test)
y_memory_pred = memory_model.predict(X_test)

# Calculate Mean Squared Error
cpu_mse = mean_squared_error(y_cpu_test, y_cpu_pred)
memory_mse = mean_squared_error(y_memory_test, y_memory_pred)

print(f"CPU Prediction MSE: {cpu_mse}")
print(f"Memory Prediction MSE: {memory_mse}")

# Save the trained models
joblib.dump(cpu_model, 'cpu_model.pkl')
joblib.dump(memory_model, 'memory_model.pkl')
