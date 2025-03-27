import random
import time
import json
import paho.mqtt.client as mqtt
import requests
from datetime import datetime

# ===== CONFIGURATION =====
# MQTT Settings
STATION_ID = "mac_station_" + str(random.randint(1000, 9999))
BROKER = "mqtt.eclipseprojects.io"
TOPIC = f"iot_assignment/{STATION_ID}/sensor_data"

# ThingSpeak Settings (REPLACE WITH YOUR KEYS!)
THINGSPEAK_API_KEY = "JISWGEN7IGWQ0X0R"  # ← Paste your key here
THINGSPEAK_URL = f"https://api.thingspeak.com/update?api_key={THINGSPEAK_API_KEY}"

# ===== MQTT SETUP =====
def on_connect(client, userdata, flags, rc):
    print(f"Connected to MQTT Broker (Code: {rc})")

client = mqtt.Client()
client.on_connect = on_connect
client.connect(BROKER, 1883, 60)

# ===== SENSOR DATA GENERATION =====
def generate_sensor_data():
    return {
        "temperature": round(random.uniform(-50, 50), 2),
        "humidity": round(random.uniform(0, 100), 2),
        "co2": random.randint(300, 2000),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# ===== THINGSPEAK PUBLISHER =====
def publish_to_thingspeak(data):
    params = {
        "field1": data["temperature"],
        "field2": data["humidity"],
        "field3": data["co2"]
    }
    try:
        response = requests.get(THINGSPEAK_URL, params=params)
        print(f"ThingSpeak Status: HTTP {response.status_code}")
    except Exception as e:
        print(f"ThingSpeak Error: {str(e)}")

# ===== MAIN PUBLISHING LOOP =====
def publish_data():
    try:
        while True:
            # Generate and send data
            data = generate_sensor_data()
            
            # Publish to MQTT
            payload = json.dumps(data)
            client.publish(TOPIC, payload)
            print(f"MQTT Published: {payload}")
            
            # Send to ThingSpeak
            publish_to_thingspeak(data)
            
            # Wait 30 seconds
            time.sleep(30)
            
    except KeyboardInterrupt:
        print("\n Stopping publisher...")
        client.disconnect()

# ===== ENTRY POINT =====
if __name__ == "__main__":
    print(f"Starting Mac IoT Station: {STATION_ID}")
    client.loop_start()
    publish_data()
