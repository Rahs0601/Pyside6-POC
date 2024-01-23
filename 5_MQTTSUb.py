import paho.mqtt.client as mqtt

# Define the MQTT broker and topic
broker_address = "127.0.0.1"
topic = "HMI-To-Service-Topic"

# Callback when a message is received
def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()}")

# Create an MQTT client instance
client = mqtt.Client("Subscriber")

# Set the on_message callback
client.on_message = on_message

# Connect to the broker
client.connect(broker_address)

# Subscribe to the specified topic
client.subscribe(topic)

# Keep the script running to receive messages
client.loop_forever()
