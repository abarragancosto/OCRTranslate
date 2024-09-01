import argparse
from pdf_processor import PDFProcessor
from text_translator import TextTranslator
from text_corrector import TextCorrector
from output_manager import OutputManager
import warnings
warnings.filterwarnings("ignore")

def main(input_dir='PDF', file_types=['pdf'], output_format='txt', output_dir=None, output_filename="output"):
    if output_dir is None:
        output_dir = input_dir
    
    processor = PDFProcessor(input_dir, file_types)
    raw_text = processor.process_files()

    translator = TextTranslator()
    translated_text = translator.translate_text(raw_text)

    corrector = TextCorrector()
    corrected_text = corrector.correct_text(translated_text)

    output_manager = OutputManager(output_dir, output_format)
    output_manager.save_output(corrected_text, filename=output_filename)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Procesador de archivos PDF/PNG para extraer, traducir y corregir texto.")
    parser.add_argument("--input_dir", type=str, default="PDF", help="Directorio de entrada donde se encuentran los archivos PDF/PNG.")
    parser.add_argument("--file_types", nargs='+', default=["pdf"], help="Tipos de archivos a procesar (por defecto es PDF).")
    parser.add_argument("--output_format", type=str, default="txt", choices=['txt', 'pdf'], help="Formato de salida (por defecto es txt).")
    parser.add_argument("--output_dir", type=str, help="Directorio de salida para el archivo final.")
    parser.add_argument("--output_filename", type=str, default="output", help="Nombre del archivo de salida (sin extensión).")

    args = parser.parse_args()

    main(
        input_dir=args.input_dir,
        file_types=args.file_types,
        output_format=args.output_format,
        output_dir=args.output_dir,
        output_filename=args.output_filename
    )
