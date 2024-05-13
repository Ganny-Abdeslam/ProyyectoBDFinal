from database.conexion import conexionBD

class Factura:
    def __init__(self, fecha, total, idCliente, vendedorCedula) -> None:
        self.fecha = fecha
        self.total = total
        self.idCliente = idCliente
        self.vendedorCedula = vendedorCedula

    def agregarFactura(self):
        conexion = conexionBD().conectar()

        consulta = "INSERT INTO factura (fecha, total, id_cliente, vendedor_cedula) VALUES (%s, %s, %s, %s)"
        datos = (self.fecha, self.total, self.idCliente, self.vendedorCedula)

        cursor = conexion.cursor()
        cursor.execute(consulta, datos)

        conexion.commit()
        conexion.close()

        print("Se agregó correctamente la factura")

    def listarFacturas(self):
        conexion = conexionBD().conectar()

        consulta = "SELECT * FROM factura"

        cursor = conexion.cursor()
        cursor.execute(consulta)

        resultados = cursor.fetchall()

        conexion.close()

        facturas = []

        for resultado in resultados:
            idFactura, fecha, total, idCliente, vendedorCedula = resultado
            factura = Factura(fecha, total, idCliente, vendedorCedula)
            facturas.append(factura)

        return facturas

    def buscarFacturaPorId(self, idFactura):
        conexion = conexionBD().conectar()

        consulta = "SELECT * FROM factura WHERE id_factura = %s"

        cursor = conexion.cursor()
        cursor.execute(consulta, (idFactura,))

        resultado = cursor.fetchone()

        conexion.close()

        if not resultado:
            return None

        idFactura, fecha, total, idCliente, vendedorCedula = resultado
        factura = Factura(fecha, total, idCliente, vendedorCedula)

        return factura
