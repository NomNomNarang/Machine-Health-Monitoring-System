import random
import time
import matplotlib.pyplot as plt

values = []
prev = 0

plt.ion()  # interactive mode

while True:
    value = random.randint(0, 1023)

    # Classification
    if value < 300:
        status = "NORMAL"
    elif value < 700:
        status = "WARNING"
    else:
        status = "FAULT"

    # Anomaly detection
    anomaly = ""
    if abs(value - prev) > 200:
        anomaly = " | ANOMALY"

    print(f"Sensor: {value} | Status: {status}{anomaly}")

    # CSV logging (FIXED)
    with open("data.csv", "a") as f:
        f.write(f"{value},{status}\n")

    prev = value

    # Store values
    values.append(value)
    if len(values) > 20:
        values.pop(0)

    # Plot graph
    plt.clf()
    plt.plot(values)
    plt.title("Machine Health Monitoring")
    plt.xlabel("Time")
    plt.ylabel("Sensor Value")
    plt.pause(0.1)

    time.sleep(1)