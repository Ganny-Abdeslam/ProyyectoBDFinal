from model.Sucursal import Sucursal

class SucursalController:

    def __init__(self):
        pass

    def inicio (self, direccion, telefono, email, jefeCedula, idCiudad):
        self.sucursal = Sucursal(direccion, telefono, email, jefeCedula, idCiudad)

    def validacionGuardarSucursal(self, SucursalWindow):
        if (SucursalWindow.direccion_sucursal_edit.text() == "" or SucursalWindow.telefono_sucursal_edit.text() == "" or SucursalWindow.email_sucursal_edit.text() == "" or SucursalWindow.cedula_jefe_sucursal_edit.text() == ""):
            print("Campos vacios")
            return False
        else:
            self.inicio(SucursalWindow.direccion_sucursal_edit.text(), SucursalWindow.telefono_sucursal_edit.text(), SucursalWindow.email_sucursal_edit.text(), SucursalWindow.cedula_jefe_sucursal_edit.text(), "1")
            print("Campos llenos")
            self.sucursal.agregarSucursal()
            return True
            