
import numpy as np

class SensorSimulator:
    def __init__(self):
        self.t = 0

    def generate(self):
        self.t += 1

        vibration = 50 + 10 * np.sin(0.1 * self.t)
        temperature = 40 + 5 * np.sin(0.05 * self.t)
        pressure = 30 + 3 * np.sin(0.07 * self.t)
        rpm = 1800 + 250 * np.sin(0.08 * self.t)
        power = 120 + 15 * np.sin(0.06 * self.t)

        vibration += np.random.normal(0, 2)
        temperature += np.random.normal(0, 1)
        pressure += np.random.normal(0, 1)
        rpm += np.random.normal(0, 50)
        power += np.random.normal(0, 5)

        if self.t > 200:
            temperature += 0.05 * (self.t - 200)

        if 300 < self.t < 320:
            vibration += np.random.uniform(20, 40)
            rpm += np.random.uniform(500, 1200)

        return {
            "vibration": vibration,
            "temperature": temperature,
            "pressure": pressure,
            "rpm": rpm,
            "power": power
        }
