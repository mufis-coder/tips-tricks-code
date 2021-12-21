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

3. Tampilkan list images yang ada pada docker kita.

```
docker images
```

4. Login pada akun ```https://hub.docker.com/```

```
docker login --username=mufis
```

5. Run docker container yang ingin kita run, dengan parameter ":latest" -> berarti kita menjalankan container dengan nama "spring-demo" dengan tag "latest".

```
docker run -d -p 8080:8080 --name spring-demo mufis/demo:latest
```