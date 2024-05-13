from database.conexion import conexionBD

class MateriaPrima:
    def __init__(self, nombre, descripcion, cantidad) -> None:
        self.nombre = nombre
        self.descripcion = descripcion
        self.cantidad = cantidad

    def agregarMateriaPrima(self):
        conexion = conexionBD().conectar()

        consulta = "INSERT INTO materia_prima (nombre, descripcion, cantidad) VALUES (%s, %s, %s)"
        datos = (self.nombre, self.descripcion, self.cantidad)

        cursor = conexion.cursor()
        cursor.execute(consulta, datos)

        conexion.commit()
        conexion.close()

        print("Se agregó correctamente la materia prima")

    def listarMateriasPrimas(self):
        conexion = conexionBD().conectar()

        consulta = "SELECT * FROM materia_prima"

        cursor = conexion.cursor()
        cursor.execute(consulta)

        resultados = cursor.fetchall()

        conexion.close()

        materiasPrimas = []

        for resultado in resultados:
            idMateriaPrima, nombre, descripcion, cantidad = resultado
            materiaPrima = MateriaPrima(nombre, descripcion, cantidad)
            materiasPrimas.append(materiaPrima)

        return materiasPrimas

    def buscarMateriaPrimaPorId(self, idMateriaPrima):
        conexion = conexionBD().conectar()

        consulta = "SELECT * FROM materia_prima WHERE id_materia_prima = %s"

        cursor = conexion.cursor()
        cursor.execute(consulta, (idMateriaPrima,))

        resultado = cursor.fetchone()

        conexion.close()

        if not resultado:
            return None

        idMateriaPrima, nombre, descripcion, cantidad = resultado
        materiaPrima = MateriaPrima(nombre, descripcion, cantidad)

        return materiaPrima
