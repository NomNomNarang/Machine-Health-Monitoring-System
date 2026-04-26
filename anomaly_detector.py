from sklearn.ensemble import IsolationForest
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import joblib

class AnomalyDetector:
    def __init__(self):
        self.pipeline = Pipeline([
            ("scaler", StandardScaler()),
            ("model", IsolationForest(contamination=0.05, random_state=42))
        ])

    def train(self, X):
        self.pipeline.fit(X)

    def predict(self, X):
        return self.pipeline.predict(X)  # -1 anomaly, 1 normal

    def save(self, path="models/model.pkl"):
        joblib.dump(self.pipeline, path)

    def load(self, path="models/model.pkl"):
        self.pipeline = joblib.load(path)