from database.conexion import conexionBD

class Material:
    def __init__(self, idMateriaPrima, idProducto) -> None:
        self.idMateriaPrima = idMateriaPrima
        self.idProducto = idProducto

    def agregarMaterial(self):
        conexion = conexionBD().conectar()

        consulta = "INSERT INTO material (id_materia_prima, id_producto) VALUES (%s, %s)"
        datos = (self.idMateriaPrima, self.idProducto)

        cursor = conexion.cursor()
        cursor.execute(consulta, datos)

        conexion.commit()
        conexion.close()

        print("Se agregó correctamente el material")

    def listarMateriales(self):
        conexion = conexionBD().conectar()

        consulta = "SELECT * FROM material"

        cursor = conexion.cursor()
        cursor.execute(consulta)

        resultados = cursor.fetchall()

        conexion.close()

        materiales = []

        for resultado in resultados:
            idMateriaPrima, idProducto = resultado
            material = Material(idMateriaPrima, idProducto)
            materiales.append(material)

        return materiales

    def buscarMaterialMaetriaPrima(self, idMateriaPrima):
        conexion = conexionBD().conectar()

        consulta = "SELECT * FROM material WHERE id_materia_prima = %s"

        cursor = conexion.cursor()
        cursor.execute(consulta, (idMateriaPrima))

        resultado = cursor.fetchone()

        conexion.close()

        if not resultado:
            return None

        idMateriaPrima = resultado
        material = Material(idMateriaPrima)

        return material
    
    def buscarMaterialPorProducto(self, idProducto):
        conexion = conexionBD().conectar()

        consulta = "SELECT * FROM material WHERE id_producto = %s"

        cursor = conexion.cursor()
        cursor.execute(consulta, (idProducto))

        resultado = cursor.fetchone()

        conexion.close()

        if not resultado:
            return None

        idProducto = resultado
        material = Material(idProducto)

        return material
