# Lector de PDF

Para correr el programa debes seguir las siguientes instrucciones en la terminal:

## Instalación:

### Linux

1- Ejecutar los siguiente comandos para actualizar los indices:
```sh
sudo apt-get update
sudo apt-get upgrade
```
2- Instalar Poppler
```sh
sudo apt install poppler-utils
```
3- Verificar que Poppler esta instalado correctamente:
```sh
pdftocairo -v
```

#### Crear y activar ambiente virtual (Linux)

Dentro de la carpeta donde se clonará el programa

```sh
git clone https://github.com/BrianMenchaca/lector_pdf.git
cd lector_pdf
python -m venv env
source env/bin/activate
```

### Windows

#### Instalación Tesseract

Descargar el instalador de Tesseract desde el siguiente enlace, elegir la opción de 32 o 64 bit según la versión de tu Windows:

[Enlace de página](https://github.com/UB-Mannheim/tesseract/wiki)

Iniciar el instalador y dar siguiente hasta que nos muestre:

![](https://miro.medium.com/max/640/1*9G5-tYLWNFZCXAv0oy5-RA.png)

Aca marcamos la opción "Math / equation..." y los idiomas que se usarán para la lectura del pdf dentro de la casilla "Adittional language data (download)".

![](https://miro.medium.com/max/640/1*ZzSChHIIgvamts0qrlC1BA.png)

En ese punto debemos escoger el directorio donde se instalará el programa. La ruta se usará mas adelante.

Damos siguiente y finalizar.

Una vez finalizado, debemos añadir una linea de codigo debajo del import de los modulos:

```sh
pytesseract.pytesseract.tesseract_cmd = r'<path>'
```
Reemplazar <path> por la ruta donde instalamos tesseract, añadiendo al final de la ruta **tesseract**.
Ejemplo:

```sh
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\nombre-usuario\AppData\Local\Tesseract-OCR\tesseract'
```

#### Añadiendo otros idiomas

En caso de que necesitemos añadir otros idiomas, además de los que añadimos al momento de instalar, podemos ir a la pagina:

[Página para descargar idiomas](https://tesseract-ocr.github.io/tessdoc/Data-Files.html)

Descargamos los idiomas que necesitemos, los copiamos y los pegamos en la carpeta **tessdata**, que se encuentra dentro de la carpeta donde se instalo tesseract.

#### Crear y activar ambiente virtual (Windows)

Dentro de la carpeta donde se clonará el programa

```sh
git clone https://github.com/BrianMenchaca/lector_pdf.git
cd lector_pdf
python -m venv env
.\env\Scripts\activate
```

### Instalar los modulos necesarios para el programa

```sh
pip install -r requirements.txt
```

## Instrucciones de uso

Crear carpetas img y pdf:
```sh
mkdir img pdf
```

Colocar el pdf que queremos aplicar el OCR en la carpeta pdf.

Después ejecutar el programa con el siguiente comando:
```sh
python lector_pdf.py
```

El programa nos listara los archivos dentro de la carpeta pdf.
Seleccionamos el archivo.

Seleccionamos el idioma en el que se encuentra el archivo.

Nos mostrará el contenido de cada pagina del PDF.