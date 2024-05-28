from database.conexion import conexionBD

class Sucursal:
    def __init__(self, direccion, telefono, email, jefeCedula, idCiudad) -> None:
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.jefeCedula = jefeCedula
        self.idCiudad = idCiudad

    def addId(self, id_sucursal):
        self.id_sucursal = id_sucursal

    def to_dict(self):
        return {
            'id_sucursal': self.id_sucursal,
            'direccion': self.direccion,
            'telefono': self.telefono,
            'email': self.email,
            'jefeCedula': self.jefeCedula,
            'idCiudad': self.idCiudad
        }

    def agregarSucursal(self):
        conexion = conexionBD().conectar()

        cursor = conexion.cursor()

        consulta_count = "SELECT COUNT(*) FROM sucursal"
        cursor.execute(consulta_count)
        count_result = cursor.fetchone()
        count_sucursales = count_result[0] if count_result else 0

        new_id_sucursal = count_sucursales + 1

        consulta = "INSERT INTO sucursal (id_sucursal, direccion, telefono, email, jefe_cedula, id_ciudad) VALUES (%s, %s, %s, %s, %s, %s)"
        datos = (new_id_sucursal, self.direccion, self.telefono, self.email, self.jefeCedula, self.idCiudad)

        cursor.execute(consulta, datos)

        conexion.commit()

        conexion.close()

        print("Se agregó correctamente la sucursal")

class BDSucursal:

    def __init__(self) -> None:
        pass

    def listarSucursales(self):
        conexion = conexionBD().conectar()

        consulta = "SELECT id_sucursal, direccion, telefono, email, jefe_cedula, id_ciudad FROM sucursal"

        cursor = conexion.cursor()
        cursor.execute(consulta)

        resultados = cursor.fetchall()

        conexion.close()

        sucursales = []

        for resultado in resultados:
            id_sucursal, direccion, telefono, email, jefeCedula, idCiudad = resultado
            sucursal = Sucursal(direccion, telefono, email, jefeCedula, idCiudad)
            sucursal.addId(id_sucursal)
            sucursales.append(sucursal.to_dict())

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
