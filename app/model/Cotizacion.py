from database.conexion import conexionBD

class Cotizacion:
    def __init__(self, fecha, total, vendedorCedula) -> None:
        self.fecha = fecha
        self.total = total
        self.vendedorCedula = vendedorCedula

    def agregarCotizacion(self):
        conexion = conexionBD().conectar()

        consulta = "INSERT INTO cotizacion (fecha, total, vendedor_cedula) VALUES (%s, %s, %s)"
        datos = (self.fecha, self.total, self.vendedorCedula)

        cursor = conexion.cursor()
        cursor.execute(consulta, datos)

        conexion.commit()
        conexion.close()

        print("Se agregó correctamente la cotización")

    def listarCotizaciones(self):
        conexion = conexionBD().conectar()

        consulta = "SELECT * FROM cotizacion"

        cursor = conexion.cursor()
        cursor.execute(consulta)

        resultados = cursor.fetchall()

        conexion.close()

        cotizaciones = []

        for resultado in resultados:
            id_cotizacion, fecha, total, vendedorCedula = resultado
            cotizacion = Cotizacion(fecha, total, vendedorCedula)
            cotizaciones.append(cotizacion)

        return cotizaciones

    def buscarCotizacionId(self, id_cotizacion):
        conexion = conexionBD().conectar()

        consulta = "SELECT * FROM cotizacion WHERE id_cotizacion = %s"

        cursor = conexion.cursor()
        cursor.execute(consulta, (id_cotizacion,))

        resultado = cursor.fetchone()

        conexion.close()

        if not resultado:
            return None

        id_cotizacion, fecha, total, vendedorCedula = resultado
        cotizacion = Cotizacion(fecha, total, vendedorCedula)

        return cotizacion
