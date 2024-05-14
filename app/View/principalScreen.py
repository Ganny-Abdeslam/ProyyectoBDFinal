from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QGridLayout, QLabel, QLineEdit, QComboBox, QCalendarWidget

class PrincipalScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Tienda BuhoVigia')
        self.setGeometry(100, 100, 400, 300)

        layout = QGridLayout()

        botones = ['Usuario', 'Cliente', 'Sucursal', 'Producto', 'Factura', 'Proveedor', 'Material', 'Cotización', 'Entrega de pedidos', 'Despacho de pedidos']
        fila = 0
        columna = 0
        for texto_boton in botones:
            boton = QPushButton(texto_boton)
            boton.setFixedSize(150, 50)
            layout.addWidget(boton, fila, columna)
            columna += 1
            if columna == 2:
                columna = 0
                fila += 1

            boton.clicked.connect(lambda _, texto=texto_boton: self.abrir_ventana(texto))

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

        layout_usuario = QGridLayout()

        # Campo de entrada para la cédula
        layout_usuario.addWidget(QLabel("Cédula:"), 0, 0)
        self.cedula_edit = QLineEdit()
        layout_usuario.addWidget(self.cedula_edit, 0, 1)

        # Campo de entrada para el primer nombre
        layout_usuario.addWidget(QLabel("Primer Nombre:"), 1, 0)
        self.primer_nombre_edit = QLineEdit()
        layout_usuario.addWidget(self.primer_nombre_edit, 1, 1)

        # Campo de entrada para el segundo nombre
        layout_usuario.addWidget(QLabel("Segundo Nombre:"), 2, 0)
        self.segundo_nombre_edit = QLineEdit()
        layout_usuario.addWidget(self.segundo_nombre_edit, 2, 1)

        # Campo de entrada para el primer apellido
        layout_usuario.addWidget(QLabel("Primer Apellido:"), 3, 0)
        self.primer_apellido_edit = QLineEdit()
        layout_usuario.addWidget(self.primer_apellido_edit, 3, 1)

        # Campo de entrada para el segundo apellido
        layout_usuario.addWidget(QLabel("Segundo Apellido:"), 4, 0)
        self.segundo_apellido_edit = QLineEdit()
        layout_usuario.addWidget(self.segundo_apellido_edit, 4, 1)

        # Campo de entrada para la fecha de nacimiento
        layout_usuario.addWidget(QLabel("Fecha de Nacimiento:"), 5, 0)
        self.fecha_nacimiento_calendar = QCalendarWidget()
        layout_usuario.addWidget(self.fecha_nacimiento_calendar, 5, 1)

        # Campo de entrada para el teléfono
        layout_usuario.addWidget(QLabel("Teléfono:"), 6, 0)
        self.telefono_edit = QLineEdit()
        layout_usuario.addWidget(self.telefono_edit, 6, 1)

        # Campo de entrada para la dirección
        layout_usuario.addWidget(QLabel("Dirección:"), 7, 0)
        self.direccion_edit = QLineEdit()
        layout_usuario.addWidget(self.direccion_edit, 7, 1)

        # Campo de entrada para el email
        layout_usuario.addWidget(QLabel("Email:"), 8, 0)
        self.email_edit = QLineEdit()
        layout_usuario.addWidget(self.email_edit, 8, 1)

        # Campo de entrada para el salario
        layout_usuario.addWidget(QLabel("Salario:"), 9, 0)
        self.salario_edit = QLineEdit()
        layout_usuario.addWidget(self.salario_edit, 9, 1)

        # Campo de entrada para el username
        layout_usuario.addWidget(QLabel("Username:"), 10, 0)
        self.username_edit = QLineEdit()
        layout_usuario.addWidget(self.username_edit, 10, 1)

        # Campo de entrada para el password
        layout_usuario.addWidget(QLabel("Password:"), 11, 0)
        self.password_edit = QLineEdit()
        layout_usuario.addWidget(self.password_edit, 11, 1)

        # Campo de entrada para el tipo de usuario
        layout_usuario.addWidget(QLabel("Tipo de Usuario:"), 12, 0)
        self.tipo_usuario_combobox = QComboBox()
        self.tipo_usuario_combobox.addItem("Seleccione tipo")  # Título no seleccionable
        self.tipo_usuario_combobox.addItems(["Distribuidor", "Bodeguero", "Vendedor"])
        layout_usuario.addWidget(self.tipo_usuario_combobox, 12, 1)

        # Campo de entrada para la comisión (solo para Vendedor)
        self.comision_label = QLabel("Comisión:")
        self.comision_edit = QLineEdit()
        layout_usuario.addWidget(self.comision_label, 13, 0)
        layout_usuario.addWidget(self.comision_edit, 13, 1)

        # Campo de entrada para la placa del vehículo (solo para Distribuidor)
        self.placa_label = QLabel("Placa del vehículo:")
        self.placa_edit = QLineEdit()
        layout_usuario.addWidget(self.placa_label, 14, 0)
        layout_usuario.addWidget(self.placa_edit, 14, 1)

        # Campo de entrada para el nombre del jefe (solo para Bodeguero)
        self.nombre_jefe_label = QLabel("Cedula del jefe:")
        self.nombre_jefe_edit = QLineEdit()
        layout_usuario.addWidget(self.nombre_jefe_label, 15, 0)
        layout_usuario.addWidget(self.nombre_jefe_edit, 15, 1)

        boton_volver = QPushButton("Volver a la pantalla principal")
        boton_volver.clicked.connect(self.volver_a_principal)
        layout_usuario.addWidget(boton_volver, 16, 0, 1, 2)

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

        elif index == 3:
            # Si el usuario selecciona "Vendedor", mostrar campo de Comisión
            self.comision_label.show()
            self.comision_edit.show()
            self.placa_label.hide()
            self.placa_edit.hide()
            self.nombre_jefe_label.hide()
            self.nombre_jefe_edit.hide()

    def volver_a_principal(self):
        self.close()
        self.parent.show()

class ClienteWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle('Cliente')
        self.setGeometry(100, 100, 400, 300)

        layout_usuario = QVBoxLayout()
        etiqueta = QLabel("Esta es la ventana para los clientes")
        layout_usuario.addWidget(etiqueta)

        boton_volver = QPushButton("Volver a la pantalla principal")
        boton_volver.clicked.connect(self.volver_a_principal)
        layout_usuario.addWidget(boton_volver)

        self.setLayout(layout_usuario)
        self.parent = parent

    def volver_a_principal(self):
        self.close()
        self.parent.show()

class SucursalWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle('Sucursal')
        self.setGeometry(100, 100, 400, 300)

        layout_usuario = QVBoxLayout()
        etiqueta = QLabel("Esta es la ventana para las sucursales")
        layout_usuario.addWidget(etiqueta)

        boton_volver = QPushButton("Volver a la pantalla principal")
        boton_volver.clicked.connect(self.volver_a_principal)
        layout_usuario.addWidget(boton_volver)

        self.setLayout(layout_usuario)
        self.parent = parent

    def volver_a_principal(self):
        self.close()
        self.parent.show()

class ProductoWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle('Producto')
        self.setGeometry(100, 100, 400, 300)

        layout_usuario = QVBoxLayout()
        etiqueta = QLabel("Esta es la ventana para los productos")
        layout_usuario.addWidget(etiqueta)

        boton_volver = QPushButton("Volver a la pantalla principal")
        boton_volver.clicked.connect(self.volver_a_principal)
        layout_usuario.addWidget(boton_volver)

        self.setLayout(layout_usuario)
        self.parent = parent

    def volver_a_principal(self):
        self.close()
        self.parent.show()

class FacturaWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle('Factura')
        self.setGeometry(100, 100, 400, 300)

        layout_usuario = QVBoxLayout()
        etiqueta = QLabel("Esta es la ventana para las facturas")
        layout_usuario.addWidget(etiqueta)

        boton_volver = QPushButton("Volver a la pantalla principal")
        boton_volver.clicked.connect(self.volver_a_principal)
        layout_usuario.addWidget(boton_volver)

        self.setLayout(layout_usuario)
        self.parent = parent

    def volver_a_principal(self):
        self.close()
        self.parent.show()
    
class ProveedorWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle('Proveedor')
        self.setGeometry(100, 100, 400, 300)

        layout_usuario = QVBoxLayout()
        etiqueta = QLabel("Esta es la ventana para los proveedor")
        layout_usuario.addWidget(etiqueta)

        boton_volver = QPushButton("Volver a la pantalla principal")
        boton_volver.clicked.connect(self.volver_a_principal)
        layout_usuario.addWidget(boton_volver)

        self.setLayout(layout_usuario)
        self.parent = parent

    def volver_a_principal(self):
        self.close()
        self.parent.show()

class MaterialWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle('Material')
        self.setGeometry(100, 100, 400, 300)

        layout_usuario = QVBoxLayout()
        etiqueta = QLabel("Esta es la ventana para los materiales")
        layout_usuario.addWidget(etiqueta)

        boton_volver = QPushButton("Volver a la pantalla principal")
        boton_volver.clicked.connect(self.volver_a_principal)
        layout_usuario.addWidget(boton_volver)

        self.setLayout(layout_usuario)
        self.parent = parent

    def volver_a_principal(self):
        self.close()
        self.parent.show()
    
class CotizacionWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle('Cotizacion')
        self.setGeometry(100, 100, 400, 300)

        layout_usuario = QVBoxLayout()
        etiqueta = QLabel("Esta es la ventana para las cotizaciones")
        layout_usuario.addWidget(etiqueta)

        boton_volver = QPushButton("Volver a la pantalla principal")
        boton_volver.clicked.connect(self.volver_a_principal)
        layout_usuario.addWidget(boton_volver)

        self.setLayout(layout_usuario)
        self.parent = parent

    def volver_a_principal(self):
        self.close()
        self.parent.show()

class EntregaPedidoWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle('Entrega de pedidos')
        self.setGeometry(100, 100, 400, 300)

        layout_usuario = QVBoxLayout()
        etiqueta = QLabel("Esta es la ventana para las entregas de los pedidos")
        layout_usuario.addWidget(etiqueta)

        boton_volver = QPushButton("Volver a la pantalla principal")
        boton_volver.clicked.connect(self.volver_a_principal)
        layout_usuario.addWidget(boton_volver)

        self.setLayout(layout_usuario)
        self.parent = parent

    def volver_a_principal(self):
        self.close()
        self.parent.show()
    
class DespachoPedidoWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle('Despacho de pedidos')
        self.setGeometry(100, 100, 400, 300)

        layout_usuario = QVBoxLayout()
        etiqueta = QLabel("Esta es la ventana para los despachos de los pedidos")
        layout_usuario.addWidget(etiqueta)

        boton_volver = QPushButton("Volver a la pantalla principal")
        boton_volver.clicked.connect(self.volver_a_principal)
        layout_usuario.addWidget(boton_volver)

        self.setLayout(layout_usuario)
        self.parent = parent

    def volver_a_principal(self):
        self.close()
        self.parent.show()
    


