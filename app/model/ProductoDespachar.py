from database.conexion import conexionBD

class PedidoDespachar:
    def __init__(self, bodegueroCedula, facturaIdFactura, fecha, estado) -> None:
        self.bodegueroCedula = bodegueroCedula
        self.facturaIdFactura = facturaIdFactura
        self.fecha = fecha
        self.estado = estado

    def agregarPedidoDespachar(self):
        conexion = conexionBD().conectar()

        consulta = "INSERT INTO pedido_despachar (bodeguero_cedula, factura_id_factura, fecha, estado) VALUES (%s, %s, %s, %s)"
        datos = (self.bodegueroCedula, self.facturaIdFactura, self.fecha, self.estado)

        cursor = conexion.cursor()
        cursor.execute(consulta, datos)

        conexion.commit()
        conexion.close()

        print("Se agregó correctamente el pedido para despachar")

    def listarPedidosDespachar(self):
        conexion = conexionBD().conectar()

        consulta = "SELECT * FROM pedido_despachar"

        cursor = conexion.cursor()
        cursor.execute(consulta)

        resultados = cursor.fetchall()

        conexion.close()

        pedidosDespachar = []

        for resultado in resultados:
            bodegueroCedula, facturaIdFactura, fecha, estado = resultado
            pedidoDespachar = PedidoDespachar(bodegueroCedula, facturaIdFactura, fecha, estado)
            pedidosDespachar.append(pedidoDespachar)

        return pedidosDespachar

    def buscarPedidoDespacharPorIds(self, facturaIdFactura):
        conexion = conexionBD().conectar()

        consulta = "SELECT * FROM pedido_despachar WHERE factura_id_factura = %s"

        cursor = conexion.cursor()
        cursor.execute(consulta, (facturaIdFactura))

        resultado = cursor.fetchone()

        conexion.close()

        if not resultado:
            return None

        facturaIdFactura, fecha, estado = resultado
        pedidoDespachar = PedidoDespachar(facturaIdFactura, fecha, estado)

        return pedidoDespachar
