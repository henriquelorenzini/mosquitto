# Import dos pacotes

import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

# Define Variables
MQTT_HOST = "localhost"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 45
MQTT_TOPIC = "AulaDoGui"
MQTT_MSG = "Aula do gui"

# onpublish para publicar
def on_publish(client, userdata, mid):
    print("Message Published...")


# Inicia MQTT Client
mqttc = mqtt.Client()

# define o onpublish do mqtt como nossa funcao
mqttc.on_publish = on_publish

# Conecta com MQTT Broker
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

# Condicao break para continuar pedindo frase
brkCondition = True
print("Publicando mosquitto ('exit' para sair)")

while(brkCondition):
    msg = input("escreva sua msg: ")
    if(msg == 'exit'):
        brkCondition = False
    else:
        # Publica messagem no MQTT Broker
        mqttc.publish(MQTT_TOPIC, msg)

# Disconecta do MQTT_Broker
mqttc.disconnect()
