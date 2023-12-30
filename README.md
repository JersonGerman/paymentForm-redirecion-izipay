# Formulario en redirección con Flask - Izipay


## Requirements
* Python 3.10v o superior

## Configuration
1. Configurar el archivo `key.py` con tus credenciales de Izipay
```sh
CONFIG = {
    "SHOP_ID": 12345678,
    "CLAVE": "AN7sDGDsd9UQ1cXLXSsaS",
    "MODE": "TEST",
    "URL" : "https://secure.micuentaweb.pe/vads-payment/"
}
```
2. Instalar librerias
```sh
pip install Flask Flask-Cors
```
3. Levandar servidor de desarrollo
```sh
py app.py
```
4. Abrir la url en el navegador `http://localhost:5000`

