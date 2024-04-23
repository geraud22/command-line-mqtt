# Import the necessary libraries
import os
from dotenv import load_dotenv
import paho.mqtt.client as mqtt

# Load variables from the .env file into the environment
load_dotenv()

# Initialize Environment Variables
APP_ID = os.getenv('APP_ID')
NETWORK_SERVER_IP = os.getenv('NETWORK_SERVER_IP')
NETWORK_SERVER_PORT = os.getenv('NETWORK_SERVER_PORT')

# Define callback functions
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        # Subscribe to uplinks from all devices within the app.
        client.subscribe(f"application/{APP_ID}/device/+/event/up")
        # Report success
        print("Connected to MQTT broker")
    else:
        print("Failed to connect, return code:", rc)

def on_message(client, userdata, message):
    print("\nReceived message on topic:", message.topic)
    print("Message payload:", message.payload.decode())

# Create MQTT client instance
client = mqtt.Client()

# Assign callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker
client.connect(f"{NETWORK_SERVER_IP}", NETWORK_SERVER_PORT, 60)

try:
    # Start the MQTT client loop
    client.loop_forever()
except KeyboardInterrupt:
    # Disconnect the client when Ctrl+C is pressed
    print("\nDisconnecting from MQTT broker...")
    client.disconnect()
    print("\nClient disconnected successfully.")
