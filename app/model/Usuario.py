from database.conexion import conexionBD

class Usuario:
    def __init__(self, cedula, primerNombre, segundoNombre, primerApellido, segundoApellido, fechaNacimiento, telefono, direccion, email, salario, username, password, idSucursal) -> None:
        self.cedula = cedula
        self.primerNombre = primerNombre
        self.segundoNombre = segundoNombre
        self.primerApellido = primerApellido
        self.segundoApellido = segundoApellido
        self.fechaNacimiento = fechaNacimiento
        self.telefono = telefono
        self.direccion = direccion
        self.email = email
        self.salario = salario
        self.username = username
        self.password = password
        self.idSucursal = idSucursal

    def agregarUsuario(self):
        conexion = conexionBD().conectar()

        consulta = "INSERT INTO usuario (cedula, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, fecha_nacimiento, telefono, direccion, email, salario, username, password, id_sucursal) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        datos = (self.cedula, self.primerNombre, self.segundoNombre, self.primerApellido, self.segundoApellido, self.fechaNacimiento, self.telefono, self.direccion, self.email, self.salario, self.username, self.password, self.idSucursal)

        cursor = conexion.cursor()
        cursor.execute(consulta, datos)

        conexion.commit()
        conexion.close()

        print("Se agregó correctamente el usuario")

    def listarUsuarios(self):
        conexion = conexionBD().conectar()

        consulta = "SELECT * FROM usuario"

        cursor = conexion.cursor()
        cursor.execute(consulta)

        resultados = cursor.fetchall()

        conexion.close()

        usuarios = []

        for resultado in resultados:
            cedula, primerNombre, segundoNombre, primerApellido, segundoApellido, fechaNacimiento, telefono, direccion, email, salario, username, password, idSucursal = resultado
            usuario = Usuario(cedula, primerNombre, segundoNombre, primerApellido, segundoApellido, fechaNacimiento, telefono, direccion, email, salario, username, password, idSucursal)
            usuarios.append(usuario)

        return usuarios

    def buscarUsuarioPorCedula(self, cedula):
        conexion = conexionBD().conectar()

        consulta = "SELECT * FROM usuario WHERE cedula = %s"

        cursor = conexion.cursor()
        cursor.execute(consulta, (cedula,))

        resultado = cursor.fetchone()

        conexion.close()

        if not resultado:
            return None

        cedula, primerNombre, segundoNombre, primerApellido, segundoApellido, fechaNacimiento, telefono, direccion, email, salario, username, password, idSucursal = resultado
        usuario = Usuario(cedula, primerNombre, segundoNombre, primerApellido, segundoApellido, fechaNacimiento, telefono, direccion, email, salario, username, password, idSucursal)

        return usuario
