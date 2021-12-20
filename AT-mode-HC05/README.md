# Pairing Master-Slave HC-05 Module

## 01 Upload code pada arduino nano
Upload kodingan pada folder ```.\setUp_bt\setUp_bt.ino``` pada arduino nano. Sambungkan HC-05 dengan ketentuan ```RX pada D3 dan TX pada D2```.  Pada saat upload, copot HC-05 dari arduino.

## 02 Masuk mode AT
Copot HC-05 dari arduino nano, saat bersamaan arduino nano dicolokan pada laptop -> pencet tombol yang ada pada HC-05, tekan terus hingga kedip lampu HC-05 melambat. Pada

## 03 Command AT mode
Buka serial monitor, lalu ubah ```baud menjadi 9600```, serta ubah samping kirinya menjadi ```Both NL & CR.```
Tes apakah sudah masuk AT-Mode, ketikan:
```
AT
```
Jika keluar balasan "OK", berarti HC-05 telah berhasil masuk ke AT-Mode.

### Pada Slave HC-05
1. ```AT+NAME={Name-HC05}``` untuk setting nama slave HC-05
2. ```AT+ROLE=0``` untuk setting role (menjadi slave) HC-05
3. ```AT+ADDR?``` untuk mengetahui alamat dari HC-05, catat alamat ini. Hal ini akan dimasukan ke HC-05 master.

### Pada Master HC-05
1. ```AT+NAME={Name-HC05}``` untuk setting nama master HC-05
2. ```AT+ROLE=1``` untuk setting role (menjadi master) HC-05
3. ```AT+CMODE=0``` untuk setting master HC-05 hanya bisa konek ke 1 device bluetooth.
4. ```AT+BIND={addresSlave}``` untuk setting addres slave yang akan konek dengan master.

catatan ketika ```AT+BIND=```, jangan lupa untuk mengubah ";" dari alamat slave menjadi ",". Contoh: alamat yang didapat dari slave ```0021:06:083F03``` maka ubah menjadi ```0021,06,083F03```.

## Tambahan
USERNAME: 
- MBT-{idsensor} //master
- SBT-{idsensor} //slave

PASSWORD:
- BluetoothModule{idsensor}