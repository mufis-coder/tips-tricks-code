# Run Database Postgresql with Docker

```sudo -i -u postgres``` //install postgress di linux

run image posgres dengan pengaturan username dan password sendiri

```
docker run -e POSTGRES_PASSWORD=POSTGRESQLPASSWORD -e POSTGRES_USER=POSTGRESQLUSARNAME postgres
```

``` sudo ss -lptn 'sport = :5432' ``` //cek penggunaan port postgresql (5432)

``` sudo kill -9 {pid} ``` //kill process dengan suatu pid

``` docker ps -a ``` // melihat list docker dengan parameter all

membuat container postgress db

```
docker run --name postgres-db -e POSTGRES_PASSWORD=POSTGRESQLPASSWORD -p 5432:5432 -d postgres
```

``` docker start postgres-db ``` //start docker

masuk ke container dengan container-id

```
docker exec -it 2b8621dd1c23652d1a3967b1a04deaa537130454d2c3f8400d4bee6692d2507e bash
```

``` psql -U postgres -W ``` // masuk ke nama user