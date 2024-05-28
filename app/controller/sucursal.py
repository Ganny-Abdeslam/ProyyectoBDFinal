from model.Sucursal import Sucursal, BDSucursal

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
            self.inicio(SucursalWindow.direccion_sucursal_edit.text(), SucursalWindow.telefono_sucursal_edit.text(), SucursalWindow.email_sucursal_edit.text(), SucursalWindow.cedula_jefe_sucursal_edit.text(), SucursalWindow.ciudad_sucursal_combobox.currentIndex())
            print("Campos llenos")
            self.sucursal.agregarSucursal()
            return True
        
    def validacionEliminar(self, SucursalWindow):
        if (SucursalWindow.id_sucursal_eliminar_edit.text() == ""):
            print("Campos vacios")
            return False
        else:
            print("Campos llenos")
            eliminar = BDSucursal()
            eliminar.eliminarSucursal(SucursalWindow.id_sucursal_eliminar_edit.text())
            return True
        
    def llenarDatos(self, SucursalWindow, id_sucursal):
        self.sucursal = BDSucursal()
        busqueda = self.sucursal.buscarSucursalPorId(id_sucursal)
        if (busqueda == None):
            return None
        return busqueda
    
    def validacionActualizarSucursal(self, SucursalWindow, id_sucursal):
        if (SucursalWindow.direccion_sucursal_edit.text() == "" or SucursalWindow.telefono_sucursal_edit.text() == "" or SucursalWindow.email_sucursal_edit.text() == "" or SucursalWindow.cedula_jefe_sucursal_edit.text() == ""):
            print("Campos vacios")
            return False
        else:
            self.inicio(SucursalWindow.direccion_sucursal_edit.text(), SucursalWindow.telefono_sucursal_edit.text(), SucursalWindow.email_sucursal_edit.text(), SucursalWindow.cedula_jefe_sucursal_edit.text(), SucursalWindow.ciudad_sucursal_combobox.currentIndex())
            print("Campos llenos")
            self.sucursal.updateSucursal(id_sucursal)
            return True

    

            