# Run Database Postgresql with Docker

```sudo -i -u postgres``` //install postgress di linux

run image posgres dengan pengaturan username dan password sendiri
```
docker run -e POSTGRES_PASSWORD=POSTGRESQLPASSWORD -e POSTGRES_USER=POSTGRESQLUSARNAME postgres
```

```sudo ss -lptn 'sport = :5432'`` //cek penggunaan port postgresql (5432)
