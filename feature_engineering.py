import pandas as pd

class FeatureEngineer:
    def __init__(self, window=5):
        self.window = window
        self.df = pd.DataFrame()

    def transform(self, new_data):
        self.df = pd.concat([self.df, pd.DataFrame([new_data])]).tail(50)

        features = {}

        for col in self.df.columns:
            series = self.df[col]
            features[f"{col}_mean"] = series.rolling(self.window).mean().iloc[-1]
            features[f"{col}_std"] = series.rolling(self.window).std().iloc[-1]
            features[f"{col}_roc"] = series.diff().iloc[-1]

        return pd.DataFrame([features]).fillna(0)