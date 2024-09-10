import paho.mqtt.publish as publish

publish.single("casa1/garagem/temp", "20.4", hostname="test.mosquitto.org")
publish.single("casa1/sala/temp", "19.4", hostname="test.mosquitto.org")