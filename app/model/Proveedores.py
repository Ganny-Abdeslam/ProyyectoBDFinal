from database.conexion import conexionBD

class Proveedor:
    def __init__(self, nombre, direccion, email, telefono) -> None:
        self.nombre = nombre
        self.direccion = direccion
        self.email = email
        self.telefono = telefono

    def agregarProveedor(self):
        conexion = conexionBD().conectar()

        consulta = "INSERT INTO proveedor (nombre, direccion, email, telefono) VALUES (%s, %s, %s, %s)"
        datos = (self.nombre, self.direccion, self.email, self.telefono)

        cursor = conexion.cursor()
        cursor.execute(consulta, datos)

        conexion.commit()
        conexion.close()

        print("Se agregó correctamente el proveedor")

    def listarProveedores(self):
        conexion = conexionBD().conectar()

        consulta = "SELECT * FROM proveedor"

        cursor = conexion.cursor()
        cursor.execute(consulta)

        resultados = cursor.fetchall()

        conexion.close()

        proveedores = []

        for resultado in resultados:
            idProveedor, nombre, direccion, email, telefono = resultado
            proveedor = Proveedor(nombre, direccion, email, telefono)
            proveedores.append(proveedor)

        return proveedores

    def buscarProveedorPorId(self, idProveedor):
        conexion = conexionBD().conectar()

        consulta = "SELECT * FROM proveedor WHERE id_proveedor = %s"

        cursor = conexion.cursor()
        cursor.execute(consulta, (idProveedor,))

        resultado = cursor.fetchone()

        conexion.close()

        if not resultado:
            return None

        idProveedor, nombre, direccion, email, telefono = resultado
        proveedor = Proveedor(nombre, direccion, email, telefono)

        return proveedor
