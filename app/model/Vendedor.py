from database.conexion import conexionBD

class Vendedor:
    def __init__(self, comisionVenta, cedula) -> None:
        self.comisionVenta = comisionVenta
        self.cedula = cedula

    def agregarVendedor(self):
        conexion = conexionBD().conectar()

        consulta = "INSERT INTO vendedor (comision_venta, cedula) VALUES (%s, %s)"
        datos = (self.comisionVenta, self.cedula)

        cursor = conexion.cursor()
        cursor.execute(consulta, datos)

        conexion.commit()
        conexion.close()

        print("Se agregó correctamente el vendedor")

    def listarVendedores(self):
        conexion = conexionBD().conectar()

        consulta = "SELECT * FROM vendedor"

        cursor = conexion.cursor()
        cursor.execute(consulta)

        resultados = cursor.fetchall()

        conexion.close()

        vendedores = []

        for resultado in resultados:
            comisionVenta, cedula = resultado
            vendedor = Vendedor(comisionVenta, cedula)
            vendedores.append(vendedor)

        return vendedores

    def buscarVendedorPorCedula(self, cedula):
        conexion = conexionBD().conectar()

        consulta = "SELECT * FROM vendedor WHERE cedula = %s"

        cursor = conexion.cursor()
        cursor.execute(consulta, (cedula,))

        resultado = cursor.fetchone()

        conexion.close()

        if not resultado:
            return None

        comisionVenta, cedula = resultado
        vendedor = Vendedor(comisionVenta, cedula)

        return vendedor
