import joblib
import xgboost as xgb
import pandas as pd

# Train models (reuse the code from `train_model.py` if needed)

# Save the models after training
joblib.dump(cpu_model, 'cpu_model.pkl')
joblib.dump(memory_model, 'memory_model.pkl')
