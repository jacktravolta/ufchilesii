
# Recupera valor UF por fecha desdes SII.CL

Este script recibe como parametro una fecha formato: dd-mm-aaaa 
Consulta a la web de servicio impuestos internos, 
autogenera la URL respectiva con el año indicado,
guarda los resultados por año en formato csv.
Devuelve el resultado formato JSON

{"data": { "dia": "1", "mes": "Enero","anio": "2021","UF": "29.069,39"}}

## Instalaciòn

git clone https://github.com/jacktravolta/ufchilesii

cd ufchilesii

mkdir repo

pip3 install -r requirements.txt

python3 main.py

## API Reference

#### Get UF por fecha

```https
  GET /api/01-02_2022
```

## Authors

- Juan Espinoza [@jacktravolta](https://github.com/jacktravolta/) 
