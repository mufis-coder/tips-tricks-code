# Run Database Postgresql with Docker

## Install biasa di Ubuntu

- Install Postgresql di linux

    ```
    sudo -i -u postgres
    ##or
    sudo apt install postgresql postgresql-contrib
    psql --version ##cek versi
    ```

- Mengatur password postgres

    ```
    sudo passwd postgres ##masukan password untuk SU postgres
    ```

## Install menggunakan docker

- Install image posgres menggunakan docker dan pengaturan username dan password sendiri

    ```
    docker run -e POSTGRES_PASSWORD=POSTGRESQLPASSWORD -e POSTGRES_USER=POSTGRESQLUSARNAME postgres
    ```

- Melihat list docker dengan parameter all

    ```
    docker ps -a
    ```

- Membuat container postgressdb

    ```
    docker run --name postgres-db -e POSTGRES_PASSWORD=POSTGRESQLPASSWORD -p 5432:5432 -d postgres
    ```

- Start docker

    ```
    docker start postgres-db
    ```

- Masuk ke container dengan container-id

    ```
    docker exec -it 2b8621dd1c23652d1a3967b1a04deaa537130454d2c3f8400d4bee6692d2507e bash
    ```

## Penggunaan postgresql

- Cek penggunaan port ```5432``` karena ini adalah port default postgresql

    ```
    sudo ss -lptn 'sport = :5432' ##cek penggunaan port postgresql (5432)
    sudo kill -9 {pid} ##kill process dengan suatu pid
    ```

- Perintah utama postgres

    ```
    sudo service postgresql status ##for checking the status of your database.
    sudo service postgresql start ##to start running your database.
    sudo service postgresql stop ##to stop running your database.
    ```

- Membuat role baru user untuk postgresql. Masukan username dan password.

    ```
    createuser --interactive --pwprompt
    ```

- Masuk ke postgresql: masukan username dan password

    ```
    psql -U postgres -W
    ##or
    su - postgres
    ```

- Masuk ke environment postgres

    ```
    psql
    ```

- Melakukan DLL di postgres
  
    ```
    CREATE DATABASE "bni-fp"; ## membuat database baru
    DROP DATABASE eco_aerator; ## menghapus database
    \l ## melihat list database
    ```

- Masuk ke environment database

    ```
    \c "{namadb}"
    \dt ## melihat list table
    ```

- Melakukan DML di postgresql
  
    ```
    SELECT * FROM posts;

    UPDATE users SET email='admin@gmail.com' WHERE id=2;

    UPDATE users SET roles='admin' WHERE id=2;

    CREATE DATABASE myApp_dev;

    UPDATE users SET role="admin" WHERE id=1;
    ```

- Keluar dari environment database dan postgresql

    ```
    exit
    ```