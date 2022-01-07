# Mongoose-os

Mongoose os adalah sebuah framework untuk firmware sebuah IoT. Repository ini berfungsi untuk menyimpan perintah-perintah penting dari mongoose os yang saya gunakan untuk membangun aplikasi IoT saya.

## Perintah-perintah dasar

- Build firmware

```
mos build --local //build secara lokal
```

- Flash firmware (masukan kodingan ke alat)

```
mos flash
```

- Masukan data wifi ke alat (saya menggunakan esp8266)

```
mos wifi "{nama-ssid-wifi}" "{password-wifi}" --port /dev/ttyUSB0
```

- Menyambungkan alat IoT dengan dashboard ([mdash.net](https://mdash.net))

```
mos config-set dash.enable=true dash.token={token-mdash} --port /dev/ttyUSB0
```

- Menyambungkan alat IoT dengan AWS IoT core

```
mos aws-iot-setup --aws-region ap-southeast-1 --aws-iot-policy mos-default
```

- Update firmware secara OTA

```
- mos build --local
- 'upload hasil build (fd.zip) ke mdash.net'
- 'commit hasil firmware terbaru menggunakan settingan OTA.commit di mdash.net'
```


## Perintah-perintah untuk membuat custom library mongoose-os