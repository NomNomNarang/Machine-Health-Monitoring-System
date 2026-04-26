import sys
import os

model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'model.pkl')

import streamlit as st
import pandas as pd
import time
from sensor_simulator import SensorSimulator
from feature_engineering import FeatureEngineer
from anomaly_detector import AnomalyDetector

st.title("Machine Health Monitoring Dashboard")

sim = SensorSimulator()
fe = FeatureEngineer()
detector = AnomalyDetector()
detector.load(model_path)

chart_data = []

for _ in range(200):
    sensor_data = sim.generate()
    features = fe.transform(sensor_data)

    pred = detector.predict(features)[0]

    sensor_data["status"] = "ANOMALY" if pred == -1 else "NORMAL"
    chart_data.append(sensor_data)

    df = pd.DataFrame(chart_data)

    st.line_chart(df[["vibration", "temperature", "pressure"]])

    if pred == -1:
        st.error("⚠️ Anomaly Detected!")

    time.sleep(0.5)