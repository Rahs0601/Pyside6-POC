import paho.mqtt.client as mqtt
import time

# Define the MQTT broker and topic
broker_address = "127.0.0.1"
topic = "HMI-To-Service-Topic"

# Create an MQTT client instance
client = mqtt.Client("Publisher")

try:
    # Connect to the broker
    client.connect(broker_address)

    # Publish a message every 2 seconds for 10 times (adjust as needed)
    for _ in range(10):
        message = "Hello, MQTT!"
        client.publish(topic, message)
        print(f"Published: {message}")
        time.sleep(2)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Disconnect from the broker when done
    client.disconnect()
    print("Disconnected from the broker")
