# Importere library til at forbinde til adafruit.io
import mqttBotPubSub
from machine import Pin
import dht
from time import sleep
lib = mqttBotPubSub
sensor = dht.DHT22(Pin(14))
while True:
    try:
        # print(lib.m)
        # sleep(1)
        # lib.m vil indholde strengen som indtastes i feltet "skriv til Jarvis"
        # Hvis strengen er identisk med "Streng til Bot" køres koden i if sætningen
        if lib.m == "skål":
            # Strengen som sættes i msg="din streng her" vil komme i adafruit som "svar fra Jarvis"
            lib.client.publish(topic=lib.mqtt_pub_feedname, msg="lååå!")
            # Tøm strengen igen, ellers vil den køre i en uendelighed og crashe :)
            lib.m = ""
        if lib.m == "fortæl en joke":
            # Strengen som sættes i msg="din streng her" vil komme i adafruit som "svar fra Jarvis"
            lib.client.publish(topic=lib.mqtt_pub_feedname, msg="Hvorfor bliver zoologisk have aldrig solgt? \n fordi den er for dyr :D")
            # Tøm strengen igen, ellers vil den køre i en uendelighed og crashe :)
            lib.m = ""
        if lib.m == "hvad er temperaturen?":
            sleep(2)
            sensor.measure()
            temp = sensor.temperature()
            print(temp)
            # Strengen som sættes i msg="din streng her" vil komme i adafruit som "svar fra Jarvis"
            lib.client.publish(topic=lib.mqtt_pub_feedname, msg="temperaturen er "+str(temp)+" C")
            # Tøm strengen igen, ellers vil den køre i en uendelighed og crashe :)
            lib.m = ""
        if lib.m == "hvad er fugtigheden?":
            sleep(2)
            sensor.measure()
            hum = sensor.humidity()
            print(hum)
            # Strengen som sættes i msg="din streng her" vil komme i adafruit som "svar fra Jarvis"
            lib.client.publish(topic=lib.mqtt_pub_feedname, msg="fugtigheden er "+str(hum)+" %")
            # Tøm strengen igen, ellers vil den køre i en uendelighed og crashe :)
            lib.m = ""
        if lib.m == "forbind igen":
            lib.clientConnect(lib.ADAFRUIT_USERNAME, lib.ADAFRUIT_IO_PUB_FEEDNAME, lib.ADAFRUIT_IO_SUB_FEEDNAME)
            # Strengen som sættes i msg="din streng her" vil komme i adafruit som "svar fra Jarvis"
            lib.client.publish(topic=lib.mqtt_pub_feedname, msg="forbinder igen...")
            # Tøm strengen igen, ellers vil den køre i en uendelighed og crashe :)
            lib.m = ""

        # Tjekker for nye beskeder
        lib.client.check_msg()
    # Stopper programmet når der trykkes Ctrl + c
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        lib.client.disconnect()
        lib.sys.exit()
    except OSError as e:
        print('Failed to read sensor.')

