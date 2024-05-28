from model.Factura import Factura, BDFactura

class FacturaController:

    def __init__(self):
        pass

    def inicio (self, fecha, total, idCliente, vendedorCedula):
        self.factura = Factura(fecha, total, idCliente, vendedorCedula)

    def validacionGuardarFactura(self, FacturaWindow):
        if (FacturaWindow.fecha_factura_calendar.date().toString("yyyy-MM-dd") == "" or FacturaWindow.total_factura_edit.text() == "" or FacturaWindow.id_cliente_edit.text() == "" or FacturaWindow.cedula_vendedor_edit.text() == ""):
            print("Campos vacios")
            return False
        else:
            self.inicio(FacturaWindow.fecha_factura_calendar.date().toString("yyyy-MM-dd"), FacturaWindow.total_factura_edit.text(), FacturaWindow.id_cliente_edit.text(), FacturaWindow.cedula_vendedor_edit.text())
            print("Campos llenos")
            self.factura.agregarFactura()
            return True
        
    def validacionEliminar(self, FacturaWindow):
        if (FacturaWindow.id_factura_eliminar_edit.text() == ""):
            print("Campos vacios")
            return False
        else:
            eliminar = BDFactura()
            eliminar.eliminarFactura(FacturaWindow.id_factura_eliminar_edit.text())
            print("Campos llenos")
            return True
        
    def llenarDatos(self, FacturaWindow, id_factura):
        self.factura = BDFactura()
        busqueda = self.factura.buscarFacturaPorId(id_factura)
        if (busqueda == None):
            return None
        return busqueda
    
    def validacionActualizarFactura(self, FacturaWindow, id_factura):
        if (FacturaWindow.fecha_factura_calendar.date().toString("yyyy-MM-dd") == "" or FacturaWindow.total_factura_edit.text() == "" or FacturaWindow.id_cliente_edit.text() == "" or FacturaWindow.cedula_vendedor_edit.text() == ""):
            print("Campos vacios")
            return False
        else:
            self.inicio(FacturaWindow.fecha_factura_calendar.date().toString("yyyy-MM-dd"), FacturaWindow.total_factura_edit.text(), FacturaWindow.id_cliente_edit.text(), FacturaWindow.cedula_vendedor_edit.text())
            print("Campos llenos")
            self.factura.updateFactura(id_factura)
            return True

      