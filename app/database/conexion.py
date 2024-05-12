import pymysql

class conexionBD():
    def __init__(self) -> None:
        pass

    def conectar(self):
        host = '127.0.0.1'
        usuario = 'admin'
        contraseña = 'pass'
        base_de_datos = 'proyecto'
        puerto = 9999

        conexion = pymysql.connect(
            host=host,
            user=usuario,
            password=contraseña,
            database=base_de_datos,
            port=puerto
        )

        return conexion