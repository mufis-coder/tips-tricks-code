# Run Database Postgresql with Docker

## Install biasa di Ubuntu

- Install Postgresql di linux

    ```bash
    sudo -i -u postgres
    ##or
    sudo apt install postgresql postgresql-contrib
    psql --version ##cek versi
    ```

- Mengatur password postgres

    ```bash
    sudo passwd postgres ##masukan password untuk SU postgres
    ```

## Install menggunakan docker

- Install image posgres menggunakan docker dan pengaturan username dan password sendiri

    ```bash
    docker run -e POSTGRES_PASSWORD=POSTGRESQLPASSWORD -e POSTGRES_USER=POSTGRESQLUSARNAME postgres
    ```

- Melihat list docker dengan parameter all

    ```bash
    docker ps -a
    ```

- Membuat container postgressdb

    ```bash
    docker run --name postgres-db -e POSTGRES_PASSWORD=POSTGRESQLPASSWORD -p 5432:5432 -d postgres
    ```

- Start docker

    ```bash
    docker start postgres-db
    ```

- Masuk ke container dengan container-id

    ```bash
    docker exec -it 2b8621dd1c23652d1a3967b1a04deaa537130454d2c3f8400d4bee6692d2507e bash
    ```

## Penggunaan postgresql

- Cek penggunaan port ```5432``` karena ini adalah port default postgresql

    ```bash
    sudo ss -lptn 'sport = :5432' ##cek penggunaan port postgresql (5432)
    sudo kill -9 {pid} ##kill process dengan suatu pid
    ```

- Perintah utama postgres

    ```bash
    sudo service postgresql status ##for checking the status of your database.
    sudo service postgresql start ##to start running your database.
    sudo service postgresql stop ##to stop running your database.
    ```

- Membuat role baru user untuk postgresql. Masukan username dan password.

    ```bash
    createuser --interactive --pwprompt
    ```

- Masuk ke postgresql: masukan username dan password

    ```bash
    psql -U postgres -W
    ##or
    su - postgres
    ```

- Masuk ke environment postgres

    ```bash
    psql
    ```

- Melakukan DLL di postgres
  
    ```sql
    CREATE DATABASE "bni-fp";  <!--membuat database baru -->
    DROP DATABASE eco_aerator; <!--menghapus database -->
    \l <!--melihat list database-->
    ```

- Masuk ke environment database

    ```bash
    \c "{namadb}"
    \dt ## melihat list table
    ```

- Melakukan DML di postgresql
  
    ```sql
    SELECT * FROM posts;

    UPDATE users SET email='admin@gmail.com' WHERE id=2;

    UPDATE users SET roles='admin' WHERE id=2;

    CREATE DATABASE myApp_dev;

    UPDATE users SET role="admin" WHERE id=1;
    ```

- Keluar dari environment database dan postgresql

    ```bash
    exit
    ```
