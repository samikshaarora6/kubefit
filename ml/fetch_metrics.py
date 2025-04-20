import pandas as pd
import random
import time

# Constants
NUM_SAMPLES = 1000000  # 1 million metrics
TIME_PERIOD = 30  # simulate over 30 days
TYPES_OF_METRICS = ['cpu_usage', 'memory_usage', 'disk_avail', 'net_receive', 'net_transmit']
INSTANCE = 'localhost:9100'

# Function to generate random metrics data
def generate_random_metric_data():
    metric_data = []
    
    for _ in range(NUM_SAMPLES):
        metric_type = random.choice(TYPES_OF_METRICS)
        value = None
        
        # Generate random values for each metric type
        if metric_type == 'cpu_usage':
            value = round(random.uniform(0, 1), 4)  # Random value between 0 and 1
        elif metric_type == 'memory_usage':
            value = round(random.uniform(0, 16e9), 4)  # Random value for memory usage in bytes
        elif metric_type == 'disk_avail':
            value = round(random.uniform(0, 50e9), 4)  # Random available disk space in bytes
        elif metric_type == 'net_receive':
            value = round(random.uniform(0, 100e6), 4)  # Random network receive bytes per second
        elif metric_type == 'net_transmit':
            value = round(random.uniform(0, 100e6), 4)  # Random network transmit bytes per second
        
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(random.randint(1609459200, 1640995200)))  # Random date
        metric_data.append({
            "metric_type": metric_type,
            "instance": INSTANCE,
            "value": value,
            "timestamp": timestamp
        })
    
    return metric_data

# Generate synthetic data and save to CSV
def generate_and_save_data():
    print("⏳ Generating 1 million synthetic metrics...")
    metric_data = generate_random_metric_data()
    df = pd.DataFrame(metric_data)
    df.to_csv("bulk_metrics_large.csv", index=False)
    print("✅ 1 million metrics saved to bulk_metrics_large.csv")

if __name__ == "__main__":
    generate_and_save_data()
