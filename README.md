# IOT-Assignment3
This is my IOT assignment regarding the creation of Environmental Monitoring System

**IoT Environmental Monitoring System**

**CIS600 Internet of Things: Application Development - Assignment 3**

**Project Overview**

This project implements a cloud-based IoT system for environmental monitoring using virtual sensors (temperature, humidity, CO2) that publish data via MQTT to ThingSpeak for visualization and analysis.

**Features**

**✅ Virtual Sensor Station:** Simulates environmental sensors with randomized data.

**✅ Real-time Monitoring:** Subscribes to MQTT for live data display.

**✅ Cloud Integration:** Stores and visualizes data on ThingSpeak.

**✅ Historical Analysis:** Retrieves and displays past sensor readings.

**System Architecture:**

Virtual Sensors(Python) → MQTT Broker(Eclipse Mosquitto) → ThingSpeak Cloud(Web Dashboard) → Data Visualization(Web Dashboard)
  

**Installation & Setup:**

**1. Prerequisites**

Python 3.8+
Required libraries:
pip install paho-mqtt requests numpy

**2. Configuration**

ThingSpeak Setup

Create a channel at thingspeak.com

Note your:

CHANNEL_ID

WRITE_API_KEY (for virtual_station.py)

READ_API_KEY (for historical_data.py)

**Update Configurations**

**In virtual_station.py:**

THINGSPEAK_API_KEY = "YOUR_WRITE_API_KEY"

**In historical_data.py:**

CHANNEL_ID = "YOUR_CHANNEL_ID"
READ_API_KEY = "YOUR_READ_API_KEY"

**Usage:**

**1.Run the Virtual Station**

python3 virtual_station.py

**Expected Output:**

Starting Mac IoT Station: mac_station_1234  
MQTT Published: {"temperature": 23.45, ...}  
ThingSpeak Status: HTTP 200  

**2. View Real-time Data**

python3 subscriber.py

**Expected Output:**

NEW SENSOR DATA  
Temperature: 23.45°C  
Humidity: 56.78%  
CO2: 1200ppm  

**3. Retrieve Historical Data**

python3 historical_data.py

**Expected Output:**

Historical Data - Last 5 Hours  
Timestamp: 2025-03-27 14:30:00  
Temperature: 23.45°C  
Humidity: 56.78%  
CO2: 1200ppm  

**Troubleshooting Guide**

If you encounter issues while running the IoT monitoring system, follow these steps to diagnose and resolve common problems:

**1.MQTT Connection Failures:** Ensure your firewall allows traffic on port 1883 and verify the broker URL (mqtt.eclipseprojects.io). If the connection is unstable, try an alternative broker like test.mosquitto.org.

**2.ThingSpeak API Errors:** Double-check your Write API Key (for virtual_station.py) and Read API Key (for historical_data.py). Ensure your channel is set to Public (temporarily) if data isn’t appearing in ThingSpeak.

**3.No Historical Data:** The historical_data.py script requires the virtual station to run for at least 30 minutes before retrieving entries. Verify your CHANNEL_ID matches the ThingSpeak dashboard.

**4.Incomplete/Incorrect Data:** Confirm the sensor data fields (field1, field2, field3) in ThingSpeak match the keys in your Python scripts (temperature, humidity, CO2).

**5.Timezone Mismatches:** If timestamps are inconsistent, enforce UTC in all scripts (datetime.utcnow()) and ThingSpeak settings.

For deeper debugging, run scripts with debug prints enabled or test the ThingSpeak API manually using:

curl "https://api.thingspeak.com/channels/YOUR_CHANNEL_ID/feeds.json?api_key=YOUR_READ_API_KEY&results=2"  
If issues persist, check the error logs or restart all components (virtual_station.py, subscriber.py, and historical_data.py).

**Files**

**virtual_station.py** - Sensor simulator and publisher

**subscriber.py** - Real-time data monitor

**historical_data.py** - ThingSpeak data analyzer

**License**
This project is licensed under the MIT License.

**Developed by:** Sri Krishna Chaitanya Chivatam
**Course:** CIS600 Internet of Things - Spring 2025
**GitHub:** github.com/Chaitu-Chivatam/IOT-Assignment3
