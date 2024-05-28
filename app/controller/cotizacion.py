from model.Cotizacion import Cotizacion

class CotizacionController:

    def __init__(self):
        pass

    def inicio (self, fecha, total, vendedorCedula):
        self.cotizacion = Cotizacion(fecha, total, vendedorCedula)

    def validacionGuardarCotizacion(self, CotizacionWindow):
        if (CotizacionWindow.fecha_cotizacion_calendar.date().toString("yyyy-MM-dd") == "" or CotizacionWindow.total_cotizacion_edit.text() == "" or CotizacionWindow.cedula_vendedor_edit.text() == ""):
            print("Campos vacios")
            return False
        else:
            self.inicio(CotizacionWindow.fecha_cotizacion_calendar.date().toString("yyyy-MM-dd"), CotizacionWindow.total_cotizacion_edit.text(), CotizacionWindow.cedula_vendedor_edit.text())
            print("Campos llenos")
            self.cotizacion.agregarCotizacion()
            return True