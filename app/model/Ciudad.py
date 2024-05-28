from database.conexion import conexionBD

class BDCiudad:
    def __init__(self) -> None:
        pass

    def listarCiudades(self):
        conexion = conexionBD().conectar()

        consulta = "SELECT nombre FROM ciudad"  # Modificar la consulta para seleccionar los nombres de las ciudades

        cursor = conexion.cursor()
        cursor.execute(consulta)

        resultados = cursor.fetchall()

        conexion.close()

        ciudades = []

        for resultado in resultados:
            nombre_ciudad = resultado[0]  # El nombre de la ciudad está en la posición 0 de la tupla
            ciudades.append(nombre_ciudad)

        return ciudades
