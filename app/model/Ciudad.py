from database.conexion import conexionBD

class BDCiudad:
    def __init__(self) -> None:
        pass

    def listarCiudad(self):
        conexion = conexionBD().conectar()

        consulta = "SELECT id_ciudad FROM ciudad"

        cursor = conexion.cursor()
        cursor.execute(consulta)

        resultados = cursor.fetchall()

        conexion.close()

        ciudades = []

        for resultado in resultados:
            id_ciudad = resultado
            ciudades.append(id_ciudad)

        return ciudades