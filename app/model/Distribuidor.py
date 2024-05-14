from database.conexion import conexionBD

class Distribuidor:
    def __init__(self, placaVehiculo, cedula) -> None:
        self.placaVehiculo = placaVehiculo
        self.cedula = cedula

    def agregarDistribuidor(self):
        conexion = conexionBD().conectar()

        consulta = "INSERT INTO distribuidor (placa_vehiculo, cedula) VALUES (%s, %s)"
        datos = (self.placaVehiculo, self.cedula)

        cursor = conexion.cursor()
        cursor.execute(consulta, datos)

        conexion.commit()
        conexion.close()

        print("Se agregó correctamente el distribuidor")

    def listarDistribuidores(self):
        conexion = conexionBD().conectar()

        consulta = "SELECT * FROM distribuidor"

        cursor = conexion.cursor()
        cursor.execute(consulta)

        resultados = cursor.fetchall()

        conexion.close()

        distribuidores = []

        for resultado in resultados:
            placaVehiculo, cedula = resultado
            distribuidor = Distribuidor(placaVehiculo, cedula)
            distribuidores.append(distribuidor)

        return distribuidores

    def buscarDistribuidorPorCedula(self, cedula):
        conexion = conexionBD().conectar()

        consulta = "SELECT * FROM distribuidor WHERE cedula = %s"

        cursor = conexion.cursor()
        cursor.execute(consulta, (cedula,))

        resultado = cursor.fetchone()

        conexion.close()

        if not resultado:
            return None

        placaVehiculo, cedula = resultado
        distribuidor = Distribuidor(placaVehiculo, cedula)

        return distribuidor
