# 🔮 Kubernetes Resource Predictor

An AI-powered tool to analyze past CPU & memory usage of Kubernetes pods and recommend optimal `requests` and `limits`.

## 🚀 Features

- Fetches metrics using Prometheus
- Trains ML models to predict future resource usage
- Suggests optimized Helm values
- Optional: Visual dashboard (Streamlit)

## 🛠️ Tech Stack

- Python, XGBoost
- Prometheus
- Kubernetes API
- Streamlit (optional)

## 📦 Setup

```bash
git clone https://github.com/your-username/k8s-resource-predictor.git
cd k8s-resource-predictor
pip install -r requirements.txt
