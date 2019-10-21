# Import dos pacote
# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt

# Define Variaveis
MQTT_HOST = "localhost"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "AulaDoGui"
MQTT_MSG = "Aula do gui"

# funcao on connect
# se inscreve no topico


def on_connect(mosq, obj, rc):
    mqttc.subscribe(MQTT_TOPIC, 1)

# Define funcao on_message
# essa funcao é chamada toda vez que uma mensagem for publicada em um topico,


def on_message(mosq, obj, msg):
    #print("Nova mensagem chegou: ")
    print("Topic: " + str(msg.topic))
    # print("QoS: " + str(msg.qos))
    print("Payload: " + str(format(msg.payload)))


def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed to Topic: " +
          MQTT_MSG + " with QoS: " + str(granted_qos))


# inicia MQTT Client
mqttc = mqtt.Client()

# define variaveis do mqtt
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Conecta com MQTT Broker
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
mqttc.subscribe(MQTT_TOPIC)
# fica em loop
mqttc.loop_forever()
