import os
import cv2
from pdf2image import convert_from_path
from pytesseract import image_to_string
from preprocessing import Preprocessing

class PDFProcessor:
    def __init__(self, input_dir, file_types=['pdf']):
        self.input_dir = input_dir
        self.file_types = file_types
        self.files = self._get_files()

    def _get_files(self):
        files = []
        for file in os.listdir(self.input_dir):
            if any(file.lower().endswith(ft) for ft in self.file_types):
                files.append(file)
            else:
                print(f"El archivo {file} no es compatible y no será procesado.")
        return files

    def process_files(self):
        texts = []
        preprocessing = Preprocessing()  # Instancia de la clase Preprocessing
        for file in self.files:
            print(f"Procesando archivo: {file}")
            file_path = os.path.join(self.input_dir, file)
            if file.lower().endswith('pdf'):
                images = convert_from_path(file_path)
            elif file.lower().endswith('png'):
                images = [cv2.imread(file_path)]
            
            for image in images:
                grayscale_image = preprocessing.convert_to_grayscale(image)
                text = image_to_string(grayscale_image)
                texts.append(text)
        return " ".join(texts)
