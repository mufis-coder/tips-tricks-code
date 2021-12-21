# Perintah-perintah pada Docker

Isi dari tips dan trik ini adalah perintah-perintah yang dibutuhkan pada docker.

## 01 Buat File Dockerfile
Pertama buat dahulu file docker pada aplikasi yang akan dikontainerisasi menggunakan docker. Isi file tersebut dengan perintah docker, contoh saya akan kontainerisasi aplikasi springboot java. Maka isi Dockerfile dengan.
```
FROM openjdk:11.0.10-jdk-oracle
EXPOSE 8080
ADD target/*.jar app.jar
ENTRYPOINT ["java", "-jar", "app.jar"]
```

## 02 Pada command prompt/terminal lakukan perintah docker
Sebelumnya harus install docker dahulu, kalo di windows menggunakan docker dekstop.
1. Build aplikasi yang akan dikontainerisasi, tanda "." berarti kontainerisasi terjadi pada folder di mana terminal dibuka.
 ```
docker build -t mufis/demo:latest . 
```
2. Tampilkan list container yang ada pada docker kita.
```
docker container ls
```