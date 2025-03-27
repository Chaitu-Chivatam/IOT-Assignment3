import paho.mqtt.client as mqtt
import json

# Configuration (MUST MATCH virtual_station.py)
BROKER = "mqtt.eclipseprojects.io"
STATION_ID = "mac_station_*"  # Wildcard to match any station ID
TOPIC = f"iot_assignment/{STATION_ID}/sensor_data"

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Successfully connected to MQTT broker")
        # Subscribe to topic with proper wildcard syntax
        client.subscribe("iot_assignment/+/sensor_data")  # Correct wildcard format
    else:
        print(f"Connection failed with code {rc}")

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
        print("\n--- NEW SENSOR DATA ---")
        print(f"Station ID: {msg.topic.split('/')[1]}")
        print(f"Temperature: {data['temperature']}°C")
        print(f"Humidity: {data['humidity']}%")
        print(f"CO2: {data['co2']}ppm")
        print(f"Timestamp: {data['timestamp']}")
    except Exception as e:
        print(f"Error processing message: {str(e)}")

# Create MQTT client with VERSION2
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

try:
    print("Connecting to MQTT broker...")
    client.connect(BROKER, 1883, 60)
    print("Waiting for sensor data...")
    client.loop_forever()
except KeyboardInterrupt:
    print("\nDisconnecting from MQTT broker...")
    client.disconnect()
except Exception as e:
    print(f"Connection error: {str(e)}")