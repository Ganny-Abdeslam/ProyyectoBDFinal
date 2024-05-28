from database.conexion import conexionBD

class Factura:
    def __init__(self, fecha, total, id_cliente, vendedorCedula) -> None:
        self.fecha = fecha
        self.total = total
        self.id_cliente = id_cliente
        self.vendedorCedula = vendedorCedula

    def agregarFactura(self):
        conexion = conexionBD().conectar()

        consulta = "INSERT INTO factura (fecha, total, id_cliente, vendedor_cedula) VALUES (%s, %s, %s, %s)"
        datos = (self.fecha, self.total, self.id_cliente, self.vendedorCedula)

        cursor = conexion.cursor()
        cursor.execute(consulta, datos)

        conexion.commit()
        conexion.close()

        print("Se agregó correctamente la factura")

class BDFactura:

    def listarFacturas(self):
        conexion = conexionBD().conectar()

        consulta = "SELECT * FROM factura"

        cursor = conexion.cursor()
        cursor.execute(consulta)

        resultados = cursor.fetchall()

        conexion.close()

        facturas = []

        for resultado in resultados:
            id_factura, fecha, total, id_cliente, vendedorCedula = resultado
            factura = Factura(id_factura, fecha, total, id_cliente, vendedorCedula)
            facturas.append(factura)

        return facturas

    def buscarFacturaPorId(self, id_factura):
        conexion = conexionBD().conectar()

        consulta = "SELECT * FROM factura WHERE id_factura = %s"

        cursor = conexion.cursor()
        cursor.execute(consulta, (id_factura,))

        resultado = cursor.fetchone()

        conexion.close()

        if not resultado:
            return None

        id_factura, fecha, total, id_cliente, vendedorCedula = resultado
        factura = Factura(fecha, total, id_cliente, vendedorCedula)

        return factura

    def eliminarFactura(self, id_factura):
        conexion = conexionBD().conectar()

        cursor = conexion.cursor()

        consulta = "DELETE FROM factura WHERE id_factura = %s"
        datos = (id_factura)

        cursor.execute(consulta, datos)

        conexion.commit()

        conexion.close()

        print("Se eliminó correctamente la factura")
