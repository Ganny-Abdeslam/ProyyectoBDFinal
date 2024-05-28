from model.PedidoEntrega import PedidoEntrega

class PedidoEntregaController:

    def __init__(self) -> None:
        pass

    def inicio (self, bodegueroCedula, facturaIdFactura, fecha, estado, distribuidorCedula):
        self.pedidoEntrega = PedidoEntrega(bodegueroCedula, facturaIdFactura, fecha, estado, distribuidorCedula)

    def validacionGuardarPedidoEntrega(self, PedidoEntregaWindow):
        if (PedidoEntregaWindow.cedula_bodeguero_edit.text() == "" or PedidoEntregaWindow.id_factura_edit.text() == "" or PedidoEntregaWindow.fecha_entrega_calendar.date().toString("yyyy-MM-dd") == "" or PedidoEntregaWindow.estado_pedido_edit.text() == "" or PedidoEntregaWindow.cedula_distribuidor_edit.text() == ""):
            print("Campos vacios")
            return False
        else:
            self.inicio(PedidoEntregaWindow.cedula_bodeguero_edit.text(), PedidoEntregaWindow.id_factura_edit.text(), PedidoEntregaWindow.fecha_entrega_calendar.date().toString("yyyy-MM-dd"), PedidoEntregaWindow.estado_pedido_edit.text(), PedidoEntregaWindow.cedula_distribuidor_edit.text())
            print("Campos llenos")
            self.pedidoEntrega.agregarPedidoEntrega()
            return True
        
