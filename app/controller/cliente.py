from model.Cliente import Cliente
from PyQt6.QtCore import Qt

class ClienteController:
    
        def __init__(self):
            pass
        
        def inicio (self, nombre, direccion, telefono, email):
            self.cliente = Cliente(nombre, direccion, telefono, email, "1")
    
        def validacionGuardarCliente(self, ClienteWindow):
            if (ClienteWindow.nombre_cliente_edit.text() == "" or ClienteWindow.direccion_cliente_edit.text() == "" or ClienteWindow.telefono_cliente_edit.text() == "" or ClienteWindow.email_cliente_edit.text() == ""):
                print("Campos vacios")
                return False
            else:
                self.inicio(ClienteWindow.nombre_cliente_edit.text(), ClienteWindow.direccion_cliente_edit.text(), ClienteWindow.telefono_cliente_edit.text(), ClienteWindow.email_cliente_edit.text())
                print("Campos llenos")
                self.cliente.agregarCliente()
                return True
                
