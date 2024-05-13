from database.conexion import conexionBD

class Cliente:
    def __init__(self, nombre, direccion, telefono, email, ciudad_id) -> None:
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.ciudad_id = ciudad_id

    def agregarCliente(self):
        conexion = conexionBD().conectar()

        consulta = "INSERT INTO cliente (nombre, direccion, telefono, email, ciudad_id_ciudad) VALUES (%s, %s, %s, %s, %s)"
        datos = (self.nombre, self.direccion, self.telefono, self.email, self.ciudad_id)

        cursor = conexion.cursor()
        cursor.execute(consulta, datos)

        conexion.commit()
        conexion.close()

        print(f"Se agregó correctamente el cliente: {self.nombre}")

    def listar(self):
        conexion = conexionBD().conectar()

        consulta = "SELECT * FROM cliente"

        cursor = conexion.cursor()
        cursor.execute(consulta)

        resultados = cursor.fetchall()

        conexion.close()

        clientes = []

        for resultado in resultados:
            id_cliente, nombre, direccion, telefono, email, ciudad_id = resultado
            cliente = Cliente(id_cliente, nombre, direccion, telefono, email, ciudad_id)
            clientes.append(cliente)

        return clientes
    
    def listarCedula(self, cedula):
        conexion = conexionBD().conectar()

        consulta = "SELECT * FROM cliente WHERE cedula = %s"

        cursor = conexion.cursor()
        cursor.execute(consulta, (cedula,))

        resultado = cursor.fetchone()

        conexion.close()

        if not resultado:
            return None

        id_cliente, nombre, direccion, telefono, email, ciudad_id = resultado
        cliente = Cliente(id_cliente, nombre, direccion, telefono, email, ciudad_id)
        
        return cliente