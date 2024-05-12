from database.conexion import conexionBD
from database.inicializacionTablas import generacionTablas

if __name__ == "__main__":
    conexion = conexionBD().conectar()

    generacionTablas().generarCliente(conexion)

    generacionTablas().generarProducto(conexion)
    generacionTablas().generarCotizacion(conexion)
    generacionTablas().generarDTCotizacion(conexion)
    
    generacionTablas().generarPais(conexion)
    generacionTablas().generarDepartamentos(conexion)
    generacionTablas().generarCiudad(conexion)

    generacionTablas().generarDistribuidor(conexion)
    generacionTablas().generarPedidoDesp(conexion)
    generacionTablas().generarPedidoEntr(conexion)

    generacionTablas().generarFactura(conexion)
    generacionTablas().generarFacturaDT(conexion)

    generacionTablas().generarMaterial(conexion)
    generacionTablas().generarMateriaPrima(conexion)
    generacionTablas().generarProductoSucursal(conexion)
    generacionTablas().generarSucursal(conexion)
    generacionTablas().generarProveedor(conexion)
    generacionTablas().generarProveedorMP(conexion)

    generacionTablas().generarUsuario(conexion)
    generacionTablas().generarVendedor(conexion)
    generacionTablas().generarBodeguero(conexion)

    generacionTablas().generarForaneas(conexion)
    
    if 'conexion' in locals() and conexion.open:
        conexion.close()