from database.conexion import conexionBD

class FacturaDetalle:
    def __init__(self, idFactura, idProducto, cantidad, precio) -> None:
        self.idFactura = idFactura
        self.idProducto = idProducto
        self.cantidad = cantidad
        self.precio = precio

    def agregarDetalleFactura(self):
        conexion = conexionBD().conectar()

        consulta = "INSERT INTO factura_detalle (id_factura, id_producto, cantidad, precio) VALUES (%s, %s, %s, %s)"
        datos = (self.idFactura, self.idProducto, self.cantidad, self.precio)

        cursor = conexion.cursor()
        cursor.execute(consulta, datos)

        conexion.commit()
        conexion.close()

        print("Se agregó correctamente el detalle de la factura")

    def listarDetallesFactura(self):
        conexion = conexionBD().conectar()

        consulta = "SELECT * FROM factura_detalle"

        cursor = conexion.cursor()
        cursor.execute(consulta)

        resultados = cursor.fetchall()

        conexion.close()

        detallesFactura = []

        for resultado in resultados:
            idFactura, idProducto, cantidad, precio = resultado
            detalleFactura = FacturaDetalle(idFactura, idProducto, cantidad, precio)
            detallesFactura.append(detalleFactura)

        return detallesFactura

    def buscarDetalleFacturaPorIds(self, idFactura):
        conexion = conexionBD().conectar()

        consulta = "SELECT * FROM factura_detalle WHERE id_factura = %s"

        cursor = conexion.cursor()
        cursor.execute(consulta, (idFactura))

        resultado = cursor.fetchone()

        conexion.close()

        if not resultado:
            return None

        idFactura, cantidad, precio = resultado
        detalleFactura = FacturaDetalle(idFactura, cantidad, precio)

        return detalleFactura
