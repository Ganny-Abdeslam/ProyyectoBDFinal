from model.MateriaPrima import MateriaPrima

class MateriaPrimaController:

    def __init__(self):
        pass

    def inicio (self, nombre, descripcion, cantidad):
        self.materiaPrima = MateriaPrima(nombre, descripcion, cantidad)

    def validacionGuardarMateriaPrima(self, MaterialWindow):
        if (MaterialWindow.nombre_material_edit.text() == "" or MaterialWindow.descripcion_material_edit.text() == "" or MaterialWindow.cantidad_material_edit.text() == ""):
            print("Campos vacios")
            return False
        else:
            self.inicio(MaterialWindow.nombre_material_edit.text(), MaterialWindow.descripcion_material_edit.text(), MaterialWindow.cantidad_material_edit.text())
            print("Campos llenos")
            self.materiaPrima.agregarMateriaPrima()
            return True