import os
import json
from pyreportjasper import PyReportJasper

def jusper(a, b, c):
    try:
        # Crear el diccionario con los datos proporcionados
        data1 = {
            'data': [{
                'titulo': a,
                'dato2': b,
                'dato3': c
            }]
        }
        
        # Convertir el diccionario a una cadena JSON
        data2 = json.dumps(data1, ensure_ascii=False)

        # Escribir la cadena JSON en un archivo
        with open('Sucursal.json', "w", encoding="utf-8") as file:
            file.write(data2)

        # Definir archivos de entrada y salida para el reporte
        input_file = 'Sucursal.jrxml'
        out_file = 'ReporteSucursal'
        
        # Configuración de la conexión JSON
        conn = {
            'driver': 'json',
            'data_file': 'Sucursal.json',
            'json_query': 'data'
        }

        # Configurar PyReportJasper
        pyreportjasper = PyReportJasper()
        pyreportjasper.config(
            input_file=input_file,
            output_file=out_file,
            output_formats=['pdf'],
            locale='pl_PL',
            db_connection=conn
        )

        # Generar el reporte
        pyreportjasper.process_report()

        print("=" * 30)
        print("Reporte generado exitosamente")
        print("=" * 30)
    except Exception as e:
        print("Error al generar el reporte:", str(e))

# Llamar a la función con los datos de ejemplo
jusper("Titulo Reporte Sucursal", "dato2", "dato3")
