# Commands dan Fitur yang ada pada Mosquitto-MQTT

## Perintah-perintah dasar

- Membuat Subscriber

    ```bash
    mosquitto_sub -h test.mosquitto.org -t "test/broker/mqttt" -v "hallo"
    ```

- Membuat Publisher

    ```bash
    mosquitto_pub -h test.mosquitto.org -t "ecoaerator/device/sensor_aerator/esp8266/501" -m "0"
    ```
