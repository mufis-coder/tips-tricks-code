# Commands dan Fitur yang ada pada NanoPB (protocol buffer untuk C)

## Perintah-perintah dasar

- Membuat .proto ke .c

```bash
protoc \
   --plugin=protoc-gen-nanopb=/home/mufis-linux/Projek/IoT/nanopb-src/nanopb/generator/protoc-gen-nanopb \
   --nanopb_out=. *.proto
```
