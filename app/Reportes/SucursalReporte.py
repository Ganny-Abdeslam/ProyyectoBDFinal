import os
import json
from pyreportjasper import PyReportJasper

def jasper(a, b, c):
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))

        data1 = {
            'data': [{
                'titulo': a,
                'dato2': b,
                'dato3': c
            }]
        }
        
        data2 = json.dumps(data1, ensure_ascii=False)

        json_file_path = os.path.join(script_dir, 'Sucursal.json')

        with open(json_file_path, "w", encoding="utf-8") as file:
            file.write(data2)

        input_file = os.path.join(script_dir, 'Sucursal.jrxml')
        out_file = os.path.join(script_dir, 'ReporteSucursal')

        conn = {
            'driver': 'json',
            'data_file': json_file_path,
            'json_query': 'data'
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

jasper("Titulo Reporte Prueba Sucursal", "dato2", "dato3")
