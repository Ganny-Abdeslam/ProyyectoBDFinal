from database.conexion import conexionBD

class FacturaDetalle:
    def __init__(self, idFactura, vendedorCedula, total, idCliente, fecha, clienteNombre, productoNombre, cantidad, precio, subtotal):
        self.idFactura = idFactura
        self.vendedorCedula = vendedorCedula
        self.total = total
        self.idCliente = idCliente
        self.fecha = fecha
        self.clienteNombre = clienteNombre
        self.productoNombre = productoNombre
        self.cantidad = cantidad
        self.precio = precio
        self.subtotal = subtotal

    def to_dict(self):
        return {
            'id_factura': self.idFactura,
            'vendedor_cedula': self.vendedorCedula,
            'total': float(self.total),
            'id_cliente': self.idCliente,
            'fecha': self.fecha.isoformat(),
            'nombre': self.clienteNombre,
            'producto': self.productoNombre,
            'cantidad': self.cantidad,
            'precio': float(self.precio),
            'subtotal': float(self.subtotal)
        }


class BDDTFactura:
    def __init__(self) -> None:
        pass

    def consultarDT(self, idFactura):
        conexion = conexionBD().conectar()

        consulta = """
                    SELECT f.id_factura, f.vendedor_cedula, f.total, f.id_cliente, f.fecha, c.nombre, 
                        (SELECT nombre FROM producto WHERE id_producto = fd.id_producto) AS producto, 
                        fd.cantidad, fd.precio, fd.cantidad * fd.precio AS subtotal
                    FROM factura_detalle fd
                    INNER JOIN factura f ON (f.id_factura = fd.id_factura)
                    INNER JOIN cliente c ON (c.id_cliente = f.id_cliente)
                    WHERE fd.id_factura = %s
                """

        cursor = conexion.cursor()
        cursor.execute(consulta, (idFactura,))

        resultados = cursor.fetchall()

        conexion.close()

        detallesFactura = []

        for resultado in resultados:
            # Desempaqueta todos los valores de la consulta
            (idFactura, vendedorCedula, total, id_cliente, fecha, clienteNombre, productoNombre, 
            cantidad, precio, subtotal) = resultado

            # Crea el objeto FacturaDetalle con los valores desempaquetados
            detalleFactura = FacturaDetalle(idFactura, vendedorCedula, total, id_cliente, fecha, clienteNombre, productoNombre, cantidad, precio, subtotal)
            detallesFactura.append(detalleFactura.to_dict())

        return detallesFactura
