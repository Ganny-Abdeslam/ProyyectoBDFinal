from database.conexion import conexionBD

class PedidoEntrega:
    def __init__(self, bodegueroCedula, facturaIdFactura, fecha, estado, distribuidorCedula) -> None:
        self.bodegueroCedula = bodegueroCedula
        self.facturaIdFactura = facturaIdFactura
        self.fecha = fecha
        self.estado = estado
        self.distribuidorCedula = distribuidorCedula

    def agregarPedidoEntrega(self):
        conexion = conexionBD().conectar()

        consulta = "INSERT INTO pedido_entrega (bodeguero_cedula, factura_id_factura, fecha, estado, distribuidor_cedula) VALUES (%s, %s, %s, %s, %s)"
        datos = (self.bodegueroCedula, self.facturaIdFactura, self.fecha, self.estado, self.distribuidorCedula)

        cursor = conexion.cursor()
        cursor.execute(consulta, datos)

        conexion.commit()
        conexion.close()

        print("Se agregó correctamente el pedido de entrega")

    def listarPedidosEntrega(self):
        conexion = conexionBD().conectar()

        consulta = "SELECT * FROM pedido_entrega"

        cursor = conexion.cursor()
        cursor.execute(consulta)

        resultados = cursor.fetchall()

        conexion.close()

        pedidosEntrega = []

        for resultado in resultados:
            bodegueroCedula, facturaIdFactura, fecha, estado, distribuidorCedula = resultado
            pedidoEntrega = PedidoEntrega(bodegueroCedula, facturaIdFactura, fecha, estado, distribuidorCedula)
            pedidosEntrega.append(pedidoEntrega)

        return pedidosEntrega

    def buscarPedidoEntregaPorIds(self, facturaIdFactura):
        conexion = conexionBD().conectar()

        consulta = "SELECT * FROM pedido_entrega WHERE factura_id_factura = %s"

        cursor = conexion.cursor()
        cursor.execute(consulta, (facturaIdFactura))

        resultado = cursor.fetchone()

        conexion.close()

        if not resultado:
            return None

        facturaIdFactura, fecha, estado, distribuidorCedula = resultado
        pedidoEntrega = PedidoEntrega(facturaIdFactura, fecha, estado, distribuidorCedula)

        return pedidoEntrega
