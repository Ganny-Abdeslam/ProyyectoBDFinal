from model.Producto import Producto

class ProductoController:

    def __init__(self):
        pass
    
    def inicio (self, nombre, descripcion, precio, cantidad):
        self.producto = Producto(nombre, descripcion, precio, cantidad)

    def validacionGuardarProducto(self, ProductoWindow):
        if (ProductoWindow.nombre_producto_edit.text() == "" or ProductoWindow.descripcion_producto_edit.text() == "" or ProductoWindow.precio_producto_edit.text() == "" or ProductoWindow.cantidad_producto_edit.text() == ""):
            print("Campos vacios")
            return False
        else:
            self.inicio(ProductoWindow.nombre_producto_edit.text(), ProductoWindow.descripcion_producto_edit.text(), ProductoWindow.precio_producto_edit.text(), ProductoWindow.cantidad_producto_edit.text())
            print("Campos llenos")
            self.producto.agregarProducto()
            return True