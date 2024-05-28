from model.Proveedor import Proveedor

class ProveedorController:

    def __init__(self):
        pass
    
    def inicio (self, id_proveedor, nombre, direccion, email, telefono):
        self.producto = Proveedor(id_proveedor, nombre, direccion, email, telefono)

    def validacionGuardarProveedor(self, ProveedorWindow):
        
        if(ProveedorWindow.id_proveedor_edit.text() == "" or ProveedorWindow.nombre_proveedor_edit.text() == "" or ProveedorWindow.direccion_proveedor_edit.text() == "" or ProveedorWindow.email_proveedor_edit.text() == "" or ProveedorWindow.telefono_proveedor_edit.text() == ""):
            print("Campos vacios")
            return False
        else:
            self.inicio(ProveedorWindow.id_proveedor_edit.text(), ProveedorWindow.nombre_proveedor_edit.text(), ProveedorWindow.direccion_proveedor_edit.text(), ProveedorWindow.email_proveedor_edit.text(), ProveedorWindow.telefono_proveedor_edit.text())
            print("Campos llenos")
            self.producto.agregarProveedor()
            return True