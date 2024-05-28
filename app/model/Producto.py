from database.conexion import conexionBD

class Producto:
    def __init__(self, nombre, descripcion, precio, cantidad) -> None:
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad

    def agregarProducto(self):
        conexion = conexionBD().conectar()

        consulta = "INSERT INTO producto (nombre, descripcion, precio, cantidad) VALUES (%s, %s, %s, %s)"
        datos = (self.nombre, self.descripcion, self.precio, self.cantidad)

        cursor = conexion.cursor()
        cursor.execute(consulta, datos)

        conexion.commit()
        conexion.close()

        print(f"Se agregó correctamente el producto: {self.nombre}")

class BDProducto:
    def __init__(self) -> None:
        pass

    def listarProductos(self):
        conexion = conexionBD().conectar()

        consulta = "SELECT * FROM producto"

        cursor = conexion.cursor()
        cursor.execute(consulta)

        resultados = cursor.fetchall()

        conexion.close()

        productos = []

        for resultado in resultados:
            id_producto, nombre, descripcion, precio, cantidad = resultado
            producto = Producto(nombre, descripcion, precio, cantidad)
            productos.append(producto)

        return productos

    def buscarProductoId(self, id_producto):
        conexion = conexionBD().conectar()

        consulta = "SELECT * FROM producto WHERE id_producto = %s"

        cursor = conexion.cursor()
        cursor.execute(consulta, (id_producto,))

        resultado = cursor.fetchone()

        conexion.close()

        if not resultado:
            return None

        id_producto, nombre, descripcion, precio, cantidad = resultado
        producto = Producto(nombre, descripcion, precio, cantidad)

        return producto
    
    def eliminarProducto(self, id_producto):
        conexion = conexionBD().conectar()

        cursor = conexion.cursor()

        consulta = "DELETE FROM producto WHERE id_producto = %s"
        datos = (id_producto)

        cursor.execute(consulta, datos)

        conexion.commit()

        conexion.close()

        print("Se eliminó correctamente el producto")
