import pytesseract
import os
import convertir_pdf_a_jpg as cpdf
import shutil
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


def main():

    dir = './pdf'
    dir_procesados = './procesados'
    dir_img = "./img"
    dir_txt = "./txt"

    # Creacion de carpetas que utiliza el programa

    if (os.path.exists(dir_img) == False):
        os.mkdir(dir_img)

    if (os.path.exists(dir) == False):
        os.mkdir(dir)

    if (os.path.exists(dir_txt) == False):
        os.mkdir(dir_txt)

    if (os.path.exists(dir_procesados) == False):
        os.mkdir(dir_procesados)

    contenido_pdf = os.listdir(dir)

    # Verifica que haya archivos en la carpeta pdf

    if len(contenido_pdf) == 0:
        print("La carpeta pdf se encuentra vacía")
        return

    language = obtener_lenguaje()

    for pdf in contenido_pdf:
        if os.path.isfile(os.path.join(dir, pdf)) and pdf.endswith('.pdf'):
            print("Se leyo el archivo: " + pdf)
            cpdf.convertir_pdf(pdf)
            nombre_txt = pdf[:-4] + ".txt"  # Nombre de la salida en formato .txt

            dir_img_pdf = dir_img + "/" + pdf[:-4]

            # Lista el contenido de la carpeta donde se crearon las imagenes del pdf
            contenido_img = os.listdir(dir_img_pdf)

            primera_lectura = True  # Bandera que se utiliza para crear un archivo vacio para después escribir

            for imagen in contenido_img:
                texto = leer_imagen(dir_img_pdf + "/" + imagen, language)

                if primera_lectura:
                    with open(dir_txt + "/" + nombre_txt, mode='w') as f:
                        f.write(texto)
                    primera_lectura = False
                else:
                    with open(dir_txt + "/" + nombre_txt, mode='a') as f:
                        f.write(texto)

            shutil.move(dir + '/' + pdf, dir_procesados + "/" + pdf)


def leer_imagen(filename, language):
    img = Image.open(filename)  # Abre la imagen con pillow
    img.load()
    text = pytesseract.image_to_string(
        img, lang=language)  # Extrae el texto de la imagen
    return (text[:-2])


def obtener_lenguaje():
    print("\nEn que idioma se encuentran los pdf:")
    i = 0
    for language in pytesseract.get_languages():
        print(str(i) + ": " + language)
        i += 1

    while True:
        option = int(input("Opcion: "))
        if option >= 0 and option < i:
            break
    print('')
    return pytesseract.get_languages()[option]


if __name__ == "__main__":
    main()
