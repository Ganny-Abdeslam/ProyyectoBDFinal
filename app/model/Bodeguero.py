from database.conexion import conexionBD

class Bodeguero:
    def __init__(self, cedula, jefeCedula=None) -> None:
        self.cedula = cedula
        self.jefeCedula = jefeCedula

    def agregarBodeguero(self):
        conexion = conexionBD().conectar()

        consulta = "INSERT INTO bodeguero (cedula, jefe_cedula) VALUES (%s, %s)"
        datos = (self.cedula, self.jefeCedula)

        cursor = conexion.cursor()
        cursor.execute(consulta, datos)

        conexion.commit()
        conexion.close()

        print("Se agregó correctamente el bodeguero")

    def listarBodegueros(self):
        conexion = conexionBD().conectar()

        consulta = "SELECT * FROM bodeguero"

        cursor = conexion.cursor()
        cursor.execute(consulta)

        resultados = cursor.fetchall()

        conexion.close()

        bodegueros = []

        for resultado in resultados:
            cedula, jefeCedula = resultado
            bodeguero = Bodeguero(cedula, jefeCedula)
            bodegueros.append(bodeguero)

        return bodegueros

    def buscarBodegueroPorCedula(self, cedula):
        conexion = conexionBD().conectar()

        consulta = "SELECT * FROM bodeguero WHERE cedula = %s"

        cursor = conexion.cursor()
        cursor.execute(consulta, (cedula,))

        resultado = cursor.fetchone()

        conexion.close()

        if not resultado:
            return None

        cedula, jefeCedula = resultado
        bodeguero = Bodeguero(cedula, jefeCedula)

        return bodeguero
