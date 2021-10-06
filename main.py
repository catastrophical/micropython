# Importere library til at forbinde til adafruit.io
import mqttJarvisPubSub
import mp3
lib = mqttJarvisPubSub

while True:
    try:
        # lib.m vil indholde strengen som indtastes i feltet "skriv til Jarvis"
        # Hvis strengen er identisk med "hej Jarvis" køres koden i if sætningen
        startMusik = ["start", "start musik", "spil musik", "play music"]
        if lib.m in startMusik:
            # Strengen som sættes i msg="din streng her" vil komme i adafruit som "svar fra Jarvis"
            lib.client.publish(topic=lib.mqtt_pub_feedname, msg="starter musikken nu!")
            # Tøm strengen igen, ellers vil den køre i en uendelighed og crashe :)
            mp3.uart1.write(mp3.play)  # write 5 bytes
            lib.m = ""
        pauseMusik = ["pause", "pause musik", "stop musik", "stop"]
        if lib.m in pauseMusik:
            # Strengen som sættes i msg="din streng her" vil komme i adafruit som "svar fra Jarvis"
            lib.client.publish(topic=lib.mqtt_pub_feedname, msg="pauser musikken nu!")
            # Tøm strengen igen, ellers vil den køre i en uendelighed og crashe :)
            mp3.uart1.write(mp3.pause)  # write 5 bytes
            lib.m = ""
        # Tjekker for nye beskeder
        lib.client.check_msg()
    # Stopper programmet når der trykkes Ctrl + c
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        lib.client.disconnect()
        lib.sys.exit()
