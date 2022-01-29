# Commands dan Fitur yang ada pada Protocol Buffer

## Pada Javascript

- Install dependensi

```bash
npm install google-protobuf
```

- Make file .proto to .js

```bash
protoc --js_out=import_style=commonjs,binary:. sensorAerator.proto
```
