from database.conexion import conexionBD

class Cliente:
    def __init__(self, nombre, direccion, telefono, email, ciudad_id) -> None:
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.ciudad_id = ciudad_id

    def addID(self, id):
        self.id = id

    def to_dict(self):
        return {
            "id_cliente": self.id,
            "nombre": self.nombre,
            "direccion": self.direccion,
            "telefono": self.telefono,
            "email": self.email,
            "ciudad_id": self.ciudad_id
        }

    def agregarCliente(self):
        conexion = conexionBD().conectar()

        consulta = "INSERT INTO cliente (nombre, direccion, telefono, email, ciudad_id_ciudad) VALUES (%s, %s, %s, %s, %s)"
        datos = (self.nombre, self.direccion, self.telefono, self.email, self.ciudad_id)

        cursor = conexion.cursor()
        cursor.execute(consulta, datos)

        conexion.commit()
        conexion.close()

        print(f"Se agregó correctamente el cliente: {self.nombre}")

    def updateCliente(self):
        conexion = conexionBD().conectar()

        consulta = "UPDATE cliente SET direccion = %s, telefono = %s, email = %s, ciudad_id_ciudad = %s WHERE nombre = %s"
        datos = (self.direccion, self.telefono, self.email, self.ciudad_id, self.nombre)

        cursor = conexion.cursor()
        cursor.execute(consulta, datos)

        conexion.commit()
        conexion.close()

        print(f"Se actualizó correctamente el cliente: {self.nombre}")


class BDCliente:

    def listar(self):
        conexion = conexionBD().conectar()

        consulta = "SELECT id_cliente, cl.nombre, direccion, telefono, email, c.nombre FROM cliente cl INNER JOIN ciudad c ON (c.id_ciudad = cl.ciudad_id_ciudad)"

        cursor = conexion.cursor()
        cursor.execute(consulta)

        resultados = cursor.fetchall()

        conexion.close()

        clientes = []

        for resultado in resultados:
            id_cliente, nombre, direccion, telefono, email, ciudad_id = resultado
            cliente = Cliente(nombre, direccion, telefono, email, ciudad_id)
            cliente.addID(id_cliente)
            clientes.append(cliente.to_dict())

        return clientes
    
    def listarNombre(self, nombre):
        conexion = conexionBD().conectar()

        consulta = "SELECT direccion, telefono, email, ciudad_id_ciudad FROM cliente WHERE nombre = %s"

        cursor = conexion.cursor()
        cursor.execute(consulta, (nombre,))

        resultado = cursor.fetchone()

        conexion.close()

        if not resultado:
            return None

        direccion, telefono, email, ciudad_id_ciudad = resultado
        cliente = Cliente(nombre, direccion, telefono, email, ciudad_id_ciudad)
        
        return cliente

    def eliminarCliente(self, id_cliente):
        conexion = conexionBD().conectar()

        cursor = conexion.cursor()

        consulta = "DELETE FROM cliente WHERE id_cliente = %s"
        datos = (id_cliente)

        cursor.execute(consulta, datos)

        conexion.commit()

        conexion.close()

        print("Se eliminó correctamente el cliente")