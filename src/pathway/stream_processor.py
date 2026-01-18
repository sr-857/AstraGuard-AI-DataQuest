import random
import os
import pickle
from typing import Dict, Tuple

MODEL_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../configs/models/anomaly_if.pkl"))
_MODEL = None

def load_model():
    """Load the anomaly detection model."""
    global _MODEL
    if os.path.exists(MODEL_PATH):
        try:
            with open(MODEL_PATH, "rb") as f:
                _MODEL = pickle.load(f)
            print("Model loaded successfully.")
        except Exception as e:
            print(f"Error loading model: {e}")
    else:
        print("Model file not found. Using heuristic mode.")

def detect_anomaly(data: Dict) -> Tuple[bool, float]:
    """
    Detect anomaly in telemetry data.
    Returns (is_anomalous, anomaly_score)
    """
    # Heuristic fallback if model not loaded or for specific checks
    score = 0.0
    
    # Simple heuristic checks based on known ranges
    if data.get("voltage", 8.0) < 7.0 or data.get("voltage", 8.0) > 9.0:
        score += 0.4
    if data.get("temperature", 25.0) > 40.0:
        score += 0.3
    if abs(data.get("gyro", 0.0)) > 0.1:
        score += 0.3
        
    # Random noise for simulation realism
    score += random.uniform(0, 0.1)
    
    is_anomalous = score > 0.6
    return is_anomalous, score
