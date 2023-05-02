
# Recupera valor UF por fecha desdes SII.CL

Este script recibe como parametro una fecha en formato dd-mm-aaaa,
consulta a la web de servicio impuestos internos https://sii.cl, 
autogenera la URL respectiva con el año indicado, guarda los resultados por año en formato .csv

La API devuelve el resultado por dia,mes,año en formato JSON
```
{"data": { "dia": "1", "mes": "Enero","anio": "2021","UF": "29.069,39"}}
```
## instalación
```
git clone https://github.com/jacktravolta/ufchilesii

cd ufchilesii

mkdir repo

pip3 install -r requirements.txt

python3 main.py
```
## Testing
```
pytest
```
## API Reference

#### Get UF por fecha

```https
  GET http:/127.0.0.1:5556/api/01-02-2022
```

## Authors

- Juan Espinoza [@jacktravolta](https://github.com/jacktravolta/) 
