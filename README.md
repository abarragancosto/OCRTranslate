# OCRTranslate
##Instalación
Para la instalación de los paquetes necesarios, únicamente hay que hacer 
````
pip install -r requirements.txt
````

##Uso
Variables de entrada:
--input_dir: Con esta variable se permite seleccionar el directorio donde se encuentran los ficheros de entrada. Por defecto se selecciona un directorio llamado "PDF" que se debe encontrar en el mismo directorio donde se encuentre el código ejecutado.

--file_types: Con esta variable se puede seleccionar el tipo de archivos a procesar entre "png" y "pdf". Por defecto se seleccionarán archivos pdf.

--output_format: Con esta variable se podrá elegir la extensión del fichero de salida. Se puede elegir entre txt o pdf. Por defecto es txt.

--output_dir: Con esta variable se podrá elegir el directorio donde se almacenará el fichero con la traducción. Por defecto será el directorio donde se ejecuta el programa.

--output_filename: Con esta variable se podrá configurar cual es el nombre del fichero que contendrá la traducción. Por defecto el fichero se llamará "output"

Ejemplos de uso 

Con todas las configuraciones por defecto:
````
python main.py
````

Si se desea tener el fichero con las traducciones en pdf:
````
python main.py --output_format=pdf
````

Si se desea introducir fotos:
````
python main.py --file_types=png