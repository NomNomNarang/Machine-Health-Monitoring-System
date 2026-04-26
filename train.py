from sensor_simulator import SensorSimulator
from feature_engineering import FeatureEngineer
from anomaly_detector import AnomalyDetector

sim = SensorSimulator()
fe = FeatureEngineer()
detector = AnomalyDetector()

data = []

# Generate training data (normal conditions)
for _ in range(300):
    sensor_data = sim.generate()
    features = fe.transform(sensor_data)
    data.append(features)

import pandas as pd
X = pd.concat(data)

detector.train(X)
detector.save()

print("Model trained and saved.")