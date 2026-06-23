
import os, sys, time
import pandas as pd
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sensor_simulator import SensorSimulator
from feature_engineering import FeatureEngineer
from anomaly_detector import AnomalyDetector

model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'model.pkl')

st.set_page_config(page_title="Industry 4.0 Machine Health Intelligence", layout="wide")
st.title("🏭 Industry 4.0 Machine Health Intelligence Platform")

sim = SensorSimulator()
fe = FeatureEngineer()
detector = AnomalyDetector()
detector.load(model_path)

records = []

for _ in range(150):
    sensor_data = sim.generate()
    features = fe.transform(sensor_data)
    pred = detector.predict(features)[0]

    health_score = 95 if pred == 1 else 55

    if health_score >= 85:
        status = "Healthy"
        recommendation = "No action required"
    elif health_score >= 70:
        status = "Monitor"
        recommendation = "Observe operating conditions"
    elif health_score >= 50:
        status = "Service Required"
        recommendation = "Inspect bearings and cooling systems"
    else:
        status = "Critical"
        recommendation = "Immediate maintenance required"

    sensor_data["health_score"] = health_score
    sensor_data["status"] = status
    sensor_data["recommendation"] = recommendation

    records.append(sensor_data)

df = pd.DataFrame(records)

c1,c2,c3=st.columns(3)
c1.metric("Telemetry Records", len(df))
c2.metric("Health Score", int(df["health_score"].iloc[-1]))
c3.metric("Machine Status", df["status"].iloc[-1])

st.subheader("Sensor Telemetry")
st.line_chart(df[["vibration","temperature","pressure","rpm","power"]])

st.subheader("Maintenance Recommendation")
st.info(df["recommendation"].iloc[-1])

st.subheader("Recent Records")
st.dataframe(df.tail(10))
