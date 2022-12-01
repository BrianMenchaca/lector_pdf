import pytesseract
import os
import convertir_pdf_a_jpg as cpdf
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

def main():
    dir = './pdf'

    contenido = os.listdir(dir)
    pdfs = []
    print("¿Que archivo desea revisar?:\n")
    i = 0
    for fichero in contenido:
        if os.path.isfile(os.path.join(dir, fichero)) and fichero.endswith('.pdf'):
            print(str(i) + ' - ' + fichero)
            i += 1
            pdfs.append(fichero)

    while True:
        select = int(input("Opcion: "))
        if select >= 0 and select < i:
            break
    
    cpdf.convertir_pdf(pdfs[select])

    dir_img = "./img/" + pdfs[select][:-4]
    contenido = os.listdir(dir_img)
    imagenes = []
    print("\nEn que idioma se encuentra el pdf:")
    language = obtener_lenguajes()

    for fichero in contenido:
        print("\n" + "*" * 10 + " " + fichero + " " + "*" * 10 + "\n")
        leer_imagen(dir_img + "/" + fichero, language)


def leer_imagen(filename, language):
    img = Image.open(filename)  # Abre la imagen con pillow
    img.load()
    text = pytesseract.image_to_string(img, lang=language)  # Extrae el texto de la imagen
    print(text[:-2])


def obtener_lenguajes():
    i = 0
    for language in pytesseract.get_languages():
        print(str(i) + ": " + language)
        i += 1

    while True:
        option = int(input("Opcion: "))
        if option >= 0 and option < i:
            break
    return pytesseract.get_languages()[option]


if __name__ == "__main__":
    main()
