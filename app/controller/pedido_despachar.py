from model.PedidoDespachar import PedidoDespachar

class PedidoDespacharController:

    def __init__(self) -> None:
        pass

    def inicio (self, bodegueroCedula, facturaIdFactura, fecha, estado):
        self.pedidoDespachar = PedidoDespachar(bodegueroCedula, facturaIdFactura, fecha, estado)

    def validacionGuardarPedidoDespachar(self, DespachoPedidoWindow):
        if (DespachoPedidoWindow.cedula_bodeguero_edit.text() == "" or DespachoPedidoWindow.id_factura_edit.text() == "" or DespachoPedidoWindow.fecha_despacho_calendar.date().toString("yyyy-MM-dd") == "" or DespachoPedidoWindow.estado_pedido_edit.text() == ""):
            print("Campos vacios")
            return False
        else:
            self.inicio(DespachoPedidoWindow.cedula_bodeguero_edit.text(), DespachoPedidoWindow.id_factura_edit.text(), DespachoPedidoWindow.fecha_despacho_calendar.date().toString("yyyy-MM-dd"), DespachoPedidoWindow.estado_pedido_edit.text())
            print("Campos llenos")
            self.pedidoDespachar.agregarPedidoDespachar()
            return True