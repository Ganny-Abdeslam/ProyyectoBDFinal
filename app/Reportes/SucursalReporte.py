import os
import json
from pyreportjasper import PyReportJasper
from model.Sucursal import BDSucursal

class SucursalReport:

    def __init__(self) -> None:
        self.sucursal = BDSucursal()

    def reporte(self):
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))

            # Obtener la lista de sucursales como diccionarios
            lista_sucursales = self.sucursal.listarSucursales()

            # Preparar los datos en un diccionario
            data = {
                'sucursales': lista_sucursales
            }
            
            # Convertir los datos a JSON y escribir en el archivo
            json_file_path = os.path.join(script_dir, 'Sucursal.json')
            with open(json_file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

            # Configurar los archivos de entrada y salida para el reporte
            input_file = os.path.join(script_dir, 'Sucursal.jrxml')
            out_file = os.path.join(script_dir, 'ReporteSucursal')

            # Configuración de la conexión JSON
            conn = {
                'driver': 'json',
                'data_file': json_file_path,
                'json_query': 'sucursales'
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