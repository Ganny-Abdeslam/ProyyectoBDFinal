from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QGridLayout

import sys

class PrincipalScreen:

    def __init__(self) -> None:
        pass

    def generarPS(self):
        app = QApplication(sys.argv)

        window = QWidget()
        window.setWindowTitle('Ejemplo de ventana con botones')
        window.setGeometry(100, 100, 400, 300)

        layout = QGridLayout()

        botones = ['Usuario', 'Cliente', 'Sucursal', 'Producto', 'Factura', 'Proveedor', 'Material', 'Cotización']
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

        window.setLayout(layout)

        window.show()

        sys.exit(app.exec())