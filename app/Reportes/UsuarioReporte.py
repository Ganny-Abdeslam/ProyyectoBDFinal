import os
import json
from pyreportjasper import PyReportJasper
from model.Usuario import BDUsuario

class UsuarioReport:

    def __init__(self) -> None:
        self.usuario = BDUsuario()

    def reporte(self):
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))

            lista_usuarios = self.usuario.listarUsuarios()

            data = {
                'usuarios': lista_usuarios
            }
            
            json_file_path = os.path.join(script_dir, 'Usuario.json')
            with open(json_file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

            input_file = os.path.join(script_dir, 'Usuario.jrxml')
            out_file = os.path.join(script_dir, 'ReporteUsuario')

            conn = {
                'driver': 'json',
                'data_file': json_file_path,
                'json_query': 'usuarios'
            }

            pyreportjasper = PyReportJasper()
            pyreportjasper.config(
                input_file=input_file,
                output_file=out_file,
                output_formats=['pdf'],
                locale='pl_PL',
                db_connection=conn
            )

            pyreportjasper.process_report()

            print("=" * 30)
            print("Reporte generado exitosamente")
            print("=" * 30)
        except Exception as e:
            print("Error al generar el reporte:", str(e))