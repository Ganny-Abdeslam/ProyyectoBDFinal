from database.conexion import conexionBD

class Sucursal:
    def __init__(self, direccion, telefono, email, jefeCedula, idCiudad) -> None:
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.jefeCedula = jefeCedula
        self.idCiudad = idCiudad

    def agregarSucursal(self):
        conexion = conexionBD().conectar()

        consulta = "INSERT INTO sucursal (direccion, telefono, email, jefe_cedula, id_ciudad) VALUES (%s, %s, %s, %s, %s)"
        datos = (self.direccion, self.telefono, self.email, self.jefeCedula, self.idCiudad)

        cursor = conexion.cursor()
        cursor.execute(consulta, datos)

        conexion.commit()
        conexion.close()

        print("Se agregó correctamente la sucursal")

    def listarSucursales(self):
        conexion = conexionBD().conectar()

        consulta = "SELECT * FROM sucursal"

        cursor = conexion.cursor()
        cursor.execute(consulta)

        resultados = cursor.fetchall()

        conexion.close()

        sucursales = []

        for resultado in resultados:
            idSucursal, direccion, telefono, email, jefeCedula, idCiudad = resultado
            sucursal = Sucursal(direccion, telefono, email, jefeCedula, idCiudad)
            sucursales.append(sucursal)

        return sucursales

    def buscarSucursalPorId(self, idSucursal):
        conexion = conexionBD().conectar()

        consulta = "SELECT * FROM sucursal WHERE id_sucursal = %s"

        cursor = conexion.cursor()
        cursor.execute(consulta, (idSucursal,))

        resultado = cursor.fetchone()

        conexion.close()

        if not resultado:
            return None

        idSucursal, direccion, telefono, email, jefeCedula, idCiudad = resultado
        sucursal = Sucursal(direccion, telefono, email, jefeCedula, idCiudad)

        return sucursal