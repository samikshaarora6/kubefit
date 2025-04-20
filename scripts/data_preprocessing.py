import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Load data (assuming you have a CSV file or similar format)
df = pd.read_csv("prometheus_metrics.csv")  # Replace with your actual data source

# Feature Engineering: Add a new column for the hour of the day (or any other time-based feature)
df['hour'] = pd.to_datetime(df['timestamp']).dt.hour

# Fill missing values
df.fillna(method='ffill', inplace=True)

# Features and target variables (Assuming 'cpu_usage' and 'memory_usage' are the target columns)
X = df[['hour', 'previous_cpu_usage', 'previous_memory_usage']]  # Example features
y_cpu = df['cpu_usage']  # Target for CPU usage prediction
y_memory = df['memory_usage']  # Target for Memory usage prediction

# Feature scaling (standardization)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split data into training and test sets (80-20 split)
X_train, X_test, y_cpu_train, y_cpu_test = train_test_split(X_scaled, y_cpu, test_size=0.2, random_state=42)
X_train, X_test, y_memory_train, y_memory_test = train_test_split(X_scaled, y_memory, test_size=0.2, random_state=42)

# Save preprocessed data for future use
X_train.to_csv("X_train.csv", index=False)
X_test.to_csv("X_test.csv", index=False)
y_cpu_train.to_csv("y_cpu_train.csv", index=False)
y_cpu_test.to_csv("y_cpu_test.csv", index=False)
y_memory_train.to_csv("y_memory_train.csv", index=False)
y_memory_test.to_csv("y_memory_test.csv", index=False)
