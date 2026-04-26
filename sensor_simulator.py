import numpy as np

class SensorSimulator:
    def __init__(self):
        self.t = 0

    def generate(self):
        self.t += 1

        # Base signals
        vibration = 50 + 10 * np.sin(0.1 * self.t)
        temperature = 40 + 5 * np.sin(0.05 * self.t)
        pressure = 30 + 3 * np.sin(0.07 * self.t)

        # Add noise
        vibration += np.random.normal(0, 2)
        temperature += np.random.normal(0, 1)
        pressure += np.random.normal(0, 1)

        # Drift
        if self.t > 200:
            temperature += 0.05 * (self.t - 200)

        # Fault injection
        if 300 < self.t < 320:
            vibration += np.random.uniform(20, 40)

        return {
            "vibration": vibration,
            "temperature": temperature,
            "pressure": pressure
        }