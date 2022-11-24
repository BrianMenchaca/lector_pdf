# Lector de PDF

Para correr el programa debes seguir las siguientes instrucciones en la terminal:

## WSL

1- Debemos tener instalado WSL
2- Ejecutar los siguiente comandos:
```sh
sudo apt-get update
sudo apt-get upgrade
```
3- Instalar Poppler
```sh
sudo apt install poppler-utils
```
4- Verificar que esta instalado correctamente:
```sh
pdftocairo -v
```

## Crear y activar ambiente virtual

Dentro de la carpeta donde se clonará el programa

```sh
git clone https://github.com/BrianMenchaca/lector_pdf.git
cd lector_pdf
python3 -m venv env
source env/bin/activate
```

## Instalar los modulos necesarios para el programa

```sh
pip3 install -r requirements.txt
```

## Instrucciones de uso

Primero debemos colocar el pdf en el que queremos aplicar el OCR en la carpeta pdf.

Después ejecutar el programa con el siguiente comando:
```sh
python3 lector_pdf.py
```

El programa nos listara los archivos dentro de la carpeta pdf.
Seleccionamos el archivo.

Seleccionamos el idioma en el que se encuentra el archivo.

Nos mostrará el contenido de cada pagina del PDF.