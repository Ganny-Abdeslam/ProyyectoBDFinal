from model.Usuario import Usuario, BDUsuario

class UsuarioController:

    def __init__(self):
        pass
    
    def inicio (self, cedula, primerNombre, segundoNombre, primerApellido, segundoApellido, fechaNacimiento, telefono, direccion, email, salario, username, password):
        self.usuario = Usuario(cedula, primerNombre, segundoNombre, primerApellido, segundoApellido, fechaNacimiento, telefono, direccion, email, salario, username, password, "1")

    def validacionGuardarUsuario(self, UsuarioWindow):
        if (UsuarioWindow.cedula_edit.text() == "" or UsuarioWindow.primer_nombre_edit.text() == "" or UsuarioWindow.segundo_nombre_edit.text() == "" or UsuarioWindow.primer_apellido_edit.text() == "" or UsuarioWindow.segundo_apellido_edit.text() == "" or UsuarioWindow.fecha_nacimiento_edit.date().toString("yyyy-MM-dd") == "" or UsuarioWindow.telefono_edit.text() == "" or UsuarioWindow.direccion_edit.text() == "" or UsuarioWindow.email_edit.text() == "" or UsuarioWindow.salario_edit.text() == "" or UsuarioWindow.username_edit.text() == "" or UsuarioWindow.password_edit.text() == ""):
            print("Campos vacios")
            return False
        else:
            self.inicio(UsuarioWindow.cedula_edit.text(), UsuarioWindow.primer_nombre_edit.text(), UsuarioWindow.segundo_nombre_edit.text(), UsuarioWindow.primer_apellido_edit.text(), UsuarioWindow.segundo_apellido_edit.text(), UsuarioWindow.fecha_nacimiento_edit.date().toString("yyyy-MM-dd"), UsuarioWindow.telefono_edit.text(), UsuarioWindow.direccion_edit.text(), UsuarioWindow.email_edit.text(), UsuarioWindow.salario_edit.text(), UsuarioWindow.username_edit.text(), UsuarioWindow.password_edit.text())
            print("Campos llenos")
            self.usuario.agregarUsuario()
            return True
        
    def validacionEliminar(self, UsuarioWindow):
        if (UsuarioWindow.id_usuario_eliminar_edit.text() == ""):
            print("Campos vacios")
            return False
        else:
            eliminar = BDUsuario()
            eliminar.eliminarUsuario(UsuarioWindow.id_usuario_eliminar_edit.text())
            print("Campos llenos")
            return True
        
    def llenarDatos(self, UsuarioWindow, cedula):
        self.usuario = BDUsuario()
        busqueda = self.usuario.buscarUsuarioPorCedula(cedula)
        if (busqueda == None):
            return None
        return busqueda
    
    def validacionActualizarUsuario(self, UsuarioWindow):
        if (UsuarioWindow.cedula_edit.text() == "" or UsuarioWindow.primer_nombre_edit.text() == "" or UsuarioWindow.segundo_nombre_edit.text() == "" or UsuarioWindow.primer_apellido_edit.text() == "" or UsuarioWindow.segundo_apellido_edit.text() == "" or UsuarioWindow.fecha_nacimiento_edit.date().toString("yyyy-MM-dd") == "" or UsuarioWindow.telefono_edit.text() == "" or UsuarioWindow.direccion_edit.text() == "" or UsuarioWindow.email_edit.text() == "" or UsuarioWindow.salario_edit.text() == "" or UsuarioWindow.username_edit.text() == "" or UsuarioWindow.password_edit.text() == ""):
            print("Campos vacios")
            return False
        else:
            self.inicio(UsuarioWindow.cedula_edit.text(), UsuarioWindow.primer_nombre_edit.text(), UsuarioWindow.segundo_nombre_edit.text(), UsuarioWindow.primer_apellido_edit.text(), UsuarioWindow.segundo_apellido_edit.text(), UsuarioWindow.fecha_nacimiento_edit.date().toString("yyyy-MM-dd"), UsuarioWindow.telefono_edit.text(), UsuarioWindow.direccion_edit.text(), UsuarioWindow.email_edit.text(), UsuarioWindow.salario_edit.text(), UsuarioWindow.username_edit.text(), UsuarioWindow.password_edit.text())
            print("Campos llenos")
            self.usuario.updateUsuario()
            return True
        