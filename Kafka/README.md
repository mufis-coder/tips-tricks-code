# Kafka di windows with Ubuntu-wsl

Mengatur konfigurasi kafka di windows dengan bantuan ubuntu wsl.

1. Download kafka

Download dlu kafka di : https://kafka.apache.org/downloads

2. Extrak dan taruh file di ```Local disk (D:)```, bebas mau ditaruh folder apa

3. Atur konfigurasi pada:

a. config/server.properties
Ubah ```dataDir= /mnt/d/Code/Belajar/Non-Kuliah-root/Altera-SpringBoot-root/Kafka/kafka-data```. Menjadi path folder di mana file MQ akan disimpan. 

b. config/zookeeper.properties
Ubah ```log.dirs=/mnt/d/Code/Belajar/Non-Kuliah-root/Altera-SpringBoot-root/Kafka/kafka-data/kafka-logs```. Menjadi tempat di mana log kafka di simpan.

** Karena saya pakai wsl, maka path ```Local disk (D:)``` diubah menjadi ```/mnt/d```.

4. pindah ke folder di mana ekstrak file kafka di atas tadi

```
cd /mnt/d/Code/Belajar/Non-Kuliah-root/Altera-SpringBoot-root/Kafka/kafka_2.13-3.0.0
```

