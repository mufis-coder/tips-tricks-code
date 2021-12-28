# Kafka di windows with Ubuntu-wsl

Mengatur konfigurasi kafka di windows dengan bantuan ubuntu wsl.

- Download kafka

   - Download dlu kafka di : https://kafka.apache.org/downloads

- Extrak dan taruh file di ```Local disk (D:)```, bebas mau ditaruh folder apa

- Atur konfigurasi pada:

   - config/server.properties:

        Ubah ```dataDir= /mnt/d/Code/Belajar/Non-Kuliah-root/Altera-SpringBoot-root/Kafka/kafka-data```. Menjadi path folder di mana file MQ akan disimpan. 

   - config/zookeeper.properties
  
        Ubah ```log.dirs=/mnt/d/Code/Belajar/Non-Kuliah-root/Altera-SpringBoot-root/Kafka/kafka-data/kafka-logs```. Menjadi tempat di mana log kafka di simpan.

** Karena saya pakai wsl, maka path ```Local disk (D:)``` diubah menjadi ```/mnt/d```.

- pindah ke folder di mana ekstrak file kafka di atas tadi

    ```
    cd /mnt/d/Code/Belajar/Non-Kuliah-root/Altera-SpringBoot-root/Kafka/kafka_2.13-3.0.0
    ```

- Start  zookeeper

    ```
    bin/zookeeper-server-start.sh config/zookeeper.properties
    ```

- Start server-kafka

    ```
    bin/kafka-server-start.sh config/server.properties
    ```

- Buat topic untuk menyimpan event

    ```
    bin/kafka-topics.sh --create --partitions 1 --replication-factor 1 --topic fpbni-altera --bootstrap-server localhost:9092
    ```

- Nulis event ke suatu topic

    ```
    bin/kafka-console-producer.sh --topic fpbni-altera --bootstrap-server localhost:9092
    ```

- Baca event dari suatu topic
    
    ```
    bin/kafka-console-consumer.sh --topic fpbni-altera --from-beginning --bootstrap-server localhost:9092
    ```

- Melihat list topic yang tersedia

    ```
    bin/kafka-topics.sh --bootstrap-server=localhost:9002 --list
    ```