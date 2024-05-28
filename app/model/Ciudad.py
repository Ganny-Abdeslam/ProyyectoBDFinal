from database.conexion import conexionBD

class BDCiudad:
    def __init__(self) -> None:
        pass

    def listarCiudades(self):
        conexion = conexionBD().conectar()

        consulta = "SELECT nombre FROM ciudad"

        cursor = conexion.cursor()
        cursor.execute(consulta)

        resultados = cursor.fetchall()

        conexion.close()

        ciudades = ['Seleccionar']

        for resultado in resultados:
            nombre_ciudad = resultado[0]
            ciudades.append(nombre_ciudad)

        return ciudades
