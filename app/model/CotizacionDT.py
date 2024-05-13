from database.conexion import conexionBD

class CotizacionDetalle:
    def __init__(self, idCotizacion, idProducto, cantidad) -> None:
        self.idCotizacion = idCotizacion
        self.idProducto = idProducto
        self.cantidad = cantidad

    def agregarDetalleCotizacion(self):
        conexion = conexionBD().conectar()

        consulta = "INSERT INTO cotizacion_detalle (id_cotizacion, id_producto, cantidad) VALUES (%s, %s, %s)"
        datos = (self.idCotizacion, self.idProducto, self.cantidad)

        cursor = conexion.cursor()
        cursor.execute(consulta, datos)

        conexion.commit()
        conexion.close()

        print("Se agregó correctamente el detalle de la cotización")

    def listarDetallesCotizacion(self):
        conexion = conexionBD().conectar()

        consulta = "SELECT * FROM cotizacion_detalle"

        cursor = conexion.cursor()
        cursor.execute(consulta)

        resultados = cursor.fetchall()

        conexion.close()

        detallesCotizacion = []

        for resultado in resultados:
            idCotizacion, idProducto, cantidad = resultado
            detalleCotizacion = CotizacionDetalle(idCotizacion, idProducto, cantidad)
            detallesCotizacion.append(detalleCotizacion)

        return detallesCotizacion

    def buscarDetalleCotizacionPorIds(self, idCotizacion):
        conexion = conexionBD().conectar()

        consulta = "SELECT * FROM cotizacion_detalle WHERE id_cotizacion = %s"

        cursor = conexion.cursor()
        cursor.execute(consulta, (idCotizacion))

        resultado = cursor.fetchone()

        conexion.close()

        if not resultado:
            return None

        idCotizacion, idProducto, cantidad = resultado
        detalleCotizacion = CotizacionDetalle(idCotizacion, idProducto, cantidad)

        return detalleCotizacion
