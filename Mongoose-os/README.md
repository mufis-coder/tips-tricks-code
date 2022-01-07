# Mongoose-os

Mongoose os adalah sebuah framework untuk firmware sebuah IoT. Repository ini berfungsi untuk menyimpan perintah-perintah penting dari mongoose os yang saya gunakan untuk membangun aplikasi IoT saya.

- Build firmware

```
mos build --local //buil secara lokal
```

- Flash firmware (masukan kodingan ke alat)

```
mos flash
```

- Masukan data wifi ke alat (saya menggunakan esp8266)

```
mos wifi "{nama-ssid-wifi}" "{password-wifi}" --port /dev/ttyUSB0
```
