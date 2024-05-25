from model.Usuario import Usuario 
from PyQt6.QtCore import Qt

class UsuarioController:

    def __init__(self):
        pass
    
    def inicio (self, cedula, primerNombre, segundoNombre, primerApellido, segundoApellido, fechaNacimiento, telefono, direccion, email, salario, username, password, idSucursal):
        self.usuario = Usuario(cedula, primerNombre, segundoNombre, primerApellido, segundoApellido, fechaNacimiento, telefono, direccion, email, salario, username, password, idSucursal)

    def validacionGuardarUsuario(self, UsuarioWindow):
        if UsuarioWindow.cedula_edit.text() == "" or UsuarioWindow.primer_nombre_edit.text() == "" or UsuarioWindow.segundo_nombre_edit.text() == "" or UsuarioWindow.primer_apellido_edit.text() == "" or UsuarioWindow.segundo_apellido_edit.text() == "" or UsuarioWindow.fecha_nacimiento_edit.date().toString("yyyy-MM-dd") == "" or UsuarioWindow.telefono_edit.text() == "" or UsuarioWindow.direccion_edit.text() == "" or UsuarioWindow.email_edit.text() == "" or UsuarioWindow.salario_edit.text() == "" or UsuarioWindow.username_edit.text() == "" or UsuarioWindow.password_edit.text() == "" or UsuarioWindow.id_sucursal_edit.text() == "":
            print("Campos vacios")
            return False
        else:
            self.inicio(UsuarioWindow.cedula_edit.text(), UsuarioWindow.primer_nombre_edit.text(), UsuarioWindow.segundo_nombre_edit.text(), UsuarioWindow.primer_apellido_edit.text(), UsuarioWindow.segundo_apellido_edit.text(), UsuarioWindow.fecha_nacimiento_edit.date().toString("yyyy-MM-dd"), UsuarioWindow.telefono_edit.text(), UsuarioWindow.direccion_edit.text(), UsuarioWindow.email_edit.text(), UsuarioWindow.salario_edit.text(), UsuarioWindow.username_edit.text(), UsuarioWindow.password_edit.text(), UsuarioWindow.id_sucursal_edit.text())
            print("Campos llenos")
            self.usuario.agregarUsuario()