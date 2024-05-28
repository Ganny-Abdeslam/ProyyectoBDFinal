from database.conexion import conexionBD
from database.inicializacionTablas import generacionTablas
from View.principalScreen import PrincipalScreen
from database.generarCiudades import Countries, Departamentos, Ciudades
from model.Cliente import Cliente
from Reportes.FacturaReporte import FacturaReport

import sys
from PyQt6.QtWidgets import QApplication

def generarBD():
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

def generarNormalizacion():
    if Countries().count_countries() > 0:
        return
    
    Countries().insert_countries()
    Departamentos().insert_states()
    Ciudades().insert_ciudades()

if __name__ == "__main__":

    generarBD()
    generarNormalizacion()
    app = QApplication(sys.argv)
    PrincipalScreen()
    PrincipalScreen().show()
    sys.exit(app.exec())
