from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QGridLayout, QLabel, QLineEdit, QComboBox, QCalendarWidget, QMessageBox, QDateEdit, QFileDialog, QDialog
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QDate
from Reportes.SucursalReporte import SucursalReport
import webbrowser
import os

from controller.usuario import UsuarioController
from controller.sucursal import SucursalController
from controller.cliente import ClienteController
from controller.producto import ProductoController
from controller.factura import FacturaController
from controller.proveedor import ProveedorController
from controller.materia_prima import MateriaPrimaController
from controller.cotizacion import CotizacionController
from controller.pedido_entrega import PedidoEntregaController
from controller.pedido_despachar import PedidoDespacharController
from model.Ciudad import BDCiudad


class PrincipalScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Tienda BuhoVigia')
        self.setGeometry(100, 100, 600, 400)
        
        # Establecer el color de fondo para la ventana
        self.setStyleSheet("background-color: lightblue;")

        layout = QVBoxLayout()

        # Agregar la imagen del logo
        logo_label = QLabel(self)
        pixmap = QPixmap("app/View/images/logo.png")
        pixmap = pixmap.scaledToWidth(200)
        logo_label.setPixmap(pixmap)
        layout.addWidget(logo_label, alignment=Qt.AlignmentFlag.AlignHCenter)  # Centrar el logo horizontalmente

        # Layout de cuadrícula para los botones
        grid_layout = QGridLayout()

        # Agregar botones
        botones = ['Usuario', 'Cliente', 'Sucursal', 'Producto', 'Factura', 'Proveedor', 'Material', 'Cotización', 'Entrega de pedidos', 'Despacho de pedidos']
        fila = 0
        columna = 0
        for texto_boton in botones:
            boton = QPushButton(texto_boton)
            boton.setFixedSize(150, 50)
            
            # Establecer un color de fondo, borde y radio para los botones
            boton.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
            
            grid_layout.addWidget(boton, fila, columna)
            fila += 1

            if fila == 5:
                fila = 0
                columna += 1

            boton.clicked.connect(lambda _, texto=texto_boton: self.abrir_ventana(texto))

        layout.addLayout(grid_layout)
        self.setLayout(layout)

    def abrir_ventana(self, opcion):
        if opcion == 'Usuario':
            self.usuario_window = UsuarioWindow(self)
            self.usuario_window.show()
            self.hide()
        
        if opcion == 'Cliente':
            self.cliente_window = ClienteWindow(self)
            self.cliente_window.show()
            self.hide()
        
        if opcion == 'Sucursal':
            self.sucursal_window = SucursalWindow(self)
            self.sucursal_window.show()
            self.hide()
        
        if opcion == 'Producto':
            self.producto_window = ProductoWindow(self)
            self.producto_window.show()
            self.hide()
        
        if opcion == 'Factura':
            self.factura_window = FacturaWindow(self)
            self.factura_window.show()
            self.hide()
        
        if opcion == 'Proveedor':
            self.proveedor_window = ProveedorWindow(self)
            self.proveedor_window.show()
            self.hide()
        
        if opcion == 'Material':
            self.material_window = MaterialWindow(self)
            self.material_window.show()
            self.hide()
        
        if opcion == 'Cotización':
            self.cotizacion_window = CotizacionWindow(self)
            self.cotizacion_window.show()
            self.hide()
        
        if opcion == 'Entrega de pedidos':
            self.entrega_pedido_window = EntregaPedidoWindow(self)
            self.entrega_pedido_window.show()
            self.hide()
        
        if opcion == 'Despacho de pedidos':
            self.despacho_pedido_window = DespachoPedidoWindow(self)
            self.despacho_pedido_window.show()
            self.hide()
        
class UsuarioWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle('Usuario')
        self.setGeometry(100, 100, 600, 400)

        self.setStyleSheet("background-color: lightblue;")

        layout_usuario = QGridLayout()

        # Campo de entrada para la cédula
        layout_usuario.addWidget(QLabel("Cédula:"), 0, 0)
        self.cedula_edit = QLineEdit()
        self.cedula_edit.setStyleSheet("background-color: white;")
        layout_usuario.addWidget(self.cedula_edit, 0, 1)

        # Campo de entrada para el primer nombre
        layout_usuario.addWidget(QLabel("Primer Nombre:"), 1, 0)
        self.primer_nombre_edit = QLineEdit()
        self.primer_nombre_edit.setStyleSheet("background-color: white;")
        layout_usuario.addWidget(self.primer_nombre_edit, 1, 1)

        # Campo de entrada para el segundo nombre
        layout_usuario.addWidget(QLabel("Segundo Nombre:"), 2, 0)
        self.segundo_nombre_edit = QLineEdit()
        self.segundo_nombre_edit.setStyleSheet("background-color: white;")
        layout_usuario.addWidget(self.segundo_nombre_edit, 2, 1)

        # Campo de entrada para el primer apellido
        layout_usuario.addWidget(QLabel("Primer Apellido:"), 3, 0)
        self.primer_apellido_edit = QLineEdit()
        self.primer_apellido_edit.setStyleSheet("background-color: white;")
        layout_usuario.addWidget(self.primer_apellido_edit, 3, 1)

        # Campo de entrada para el segundo apellido
        layout_usuario.addWidget(QLabel("Segundo Apellido:"), 4, 0)
        self.segundo_apellido_edit = QLineEdit()
        self.segundo_apellido_edit.setStyleSheet("background-color: white;")
        layout_usuario.addWidget(self.segundo_apellido_edit, 4, 1)

        # Campo de entrada para la fecha de nacimiento
        layout_usuario.addWidget(QLabel("Fecha de Nacimiento:"), 5, 0)
        self.fecha_nacimiento_edit = QDateEdit()
        self.fecha_nacimiento_edit.setCalendarPopup(True)
        self.fecha_nacimiento_edit.setStyleSheet("background-color: white; color:black;")
        layout_usuario.addWidget(self.fecha_nacimiento_edit, 5, 1)

        # Campo de entrada para el teléfono
        layout_usuario.addWidget(QLabel("Teléfono:"), 6, 0)
        self.telefono_edit = QLineEdit()
        self.telefono_edit.setStyleSheet("background-color: white;")
        layout_usuario.addWidget(self.telefono_edit, 6, 1)

        # Campo de entrada para la dirección
        layout_usuario.addWidget(QLabel("Dirección:"), 7, 0)
        self.direccion_edit = QLineEdit()
        self.direccion_edit.setStyleSheet("background-color: white;")
        layout_usuario.addWidget(self.direccion_edit, 7, 1)

        # Campo de entrada para el email
        layout_usuario.addWidget(QLabel("Email:"), 8, 0)
        self.email_edit = QLineEdit()
        self.email_edit.setStyleSheet("background-color: white;")
        layout_usuario.addWidget(self.email_edit, 8, 1)

        # Campo de entrada para el salario
        layout_usuario.addWidget(QLabel("Salario:"), 9, 0)
        self.salario_edit = QLineEdit()
        self.salario_edit.setStyleSheet("background-color: white;")
        layout_usuario.addWidget(self.salario_edit, 9, 1)

        # Campo de entrada para el username
        layout_usuario.addWidget(QLabel("Username:"), 10, 0)
        self.username_edit = QLineEdit()
        self.username_edit.setStyleSheet("background-color: white;")
        layout_usuario.addWidget(self.username_edit, 10, 1)

        # Campo de entrada para el password
        layout_usuario.addWidget(QLabel("Password:"), 11, 0)
        self.password_edit = QLineEdit()
        self.password_edit.setStyleSheet("background-color: white;")
        layout_usuario.addWidget(self.password_edit, 11, 1)

        # Campo de entrada para el tipo de usuario
        layout_usuario.addWidget(QLabel("Tipo de Usuario:"), 12, 0)
        self.tipo_usuario_combobox = QComboBox()
        self.tipo_usuario_combobox.setStyleSheet("background-color: white;")
        self.tipo_usuario_combobox.addItem("Seleccione tipo")  # Título no seleccionable
        self.tipo_usuario_combobox.addItems(["Distribuidor", "Bodeguero", "Vendedor"])
        layout_usuario.addWidget(self.tipo_usuario_combobox, 12, 1)

        # Campo de entrada para la comisión (solo para Vendedor)
        self.comision_label = QLabel("Comisión:")
        self.comision_edit = QLineEdit()
        self.comision_edit.setStyleSheet("background-color: white;")
        layout_usuario.addWidget(self.comision_label, 13, 0)
        layout_usuario.addWidget(self.comision_edit, 13, 1)

        # Campo de entrada para la placa del vehículo (solo para Distribuidor)
        self.placa_label = QLabel("Placa del vehículo:")
        self.placa_edit = QLineEdit()
        self.placa_edit.setStyleSheet("background-color: white;")
        layout_usuario.addWidget(self.placa_label, 14, 0)
        layout_usuario.addWidget(self.placa_edit, 14, 1)

        # Campo de entrada para el nombre del jefe (solo para Bodeguero)
        self.nombre_jefe_label = QLabel("Cedula del jefe:")
        self.nombre_jefe_edit = QLineEdit()
        self.nombre_jefe_edit.setStyleSheet("background-color: white;")
        layout_usuario.addWidget(self.nombre_jefe_label, 15, 0)
        layout_usuario.addWidget(self.nombre_jefe_edit, 15, 1)

        # Botones
        boton_volver = QPushButton("Volver a la pantalla principal")
        boton_volver.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_volver.setFixedSize(200, 40)
        boton_volver.clicked.connect(self.volver_a_principal)

        boton_actualizar = QPushButton("Actualizar")
        boton_actualizar.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_actualizar.setFixedSize(120, 40)

        boton_eliminar = QPushButton("Eliminar")
        boton_eliminar.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_eliminar.setFixedSize(120, 40)

        boton_agregar = QPushButton("Agregar")
        boton_agregar.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_agregar.setFixedSize(120, 40)
        boton_agregar.clicked.connect(self.agregar_usuario)

        layout_usuario.addWidget(boton_volver, 16, 0, 1, 1)
        layout_usuario.addWidget(boton_actualizar, 16, 1, 1, 1)
        layout_usuario.addWidget(boton_eliminar, 16, 2, 1, 1)
        layout_usuario.addWidget(boton_agregar, 16, 3, 1, 1)

        self.setLayout(layout_usuario)
        self.parent = parent

        self.comision_label.hide()
        self.comision_edit.hide()
        self.placa_label.hide()
        self.placa_edit.hide()
        self.nombre_jefe_label.hide()
        self.nombre_jefe_edit.hide()

        # Conectar la señal currentIndexChanged del ComboBox
        self.tipo_usuario_combobox.currentIndexChanged.connect(self.actualizar_campos)

    def actualizar_campos(self, index):
        if index == 0:
            # Si el usuario selecciona "Seleccione tipo", ocultar todos los campos adicionales
            self.comision_label.hide()
            self.comision_edit.hide()
            self.placa_label.hide()
            self.placa_edit.hide()
            self.nombre_jefe_label.hide()
            self.nombre_jefe_edit.hide()

        elif index == 1:
            # Si el usuario selecciona "Distribuidor", mostrar campo de Placa del vehículo
            self.comision_label.hide()
            self.comision_edit.hide()
            self.placa_label.show()
            self.placa_edit.show()
            self.nombre_jefe_label.hide()
            self.nombre_jefe_edit.hide()

        elif index == 2:
            # Si el usuario selecciona "Bodeguero", mostrar campo de Nombre del jefe
            self.comision_label.hide()
            self.comision_edit.hide()
            self.placa_label.hide()
            self.placa_edit.hide()
            self.nombre_jefe_label.show()
            self.nombre_jefe_edit.show()

    def agregar_usuario(self):
        usuarioAgregar = UsuarioController() 
        condicion = usuarioAgregar.validacionGuardarUsuario(self)
        if (condicion):
            QMessageBox.information(self, "Éxito", "Usuario agregado exitosamente.")
        else:
            QMessageBox.information(self, "Informacion", "Campos vacios.")

    def volver_a_principal(self):
        self.close()
        self.parent.show()
        
class ClienteWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle('Cliente')
        self.setGeometry(100, 100, 600, 400)

        self.setStyleSheet("background-color: lightblue;")

        layout_cliente = QGridLayout()

        # Campo de entrada para el nombre del cliente
        layout_cliente.addWidget(QLabel("Nombre del Cliente:"), 0, 0)
        self.nombre_cliente_edit = QLineEdit()
        self.nombre_cliente_edit.setStyleSheet("background-color: white;")
        layout_cliente.addWidget(self.nombre_cliente_edit, 0, 1)

        # Campo de entrada para la dirección del cliente
        layout_cliente.addWidget(QLabel("Dirección del Cliente:"), 1, 0)
        self.direccion_cliente_edit = QLineEdit()
        self.direccion_cliente_edit.setStyleSheet("background-color: white;")
        layout_cliente.addWidget(self.direccion_cliente_edit, 1, 1)

        # Campo de entrada para el teléfono del cliente
        layout_cliente.addWidget(QLabel("Teléfono del Cliente:"), 2, 0)
        self.telefono_cliente_edit = QLineEdit()
        self.telefono_cliente_edit.setStyleSheet("background-color: white;")
        layout_cliente.addWidget(self.telefono_cliente_edit, 2, 1)

        # Campo de entrada para el email del cliente
        layout_cliente.addWidget(QLabel("Email del Cliente:"), 3, 0)
        self.email_cliente_edit = QLineEdit()
        self.email_cliente_edit.setStyleSheet("background-color: white;")
        layout_cliente.addWidget(self.email_cliente_edit, 3, 1)

        # Campo de entrada para seleccionar la ciudad del cliente
        layout_cliente.addWidget(QLabel("Ciudad del Cliente:"), 4, 0)
        self.ciudad_cliente_combobox = QComboBox()
        self.ciudad_cliente_combobox.setStyleSheet("background-color: white;")
        self.ciudad_cliente_combobox.addItems(["Seleccione Ciudad", "Ciudad A", "Ciudad B", "Ciudad C"])  # Ejemplo de ciudades
        layout_cliente.addWidget(self.ciudad_cliente_combobox, 4, 1)

        # Botones
        boton_volver = QPushButton("Volver a la pantalla principal")
        boton_volver.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_volver.setFixedSize(200, 40)
        boton_volver.clicked.connect(self.volver_a_principal)

        boton_actualizar = QPushButton("Actualizar")
        boton_actualizar.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_actualizar.setFixedSize(120, 40)

        boton_eliminar = QPushButton("Eliminar")
        boton_eliminar.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_eliminar.setFixedSize(120, 40)
        boton_eliminar.clicked.connect(self.mostrar_popup_eliminar)

        boton_agregar = QPushButton("Agregar")
        boton_agregar.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_agregar.setFixedSize(120, 40)
        boton_agregar.clicked.connect(self.agregar_cliente)

        layout_cliente.addWidget(boton_volver, 5, 0, 1, 1)
        layout_cliente.addWidget(boton_actualizar, 5, 1, 1, 1)
        layout_cliente.addWidget(boton_eliminar, 5, 2, 1, 1)
        layout_cliente.addWidget(boton_agregar, 5, 3, 1, 1)

        self.setLayout(layout_cliente)
        self.parent = parent

    def agregar_cliente(self):
        clienteAgregar = ClienteController() 
        condicion = clienteAgregar.validacionGuardarCliente(self)
        if (condicion):
            QMessageBox.information(self, "Éxito", "Cliente agregado exitosamente.")
        else:
            QMessageBox.information(self, "Informacion", "Campos vacios.")

    def mostrar_popup_eliminar(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Eliminar Cliente")

        layout = QVBoxLayout()

        label = QLabel("Ingrese el ID del cliente a eliminar:")
        layout.addWidget(label)

        self.id_cliente_eliminar_edit = QLineEdit()
        self.id_cliente_eliminar_edit.setStyleSheet("background-color: white;")
        layout.addWidget(self.id_cliente_eliminar_edit)

        boton_eliminar_confirmar = QPushButton("Eliminar")
        boton_eliminar_confirmar.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_eliminar_confirmar.setFixedSize(120, 40)
        boton_eliminar_confirmar.clicked.connect(self.eliminar_cliente)

        layout.addWidget(boton_eliminar_confirmar)

        dialog.setLayout(layout)
        dialog.exec()

    def eliminar_cliente(self):
        pass


    def volver_a_principal(self):
        self.close()
        self.parent.show()

class SucursalWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle('Sucursal')
        self.setGeometry(100, 100, 600, 400)

        self.setStyleSheet("background-color: lightblue;")

        layout_sucursal = QGridLayout()

        # Campo de entrada para la dirección de la sucursal
        layout_sucursal.addWidget(QLabel("Dirección de la Sucursal:"), 0, 0)
        self.direccion_sucursal_edit = QLineEdit()
        self.direccion_sucursal_edit.setStyleSheet("background-color: white;")
        layout_sucursal.addWidget(self.direccion_sucursal_edit, 0, 1)

        # Campo de entrada para el teléfono de la sucursal
        layout_sucursal.addWidget(QLabel("Teléfono de la Sucursal:"), 1, 0)
        self.telefono_sucursal_edit = QLineEdit()
        self.telefono_sucursal_edit.setStyleSheet("background-color: white;")
        layout_sucursal.addWidget(self.telefono_sucursal_edit, 1, 1)

        # Campo de entrada para el email de la sucursal
        layout_sucursal.addWidget(QLabel("Email de la Sucursal:"), 2, 0)
        self.email_sucursal_edit = QLineEdit()
        self.email_sucursal_edit.setStyleSheet("background-color: white;")
        layout_sucursal.addWidget(self.email_sucursal_edit, 2, 1)

        # Campo de entrada para la cédula del jefe de la sucursal
        layout_sucursal.addWidget(QLabel("Cédula del Jefe de la Sucursal:"), 3, 0)
        self.cedula_jefe_sucursal_edit = QLineEdit()
        self.cedula_jefe_sucursal_edit.setStyleSheet("background-color: white;")
        layout_sucursal.addWidget(self.cedula_jefe_sucursal_edit, 3, 1)

        # Campo de entrada para seleccionar la ciudad de la sucursal
        layout_sucursal.addWidget(QLabel("Ciudad de la Sucursal:"), 4, 0)
        self.ciudad_sucursal_combobox = QComboBox()
        self.ciudad_sucursal_combobox.setStyleSheet("background-color: white;")
        ciudades = BDCiudad()
        self.ciudad_sucursal_combobox.addItems(ciudades.listarCiudades())  # Ejemplo de ciudades
        layout_sucursal.addWidget(self.ciudad_sucursal_combobox, 4, 1)

        # Botones
        boton_volver = QPushButton("Volver a la pantalla principal")
        boton_volver.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_volver.setFixedSize(200, 40)
        boton_volver.clicked.connect(self.volver_a_principal)

        boton_actualizar = QPushButton("Actualizar")
        boton_actualizar.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_actualizar.setFixedSize(120, 40)

        boton_eliminar = QPushButton("Eliminar")
        boton_eliminar.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_eliminar.setFixedSize(120, 40)
        boton_eliminar.clicked.connect(self.mostrar_popup_eliminar)

        boton_agregar = QPushButton("Agregar")
        boton_agregar.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_agregar.setFixedSize(120, 40)
        boton_agregar.clicked.connect(self.agregar_sucursal)

        boton_generar_reporte = QPushButton("Generar reporte")
        boton_generar_reporte.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_generar_reporte.setFixedSize(120, 40)
        boton_generar_reporte.clicked.connect(self.generar_reporte)

        layout_sucursal.addWidget(boton_volver, 5, 0, 1, 1)
        layout_sucursal.addWidget(boton_actualizar, 5, 1, 1, 1)
        layout_sucursal.addWidget(boton_eliminar, 5, 2, 1, 1)
        layout_sucursal.addWidget(boton_agregar, 5, 3, 1, 1)
        layout_sucursal.addWidget(boton_generar_reporte, 6, 0, 1, 1) 

        self.setLayout(layout_sucursal)
        self.parent = parent

    def agregar_sucursal(self):

        sucursalAgregar = SucursalController() 
        condicion = sucursalAgregar.validacionGuardarSucursal(self)
        if (condicion):
            QMessageBox.information(self, "Éxito", "Sucursal agregada exitosamente.")
            self.direccion_sucursal_edit.setText("")
            self.telefono_sucursal_edit.setText("")
            self.telefono_sucursal_edit.setText("")
            self.email_sucursal_edit.setText("")
            self.cedula_jefe_sucursal_edit.setText("")
            self.ciudad_sucursal_combobox.setCurrentIndex(0)
        else:
            QMessageBox.information(self, "Informacion", "Campos vacios.")

    def generar_reporte(self):
        sucursalReporte = SucursalReport()
        sucursalReporte.reporte()

        # Obtener la ruta del directorio de trabajo actual
        directorio_actual = os.getcwd()
        
        # Concatenar la ruta del archivo PDF
        pdf_nombre = "ReporteSucursal.pdf"
        pdf_path = os.path.join(directorio_actual + "/app/Reportes/", pdf_nombre)
        
        # Abrir el PDF en el navegador
        webbrowser.open_new(pdf_path)   

    def mostrar_popup_eliminar(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Eliminar Sucursal")

        layout = QVBoxLayout()

        label = QLabel("Ingrese el ID de la sucursal a eliminar:")
        layout.addWidget(label)

        self.id_sucursal_eliminar_edit = QLineEdit()
        self.id_sucursal_eliminar_edit.setStyleSheet("background-color: white;")
        layout.addWidget(self.id_sucursal_eliminar_edit)

        boton_eliminar_confirmar = QPushButton("Eliminar")
        boton_eliminar_confirmar.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_eliminar_confirmar.setFixedSize(120, 40)
        boton_eliminar_confirmar.clicked.connect(self.eliminar_sucursal)

        layout.addWidget(boton_eliminar_confirmar)

        dialog.setLayout(layout)
        dialog.exec()

    def eliminar_sucursal(self):
        sucursalEliminar = SucursalController()
        condicion = sucursalEliminar.validacionEliminar(self)
        if (condicion):
            QMessageBox.information(self, "Éxito", "Sucursal eliminada exitosamente.")
        else:
            QMessageBox.information(self, "Informacion", "Campos vacios.")
       

    def volver_a_principal(self):
        self.close()
        self.parent.show()

class ProductoWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle('Producto')
        self.setGeometry(100, 100, 600, 400)

        self.setStyleSheet("background-color: lightblue;")

        layout_producto = QGridLayout()

        # Campo de entrada para el nombre del producto
        layout_producto.addWidget(QLabel("Nombre del Producto:"), 0, 0)
        self.nombre_producto_edit = QLineEdit()
        self.nombre_producto_edit.setStyleSheet("background-color: white;")
        layout_producto.addWidget(self.nombre_producto_edit, 0, 1)

        # Campo de entrada para la descripción del producto
        layout_producto.addWidget(QLabel("Descripción del Producto:"), 1, 0)
        self.descripcion_producto_edit = QLineEdit()
        self.descripcion_producto_edit.setStyleSheet("background-color: white;")
        layout_producto.addWidget(self.descripcion_producto_edit, 1, 1)

        # Campo de entrada para el precio del producto
        layout_producto.addWidget(QLabel("Precio del Producto:"), 2, 0)
        self.precio_producto_edit = QLineEdit()
        self.precio_producto_edit.setStyleSheet("background-color: white;")
        layout_producto.addWidget(self.precio_producto_edit, 2, 1)

        # Campo de entrada para la cantidad del producto
        layout_producto.addWidget(QLabel("Cantidad del Producto:"), 3, 0)
        self.cantidad_producto_edit = QLineEdit()
        self.cantidad_producto_edit.setStyleSheet("background-color: white;")
        layout_producto.addWidget(self.cantidad_producto_edit, 3, 1)

        # Botones
        boton_volver = QPushButton("Volver a la pantalla principal")
        boton_volver.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_volver.setFixedSize(200, 40)
        boton_volver.clicked.connect(self.volver_a_principal)

        boton_actualizar = QPushButton("Actualizar")
        boton_actualizar.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_actualizar.setFixedSize(120, 40)

        boton_eliminar = QPushButton("Eliminar")
        boton_eliminar.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_eliminar.setFixedSize(120, 40)
        boton_eliminar.clicked.connect(self.mostrar_popup_eliminar)

        boton_agregar = QPushButton("Agregar")
        boton_agregar.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_agregar.setFixedSize(120, 40)
        boton_agregar.clicked.connect(self.agregar_producto)

        layout_producto.addWidget(boton_volver, 4, 0, 1, 1)
        layout_producto.addWidget(boton_actualizar, 4, 1, 1, 1)
        layout_producto.addWidget(boton_eliminar, 4, 2, 1, 1)
        layout_producto.addWidget(boton_agregar, 4, 3, 1, 1)

        self.setLayout(layout_producto)
        self.parent = parent

    def agregar_producto(self):
        productoAgregar = ProductoController() 
        condicion = productoAgregar.validacionGuardarProducto(self)
        if (condicion):
            QMessageBox.information(self, "Éxito", "Producto agregado exitosamente.")
            self.nombre_producto_edit.setText("")
            self.descripcion_producto_edit.setText("")
            self.precio_producto_edit.setText("")
            self.cantidad_producto_edit.setText("")
        else:
            QMessageBox.information(self, "Informacion", "Campos vacios.")

    def mostrar_popup_eliminar(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Eliminar Producto")

        layout = QVBoxLayout()

        label = QLabel("Ingrese el ID del producto a eliminar:")
        layout.addWidget(label)

        self.id_producto_eliminar_edit = QLineEdit()
        self.id_producto_eliminar_edit.setStyleSheet("background-color: white;")
        layout.addWidget(self.id_producto_eliminar_edit)

        boton_eliminar_confirmar = QPushButton("Eliminar")
        boton_eliminar_confirmar.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_eliminar_confirmar.setFixedSize(120, 40)
        boton_eliminar_confirmar.clicked.connect(self.eliminar_producto)

        layout.addWidget(boton_eliminar_confirmar)

        dialog.setLayout(layout)
        dialog.exec()

    def eliminar_producto(self):
        productoEliminar = ProductoController()
        condicion = productoEliminar.validacionEliminar(self)
        if (condicion):
            QMessageBox.information(self, "Éxito", "Producto eliminado exitosamente.")
        else:
            QMessageBox.information(self, "Informacion", "Campos vacios.")

    def volver_a_principal(self):
        self.close()
        self.parent.show()

class FacturaWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle('Factura')
        self.setGeometry(100, 100, 600, 400)

        self.setStyleSheet("background-color: lightblue;")

        layout_factura = QGridLayout()

        # Campo de entrada para la fecha de la factura
        layout_factura.addWidget(QLabel("Fecha de la Factura:"), 0, 0)
        self.fecha_factura_calendar = QDateEdit()
        self.fecha_factura_calendar.setCalendarPopup(True)
        self.fecha_factura_calendar.setStyleSheet("background-color: white; color:black;")
        layout_factura.addWidget(self.fecha_factura_calendar, 0, 1)

        # Campo de entrada para el total de la factura
        layout_factura.addWidget(QLabel("Total de la Factura:"), 1, 0)
        self.total_factura_edit = QLineEdit()
        self.total_factura_edit.setStyleSheet("background-color: white;")
        layout_factura.addWidget(self.total_factura_edit, 1, 1)

        # Campo de entrada para el ID del cliente
        layout_factura.addWidget(QLabel("ID del Cliente:"), 2, 0)
        self.id_cliente_edit = QLineEdit()
        self.id_cliente_edit.setStyleSheet("background-color: white;")
        layout_factura.addWidget(self.id_cliente_edit, 2, 1)

        # Campo de entrada para la cédula del vendedor
        layout_factura.addWidget(QLabel("Cédula del Vendedor:"), 3, 0)
        self.cedula_vendedor_edit = QLineEdit()
        self.cedula_vendedor_edit.setStyleSheet("background-color: white;")
        layout_factura.addWidget(self.cedula_vendedor_edit, 3, 1)

        # Botones
        boton_volver = QPushButton("Volver a la pantalla principal")
        boton_volver.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_volver.setFixedSize(200, 40)
        boton_volver.clicked.connect(self.volver_a_principal)

        boton_actualizar = QPushButton("Actualizar")
        boton_actualizar.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_actualizar.setFixedSize(120, 40)

        boton_eliminar = QPushButton("Eliminar")
        boton_eliminar.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_eliminar.setFixedSize(120, 40)

        boton_agregar = QPushButton("Agregar")
        boton_agregar.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_agregar.setFixedSize(120, 40)
        boton_agregar.clicked.connect(self.agregar_factura)

        layout_factura.addWidget(boton_volver, 4, 0, 1, 1)
        layout_factura.addWidget(boton_actualizar, 4, 1, 1, 1)
        layout_factura.addWidget(boton_eliminar, 4, 2, 1, 1)
        layout_factura.addWidget(boton_agregar, 4, 3, 1, 1)

        self.setLayout(layout_factura)
        self.parent = parent

    def agregar_factura(self):
        facturaAgregar = FacturaController() 
        condicion = facturaAgregar.validacionGuardarFactura(self)
        if (condicion):
            QMessageBox.information(self, "Éxito", "Factura agregado exitosamente.")
        else:
            QMessageBox.information(self, "Informacion", "Campos vacios.")

    def volver_a_principal(self):
        self.close()
        self.parent.show()
    
class ProveedorWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle('Proveedor')
        self.setGeometry(100, 100, 600, 400)

        self.setStyleSheet("background-color: lightblue;")

        layout_proveedor = QGridLayout()

        # Campo de entrada para el nombre del proveedor
        layout_proveedor.addWidget(QLabel("Nombre del Proveedor:"), 0, 0)
        self.nombre_proveedor_edit = QLineEdit()
        self.nombre_proveedor_edit.setStyleSheet("background-color: white;")
        layout_proveedor.addWidget(self.nombre_proveedor_edit, 0, 1)

        # Campo de entrada para la dirección del proveedor
        layout_proveedor.addWidget(QLabel("Dirección del Proveedor:"), 1, 0)
        self.direccion_proveedor_edit = QLineEdit()
        self.direccion_proveedor_edit.setStyleSheet("background-color: white;")
        layout_proveedor.addWidget(self.direccion_proveedor_edit, 1, 1)

        # Campo de entrada para el email del proveedor
        layout_proveedor.addWidget(QLabel("Email del Proveedor:"), 2, 0)
        self.email_proveedor_edit = QLineEdit()
        self.email_proveedor_edit.setStyleSheet("background-color: white;")
        layout_proveedor.addWidget(self.email_proveedor_edit, 2, 1)

        # Campo de entrada para el teléfono del proveedor
        layout_proveedor.addWidget(QLabel("Teléfono del Proveedor:"), 3, 0)
        self.telefono_proveedor_edit = QLineEdit()
        self.telefono_proveedor_edit.setStyleSheet("background-color: white;")
        layout_proveedor.addWidget(self.telefono_proveedor_edit, 3, 1)

        # Botones
        boton_volver = QPushButton("Volver a la pantalla principal")
        boton_volver.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_volver.setFixedSize(200, 40)
        boton_volver.clicked.connect(self.volver_a_principal)

        boton_actualizar = QPushButton("Actualizar")
        boton_actualizar.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_actualizar.setFixedSize(120, 40)

        boton_eliminar = QPushButton("Eliminar")
        boton_eliminar.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_eliminar.setFixedSize(120, 40)

        boton_agregar = QPushButton("Agregar")
        boton_agregar.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_agregar.setFixedSize(120, 40)
        boton_agregar.clicked.connect(self.agregar_proveedor)

        layout_proveedor.addWidget(boton_volver, 4, 0, 1, 1)
        layout_proveedor.addWidget(boton_actualizar, 4, 1, 1, 1)
        layout_proveedor.addWidget(boton_eliminar, 4, 2, 1, 1)
        layout_proveedor.addWidget(boton_agregar, 4, 3, 1, 1)

        self.setLayout(layout_proveedor)
        self.parent = parent

    def agregar_proveedor(self):
        proveedorAgregar = ProveedorController() 
        condicion = proveedorAgregar.validacionGuardarProveedor(self)
        if (condicion):
            QMessageBox.information(self, "Éxito", "Proveedor agregado exitosamente.")
        else:
            QMessageBox.information(self, "Informacion", "Campos vacios.")

    def volver_a_principal(self):
        self.close()
        self.parent.show()

class MaterialWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle('Material')
        self.setGeometry(100, 100, 600, 400)

        self.setStyleSheet("background-color: lightblue;")

        layout_material = QGridLayout()

        # Campo de entrada para el nombre del material
        layout_material.addWidget(QLabel("Nombre del Material:"), 0, 0)
        self.nombre_material_edit = QLineEdit()
        self.nombre_material_edit.setStyleSheet("background-color: white;")
        layout_material.addWidget(self.nombre_material_edit, 0, 1)

        # Campo de entrada para la descripción del material
        layout_material.addWidget(QLabel("Descripción del Material:"), 1, 0)
        self.descripcion_material_edit = QLineEdit()
        self.descripcion_material_edit.setStyleSheet("background-color: white;")
        layout_material.addWidget(self.descripcion_material_edit, 1, 1)

        # Campo de entrada para la cantidad del material
        layout_material.addWidget(QLabel("Cantidad del Material:"), 2, 0)
        self.cantidad_material_edit = QLineEdit()
        self.cantidad_material_edit.setStyleSheet("background-color: white;")
        layout_material.addWidget(self.cantidad_material_edit, 2, 1)

        # Botones
        boton_volver = QPushButton("Volver a la pantalla principal")
        boton_volver.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_volver.setFixedSize(200, 40)
        boton_volver.clicked.connect(self.volver_a_principal)

        boton_actualizar = QPushButton("Actualizar")
        boton_actualizar.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_actualizar.setFixedSize(120, 40)

        boton_eliminar = QPushButton("Eliminar")
        boton_eliminar.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_eliminar.setFixedSize(120, 40)

        boton_agregar = QPushButton("Agregar")
        boton_agregar.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_agregar.setFixedSize(120, 40)
        boton_agregar.clicked.connect(self.agregar_material)

        layout_material.addWidget(boton_volver, 3, 0, 1, 1)
        layout_material.addWidget(boton_actualizar, 3, 1, 1, 1)
        layout_material.addWidget(boton_eliminar, 3, 2, 1, 1)
        layout_material.addWidget(boton_agregar, 3, 3, 1, 1)

        self.setLayout(layout_material)
        self.parent = parent

    def agregar_material(self):
        materialAgregar = MateriaPrimaController() 
        condicion = materialAgregar.validacionGuardarMateriaPrima(self)
        if (condicion):
            QMessageBox.information(self, "Éxito", "Materia prima agregada exitosamente.")
        else:
            QMessageBox.information(self, "Informacion", "Campos vacios.")

    def volver_a_principal(self):
        self.close()
        self.parent.show()
    
class CotizacionWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle('Cotización')
        self.setGeometry(100, 100, 600, 400)

        self.setStyleSheet("background-color: lightblue;")

        layout_cotizacion = QGridLayout()

        # Campo de entrada para la fecha de la cotización
        layout_cotizacion.addWidget(QLabel("Fecha de la Cotización:"), 0, 0)
        self.fecha_cotizacion_calendar = QDateEdit()
        self.fecha_cotizacion_calendar.setCalendarPopup(True)
        self.fecha_cotizacion_calendar.setStyleSheet("background-color: white; color:black;")
        layout_cotizacion.addWidget(self.fecha_cotizacion_calendar, 0, 1)

        # Campo de entrada para el total de la cotización
        layout_cotizacion.addWidget(QLabel("Total de la Cotización:"), 1, 0)
        self.total_cotizacion_edit = QLineEdit()
        self.total_cotizacion_edit.setStyleSheet("background-color: white;")
        layout_cotizacion.addWidget(self.total_cotizacion_edit, 1, 1)

        # Campo de entrada para la cédula del vendedor
        layout_cotizacion.addWidget(QLabel("Cédula del Vendedor:"), 2, 0)
        self.cedula_vendedor_edit = QLineEdit()
        self.cedula_vendedor_edit.setStyleSheet("background-color: white;")
        layout_cotizacion.addWidget(self.cedula_vendedor_edit, 2, 1)

        # Botones
        boton_volver = QPushButton("Volver a la pantalla principal")
        boton_volver.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_volver.setFixedSize(200, 40)
        boton_volver.clicked.connect(self.volver_a_principal)

        boton_actualizar = QPushButton("Actualizar")
        boton_actualizar.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_actualizar.setFixedSize(120, 40)

        boton_eliminar = QPushButton("Eliminar")
        boton_eliminar.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_eliminar.setFixedSize(120, 40)

        boton_agregar = QPushButton("Agregar")
        boton_agregar.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_agregar.setFixedSize(120, 40)
        boton_agregar.clicked.connect(self.agregar_cotizacion)

        layout_cotizacion.addWidget(boton_volver, 3, 0, 1, 1)
        layout_cotizacion.addWidget(boton_actualizar, 3, 1, 1, 1)
        layout_cotizacion.addWidget(boton_eliminar, 3, 2, 1, 1)
        layout_cotizacion.addWidget(boton_agregar, 3, 3, 1, 1)

        self.setLayout(layout_cotizacion)
        self.parent = parent

    def agregar_cotizacion(self):
        cotizacionAgregar = CotizacionController()
        condicion = cotizacionAgregar.validacionGuardarCotizacion(self)
        if (condicion):
            QMessageBox.information(self, "Éxito", "Cotizacion agregada exitosamente.")
        else:
            QMessageBox.information(self, "Informacion", "Campos vacios.")

    def volver_a_principal(self):
        self.close()
        self.parent.show()

class EntregaPedidoWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle('Entrega de Pedido')
        self.setGeometry(100, 100, 600, 400)

        self.setStyleSheet("background-color: lightblue;")

        layout_entrega_pedido = QGridLayout()

        # Campo de entrada para la cédula del bodeguero
        layout_entrega_pedido.addWidget(QLabel("Cédula del Bodeguero:"), 0, 0)
        self.cedula_bodeguero_edit = QLineEdit()
        self.cedula_bodeguero_edit.setStyleSheet("background-color: white;")
        layout_entrega_pedido.addWidget(self.cedula_bodeguero_edit, 0, 1)

        # Campo de entrada para el ID de la factura
        layout_entrega_pedido.addWidget(QLabel("ID de la Factura:"), 1, 0)
        self.id_factura_edit = QLineEdit()
        self.id_factura_edit.setStyleSheet("background-color: white;")
        layout_entrega_pedido.addWidget(self.id_factura_edit, 1, 1)

        # Campo de entrada para la fecha de entrega
        layout_entrega_pedido.addWidget(QLabel("Fecha de Entrega:"), 2, 0)
        self.fecha_entrega_calendar = QDateEdit()
        self.fecha_entrega_calendar.setCalendarPopup(True)
        self.fecha_entrega_calendar.setStyleSheet("background-color: white; color:black;")
        layout_entrega_pedido.addWidget(self.fecha_entrega_calendar, 2, 1)

        # Campo de entrada para el estado del pedido
        layout_entrega_pedido.addWidget(QLabel("Estado del Pedido:"), 3, 0)
        self.estado_pedido_edit = QLineEdit()
        self.estado_pedido_edit.setStyleSheet("background-color: white;")
        layout_entrega_pedido.addWidget(self.estado_pedido_edit, 3, 1)

        # Campo de entrada para la cédula del distribuidor
        layout_entrega_pedido.addWidget(QLabel("Cédula del Distribuidor:"), 4, 0)
        self.cedula_distribuidor_edit = QLineEdit()
        self.cedula_distribuidor_edit.setStyleSheet("background-color: white;")
        layout_entrega_pedido.addWidget(self.cedula_distribuidor_edit, 4, 1)

        # Botones
        boton_volver = QPushButton("Volver a la pantalla principal")
        boton_volver.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_volver.setFixedSize(200, 40)
        boton_volver.clicked.connect(self.volver_a_principal)

        boton_actualizar = QPushButton("Actualizar")
        boton_actualizar.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_actualizar.setFixedSize(120, 40)

        boton_eliminar = QPushButton("Eliminar")
        boton_eliminar.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_eliminar.setFixedSize(120, 40)

        boton_agregar = QPushButton("Agregar")
        boton_agregar.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_agregar.setFixedSize(120, 40)
        boton_agregar.clicked.connect(self.agregar_entrega_pedido)

        layout_entrega_pedido.addWidget(boton_volver, 6, 0, 1, 1)
        layout_entrega_pedido.addWidget(boton_actualizar, 6, 1, 1, 1)
        layout_entrega_pedido.addWidget(boton_eliminar, 6, 2, 1, 1)
        layout_entrega_pedido.addWidget(boton_agregar, 6, 3, 1, 1)

        self.setLayout(layout_entrega_pedido)
        self.parent = parent
    
    def agregar_entrega_pedido(self):
        entregaPedidoAgregar = PedidoEntregaController()
        condicion = entregaPedidoAgregar.validacionGuardarPedidoEntrega(self)
        if (condicion):
            QMessageBox.information(self, "Éxito", "Entrega de Pedido agregada exitosamente.")
        else:
            QMessageBox.information(self, "Informacion", "Campos vacios.")

    def volver_a_principal(self):
        self.close()
        self.parent.show()
    
class DespachoPedidoWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle('Despacho de Pedido')
        self.setGeometry(100, 100, 600, 400)

        self.setStyleSheet("background-color: lightblue;")

        layout_despacho_pedido = QGridLayout()

        # Campo de entrada para la cédula del bodeguero
        layout_despacho_pedido.addWidget(QLabel("Cédula del Bodeguero:"), 0, 0)
        self.cedula_bodeguero_edit = QLineEdit()
        self.cedula_bodeguero_edit.setStyleSheet("background-color: white;")
        layout_despacho_pedido.addWidget(self.cedula_bodeguero_edit, 0, 1)

        # Campo de entrada para el ID de la factura
        layout_despacho_pedido.addWidget(QLabel("ID de la Factura:"), 1, 0)
        self.id_factura_edit = QLineEdit()
        self.id_factura_edit.setStyleSheet("background-color: white;")
        layout_despacho_pedido.addWidget(self.id_factura_edit, 1, 1)

        # Campo de entrada para la fecha de despacho
        layout_despacho_pedido.addWidget(QLabel("Fecha de Despacho:"), 2, 0)
        self.fecha_despacho_calendar = QDateEdit()
        self.fecha_despacho_calendar.setCalendarPopup(True)
        self.fecha_despacho_calendar.setStyleSheet("background-color: white; color:black;")
        layout_despacho_pedido.addWidget(self.fecha_despacho_calendar, 2, 1)

        # Campo de entrada para el estado del pedido
        layout_despacho_pedido.addWidget(QLabel("Estado del Pedido:"), 3, 0)
        self.estado_pedido_edit = QLineEdit()
        self.estado_pedido_edit.setStyleSheet("background-color: white;")
        layout_despacho_pedido.addWidget(self.estado_pedido_edit, 3, 1)

        # Botones
        boton_volver = QPushButton("Volver a la pantalla principal")
        boton_volver.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_volver.setFixedSize(200, 40)
        boton_volver.clicked.connect(self.volver_a_principal)

        boton_actualizar = QPushButton("Actualizar")
        boton_actualizar.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_actualizar.setFixedSize(120, 40)

        boton_eliminar = QPushButton("Eliminar")
        boton_eliminar.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_eliminar.setFixedSize(120, 40)

        boton_agregar = QPushButton("Agregar")
        boton_agregar.setStyleSheet("background-color: lightgreen; color: black; border: 2px solid black; border-radius: 10px;")
        boton_agregar.setFixedSize(120, 40)
        boton_agregar.clicked.connect(self.agregar_despacho_pedido)

        layout_despacho_pedido.addWidget(boton_volver, 6, 0, 1, 1)
        layout_despacho_pedido.addWidget(boton_actualizar, 6, 1, 1, 1)
        layout_despacho_pedido.addWidget(boton_eliminar, 6, 2, 1, 1)
        layout_despacho_pedido.addWidget(boton_agregar, 6, 3, 1, 1)

        self.setLayout(layout_despacho_pedido)
        self.parent = parent

    def agregar_despacho_pedido(self):
        despachoPedidoAgregar = PedidoDespacharController()
        condicion = despachoPedidoAgregar.validacionGuardarPedidoDespachar(self)
        if (condicion):
            QMessageBox.information(self, "Éxito", "Despacho de Pedido agregado exitosamente.")
        else:
            QMessageBox.information(self, "Informacion", "Campos vacios.")

    def volver_a_principal(self):
        self.close()
        self.parent.show()
    


