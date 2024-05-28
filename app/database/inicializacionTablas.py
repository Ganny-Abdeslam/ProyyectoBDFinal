class generacionTablas():
    
    def __init__(self) -> None:
        pass

    #Clientes
    def generarCliente(self, conexion):
        condicion = False
        
        try:
            with conexion.cursor() as cursor:
                sql = "SHOW TABLES LIKE 'cliente'"
                cursor.execute(sql)
                resultado = cursor.fetchone()

            if resultado:
                condicion = True

        finally:
            if not(condicion):
                self.crearTablaCliente(conexion)

    def crearTablaCliente(self, conexion):
        try:
            with conexion.cursor() as cursor:
                sql = """
                CREATE TABLE cliente (
                    id_cliente       INT NOT NULL AUTO_INCREMENT,
                    nombre           VARCHAR(255) NOT NULL,
                    direccion        VARCHAR(255) NOT NULL,
                    telefono         VARCHAR(255) NOT NULL,
                    email            VARCHAR(255) NOT NULL,
                    ciudad_id_ciudad INT NOT NULL,
                    PRIMARY KEY (id_cliente)
                );
                """
                cursor.execute(sql)

            print("Tabla de clientes creada correctamente.")

        finally:
            pass

    #Producto
    def generarProducto(self, conexion):
        condicion = False
        
        try:
            with conexion.cursor() as cursor:
                sql = "SHOW TABLES LIKE 'producto'"
                cursor.execute(sql)
                resultado = cursor.fetchone()

            if resultado:
                condicion = True

        finally:
            if not(condicion):
                self.crearTablaProducto(conexion)

    def crearTablaProducto(self, conexion):
        try:
            with conexion.cursor() as cursor:
                sql = """
                CREATE TABLE producto (
                    id_producto INT NOT NULL AUTO_INCREMENT,
                    nombre      VARCHAR(255) NOT NULL,
                    descripcion VARCHAR(255) NOT NULL,
                    precio      DECIMAL(10, 2) NOT NULL,
                    cantidad    INT,
                    PRIMARY KEY (id_producto)
                );
                """
                cursor.execute(sql)

            print("Tabla de producto fue creada correctamente.")

        finally:
            pass

    #Cotizacion
    def generarCotizacion(self, conexion):
        condicion = False
        
        try:
            with conexion.cursor() as cursor:
                sql = "SHOW TABLES LIKE 'cotizacion'"
                cursor.execute(sql)
                resultado = cursor.fetchone()

            if resultado:
                condicion = True

        finally:
            if not(condicion):
                self.crearTablaCotizacion(conexion)

    def crearTablaCotizacion(self, conexion):
        try:
            with conexion.cursor() as cursor:
                sql = """
                CREATE TABLE cotizacion (
                    id_cotizacion   INT NOT NULL AUTO_INCREMENT,
                    fecha           DATE NOT NULL,
                    total           DECIMAL(10, 2) NOT NULL,
                    vendedor_cedula INT NOT NULL,
                    PRIMARY KEY (id_cotizacion)
                );
                """
                cursor.execute(sql)

            print("Tabla de cotizacion fue creada correctamente.")

        finally:
            pass

    #Detalles Cotizacion
    def generarDTCotizacion(self, conexion):
        condicion = False
        
        try:
            with conexion.cursor() as cursor:
                sql = "SHOW TABLES LIKE 'cotizacion_detalle'"
                cursor.execute(sql)
                resultado = cursor.fetchone()

            if resultado:
                condicion = True

        finally:
            if not(condicion):
                self.crearTablaDTCotizacion(conexion)

    def crearTablaDTCotizacion(self, conexion):
        try:
            with conexion.cursor() as cursor:
                sql = """
                CREATE TABLE cotizacion_detalle (
                    id_cotizacion INT NOT NULL,
                    id_producto   INT NOT NULL,
                    cantidad      INT NOT NULL,
                    PRIMARY KEY (id_cotizacion, id_producto)
                );
                """
                cursor.execute(sql)

            print("Tabla de cotizacion detalle fue creada correctamente.")

        finally:
            pass

    #Pais
    def generarPais(self, conexion):
        condicion = False
        
        try:
            with conexion.cursor() as cursor:
                sql = "SHOW TABLES LIKE 'pais'"
                cursor.execute(sql)
                resultado = cursor.fetchone()

            if resultado:
                condicion = True

        finally:
            if not(condicion):
                self.crearTablaPais(conexion)

    def crearTablaPais(self, conexion):
        try:
            with conexion.cursor() as cursor:
                sql = """
                CREATE TABLE pais (
                    id_pais INT NOT NULL,
                    nombre  VARCHAR(255) NOT NULL,
                    PRIMARY KEY (id_pais)
                );
                """
                cursor.execute(sql)

            print("Tabla de pais fue creada correctamente.")

        finally:
            pass

    #Departamentos
    def generarDepartamentos(self, conexion):
        condicion = False
        
        try:
            with conexion.cursor() as cursor:
                sql = "SHOW TABLES LIKE 'departamento'"
                cursor.execute(sql)
                resultado = cursor.fetchone()

            if resultado:
                condicion = True

        finally:
            if not(condicion):
                self.crearTablaDepartamentos(conexion)

    def crearTablaDepartamentos(self, conexion):
        try:
            with conexion.cursor() as cursor:
                sql = """
                CREATE TABLE departamento (
                    id_departamento INT NOT NULL,
                    nombre VARCHAR(255) NOT NULL,
                    id_pais INT NOT NULL,
                    PRIMARY KEY (id_departamento)
                ) CHARACTER SET utf8mb4;
                """
                cursor.execute(sql)

            print("Tabla de departamento fue creada correctamente.")

        finally:
            pass

    #Ciudad
    def generarCiudad(self, conexion):
        condicion = False
        
        try:
            with conexion.cursor() as cursor:
                sql = "SHOW TABLES LIKE 'ciudad'"
                cursor.execute(sql)
                resultado = cursor.fetchone()

            if resultado:
                condicion = True

        finally:
            if not(condicion):
                self.crearTablaCiudad(conexion)

    def crearTablaCiudad(self, conexion):
        try:
            with conexion.cursor() as cursor:
                sql = """
                CREATE TABLE ciudad (
                    id_ciudad       INT NOT NULL,
                    nombre          VARCHAR(255) NOT NULL,
                    id_departamento INT NOT NULL,
                    PRIMARY KEY (id_ciudad)
                );
                """
                cursor.execute(sql)

            print("Tabla de ciudad fue creada correctamente.")

        finally:
            pass
    
    #Pedido Despachado
    def generarPedidoDesp(self, conexion):
        condicion = False
        
        try:
            with conexion.cursor() as cursor:
                sql = "SHOW TABLES LIKE 'pedido_despachar'"
                cursor.execute(sql)
                resultado = cursor.fetchone()

            if resultado:
                condicion = True

        finally:
            if not(condicion):
                self.crearTablaPedidoDesp(conexion)

    def crearTablaPedidoDesp(self, conexion):
        try:
            with conexion.cursor() as cursor:
                sql = """
                CREATE TABLE pedido_despachar (
                    bodeguero_cedula   INT NOT NULL,
                    factura_id_factura INT NOT NULL,
                    fecha              DATE NOT NULL,
                    estado             VARCHAR(255) NOT NULL,
                    PRIMARY KEY (bodeguero_cedula, factura_id_factura)
                );
                """
                cursor.execute(sql)

            print("Tabla de pedido despachar fue creada correctamente.")

        finally:
            pass

    #Pedidos Entrega
    def generarPedidoEntr(self, conexion):
        condicion = False
        
        try:
            with conexion.cursor() as cursor:
                sql = "SHOW TABLES LIKE 'pedido_entrega'"
                cursor.execute(sql)
                resultado = cursor.fetchone()

            if resultado:
                condicion = True

        finally:
            if not(condicion):
                self.crearTablaPedidoEntr(conexion)

    def crearTablaPedidoEntr(self, conexion):
        try:
            with conexion.cursor() as cursor:
                sql = """
                CREATE TABLE pedido_entrega (
                    bodeguero_cedula    INT NOT NULL,
                    factura_id_factura  INT NOT NULL,
                    fecha               DATE NOT NULL,
                    estado              VARCHAR(255) NOT NULL,
                    distribuidor_cedula INT NOT NULL,
                    PRIMARY KEY (factura_id_factura, bodeguero_cedula)
                );
                """
                cursor.execute(sql)

            print("Tabla de pedido entrega fue creada correctamente.")

        finally:
            pass

    #Distribuidor
    def generarDistribuidor(self, conexion):
        condicion = False
        
        try:
            with conexion.cursor() as cursor:
                sql = "SHOW TABLES LIKE 'distribuidor'"
                cursor.execute(sql)
                resultado = cursor.fetchone()

            if resultado:
                condicion = True

        finally:
            if not(condicion):
                self.crearTablaDistribuidor(conexion)

    def crearTablaDistribuidor(self, conexion):
        try:
            with conexion.cursor() as cursor:
                sql = """
                CREATE TABLE distribuidor (
                    placa_vehiculo VARCHAR(255) NOT NULL,
                    cedula         INT NOT NULL,
                    PRIMARY KEY (cedula)
                );
                """
                cursor.execute(sql)

            print("Tabla de distribuidor fue creada correctamente.")

        finally:
            pass

    #Factura
    def generarFactura(self, conexion):
        condicion = False
        
        try:
            with conexion.cursor() as cursor:
                sql = "SHOW TABLES LIKE 'factura'"
                cursor.execute(sql)
                resultado = cursor.fetchone()

            if resultado:
                condicion = True

        finally:
            if not(condicion):
                self.crearTablaFactura(conexion)

    def crearTablaFactura(self, conexion):
        try:
            with conexion.cursor() as cursor:
                sql = """
                CREATE TABLE factura (
                    id_factura      INT NOT NULL AUTO_INCREMENT,
                    fecha           DATE NOT NULL,
                    total           DECIMAL(10, 2),
                    id_cliente      INT NOT NULL,
                    vendedor_cedula INT NOT NULL,
                    PRIMARY KEY (id_factura)
                );
                """
                cursor.execute(sql)

            print("Tabla de factura fue creada correctamente.")

        finally:
            pass
    
    #FacturaDT
    def generarFacturaDT(self, conexion):
        condicion = False
        
        try:
            with conexion.cursor() as cursor:
                sql = "SHOW TABLES LIKE 'factura_detalle'"
                cursor.execute(sql)
                resultado = cursor.fetchone()

            if resultado:
                condicion = True

        finally:
            if not(condicion):
                self.crearTablaFacturaDT(conexion)

    def crearTablaFacturaDT(self, conexion):
        try:
            with conexion.cursor() as cursor:
                sql = """
                CREATE TABLE factura_detalle (
                    id_factura  INT NOT NULL,
                    id_producto INT NOT NULL,
                    cantidad    INT NOT NULL,
                    precio      DECIMAL(10, 2) NOT NULL,
                    PRIMARY KEY (id_producto, id_factura)
                );
                """
                cursor.execute(sql)

            print("Tabla de factura detalle fue creada correctamente.")

        finally:
            pass

    #MateriaPrima
    def generarMateriaPrima(self, conexion):
        condicion = False
        
        try:
            with conexion.cursor() as cursor:
                sql = "SHOW TABLES LIKE 'materia_prima'"
                cursor.execute(sql)
                resultado = cursor.fetchone()

            if resultado:
                condicion = True

        finally:
            if not(condicion):
                self.crearTablaMateriaPrima(conexion)

    def crearTablaMateriaPrima(self, conexion):
        try:
            with conexion.cursor() as cursor:
                sql = """
                CREATE TABLE materia_prima (
                    id_materia_prima INT NOT NULL AUTO_INCREMENT,
                    nombre           VARCHAR(255) NOT NULL,
                    descripcion      VARCHAR(255) NOT NULL,
                    cantidad         INT,
                    PRIMARY KEY (id_materia_prima)
                );
                """
                cursor.execute(sql)

            print("Tabla de materia prima fue creada correctamente.")

        finally:
            pass

    #Material
    def generarMaterial(self, conexion):
        condicion = False
        
        try:
            with conexion.cursor() as cursor:
                sql = "SHOW TABLES LIKE 'material'"
                cursor.execute(sql)
                resultado = cursor.fetchone()

            if resultado:
                condicion = True

        finally:
            if not(condicion):
                self.crearTablaMaterial(conexion)

    def crearTablaMaterial(self, conexion):
        try:
            with conexion.cursor() as cursor:
                sql = """
                CREATE TABLE material (
                    id_materia_prima INT NOT NULL,
                    id_producto      INT NOT NULL,
                    PRIMARY KEY (id_materia_prima, id_producto)
                );
                """
                cursor.execute(sql)

            print("Tabla de material fue creada correctamente.")

        finally:
            pass

    #ProductoSucursal
    def generarProductoSucursal(self, conexion):
        condicion = False
        
        try:
            with conexion.cursor() as cursor:
                sql = "SHOW TABLES LIKE 'producto_sucursal'"
                cursor.execute(sql)
                resultado = cursor.fetchone()

            if resultado:
                condicion = True

        finally:
            if not(condicion):
                self.crearTablaProductoSucursal(conexion)

    def crearTablaProductoSucursal(self, conexion):
        try:
            with conexion.cursor() as cursor:
                sql = """
                CREATE TABLE producto_sucursal (
                    id_producto INT NOT NULL,
                    id_sucursal INT NOT NULL,
                    PRIMARY KEY (id_producto, id_sucursal)
                );
                """
                cursor.execute(sql)

            print("Tabla de producto sucursal fue creada correctamente.")

        finally:
            pass
    
    #Proveedor
    def generarProveedor(self, conexion):
        condicion = False
        
        try:
            with conexion.cursor() as cursor:
                sql = "SHOW TABLES LIKE 'proveedor'"
                cursor.execute(sql)
                resultado = cursor.fetchone()

            if resultado:
                condicion = True

        finally:
            if not(condicion):
                self.crearTablaProveedor(conexion)

    def crearTablaProveedor(self, conexion):
        try:
            with conexion.cursor() as cursor:
                sql = """
                CREATE TABLE proveedor (
                    id_proveedor INT NOT NULL AUTO_INCREMENT,
                    nombre       VARCHAR(255) NOT NULL,
                    direccion    VARCHAR(255) NOT NULL,
                    email        VARCHAR(255) NOT NULL,
                    telefono     VARCHAR(255) NOT NULL,
                    PRIMARY KEY (id_proveedor)
                );
                """
                cursor.execute(sql)

            print("Tabla de proveedor fue creada correctamente.")

        finally:
            pass
    
    #ProveedorMP
    def generarProveedorMP(self, conexion):
        condicion = False
        
        try:
            with conexion.cursor() as cursor:
                sql = "SHOW TABLES LIKE 'proveedor_materiaprima'"
                cursor.execute(sql)
                resultado = cursor.fetchone()

            if resultado:
                condicion = True

        finally:
            if not(condicion):
                self.crearTablaProveedorMP(conexion)

    def crearTablaProveedorMP(self, conexion):
        try:
            with conexion.cursor() as cursor:
                sql = """
                CREATE TABLE proveedor_materiaprima (
                    id_materia_prima INT NOT NULL,
                    id_proveedor     INT NOT NULL,
                    PRIMARY KEY (id_materia_prima, id_proveedor)
                );
                """
                cursor.execute(sql)

            print("Tabla de proveedor_materiaprima fue creada correctamente.")

        finally:
            pass
    
    #Sucursal
    def generarSucursal(self, conexion):
        condicion = False
        
        try:
            with conexion.cursor() as cursor:
                sql = "SHOW TABLES LIKE 'sucursal'"
                cursor.execute(sql)
                resultado = cursor.fetchone()

            if resultado:
                condicion = True

        finally:
            if not(condicion):
                self.crearTablaSucursal(conexion)

    def crearTablaSucursal(self, conexion):
        try:
            with conexion.cursor() as cursor:
                sql = """
                CREATE TABLE sucursal (
                    id_sucursal  INT NOT NULL,
                    direccion    VARCHAR(255) NOT NULL,
                    telefono     VARCHAR(255) NOT NULL,
                    email        VARCHAR(255) NOT NULL,
                    jefe_cedula  INT NULL,
                    id_ciudad    INT NOT NULL,
                    PRIMARY KEY (id_sucursal)
                );
                """
                cursor.execute(sql)

            print("Tabla de sucursal fue creada correctamente.")

        finally:
            pass
    
    #Usuario
    def generarUsuario(self, conexion):
        condicion = False
        
        try:
            with conexion.cursor() as cursor:
                sql = "SHOW TABLES LIKE 'usuario'"
                cursor.execute(sql)
                resultado = cursor.fetchone()

            if resultado:
                condicion = True

        finally:
            if not(condicion):
                self.crearTablaUsuario(conexion)

    def crearTablaUsuario(self, conexion):
        try:
            with conexion.cursor() as cursor:
                sql = """
                CREATE TABLE usuario (
                    cedula           INT NOT NULL,
                    primer_nombre    VARCHAR(255) NOT NULL,
                    segundo_nombre   VARCHAR(255),
                    primer_apellido  VARCHAR(255) NOT NULL,
                    segundo_apellido VARCHAR(255) NOT NULL,
                    fecha_nacimiento DATE NOT NULL,
                    telefono         VARCHAR(255) NOT NULL,
                    direccion        VARCHAR(255) NOT NULL,
                    email            VARCHAR(255) NOT NULL,
                    salario          DECIMAL(10, 2) NOT NULL,
                    username         VARCHAR(255) NOT NULL,
                    password         VARCHAR(255) NOT NULL,
                    id_sucursal      INT NOT NULL,
                    PRIMARY KEY (cedula)
                );
                """
                cursor.execute(sql)

            print("Tabla de usuario fue creada correctamente.")

        finally:
            pass
    
    #Vendedor
    def generarVendedor(self, conexion):
        condicion = False
        
        try:
            with conexion.cursor() as cursor:
                sql = "SHOW TABLES LIKE 'vendedor'"
                cursor.execute(sql)
                resultado = cursor.fetchone()

            if resultado:
                condicion = True

        finally:
            if not(condicion):
                self.crearTablaVendedor(conexion)

    def crearTablaVendedor(self, conexion):
        try:
            with conexion.cursor() as cursor:
                sql = """
                CREATE TABLE vendedor (
                    comision_venta DECIMAL(10, 2),
                    cedula         INT NOT NULL,
                    PRIMARY KEY (cedula)
                );
                """
                cursor.execute(sql)

            print("Tabla de vendedor fue creada correctamente.")

        finally:
            pass

    #Bodeguero
    def generarBodeguero(self, conexion):
        condicion = False
        
        try:
            with conexion.cursor() as cursor:
                sql = "SHOW TABLES LIKE 'bodeguero'"
                cursor.execute(sql)
                resultado = cursor.fetchone()

            if resultado:
                condicion = True

        finally:
            if not(condicion):
                self.crearTablaBodeguero(conexion)

    def crearTablaBodeguero(self, conexion):
        try:
            with conexion.cursor() as cursor:
                sql = """
                CREATE TABLE bodeguero (
                    cedula      INT NOT NULL,
                    jefe_cedula INT,
                    PRIMARY KEY (cedula)
                );
                """
                cursor.execute(sql)

            print("Tabla de bodeguero fue creada correctamente.")

        finally:
            pass

    #Generacion Foraneas
    def generarForaneas(self, conexion):

        try:
            with conexion.cursor() as cursor:
                sql = """
                SELECT CONSTRAINT_NAME
                FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
                WHERE TABLE_NAME = 'bodeguero'
                AND CONSTRAINT_NAME = 'fk_bodeguero_bodeguero';
                """

                cursor.execute(sql)

                resultado = cursor.fetchone()

                if resultado:
                    return
        finally:
            pass

        try:
            with conexion.cursor() as cursor:
                sql = """
                ALTER TABLE bodeguero
                    ADD CONSTRAINT fk_bodeguero_bodeguero FOREIGN KEY (jefe_cedula)
                        REFERENCES bodeguero (cedula);
                """
                cursor.execute(sql)

                sql = """
                ALTER TABLE ciudad
                    ADD CONSTRAINT fk_ciudad_departamento FOREIGN KEY (id_departamento)
                        REFERENCES departamento (id_departamento);
                """
                cursor.execute(sql)

                sql = """
                ALTER TABLE cliente
                    ADD CONSTRAINT fk_cliente_ciudad FOREIGN KEY (ciudad_id_ciudad)
                        REFERENCES ciudad (id_ciudad);
                """
                cursor.execute(sql)
            
                sql = """
                ALTER TABLE cotizacion_detalle
                    ADD CONSTRAINT fk_cotizacion_detalle_cotizacion FOREIGN KEY (id_cotizacion)
                        REFERENCES cotizacion (id_cotizacion);
                """
                cursor.execute(sql)

                sql = """
                ALTER TABLE cotizacion_detalle
                    ADD CONSTRAINT fk_cotizacion_detalle_producto FOREIGN KEY (id_producto)
                        REFERENCES producto (id_producto);
                """
                cursor.execute(sql)
           
                sql = """
                ALTER TABLE cotizacion
                    ADD CONSTRAINT fk_cotizacion_vendedor FOREIGN KEY (vendedor_cedula)
                        REFERENCES vendedor (cedula);
                """
                cursor.execute(sql)
           
                sql = """
                ALTER TABLE departamento
                    ADD CONSTRAINT fk_departamento_pais FOREIGN KEY (id_pais)
                        REFERENCES pais (id_pais);
                """
                cursor.execute(sql)
           
                sql = """
                ALTER TABLE distribuidor
                    ADD CONSTRAINT fk_distribuidor_usuario FOREIGN KEY (cedula)
                        REFERENCES usuario (cedula);
                """
                cursor.execute(sql)
           
                sql = """
                ALTER TABLE factura
                    ADD CONSTRAINT fk_factura_cliente FOREIGN KEY (id_cliente)
                        REFERENCES cliente (id_cliente);
                """
                cursor.execute(sql)
           
                sql = """
                ALTER TABLE factura_detalle
                    ADD CONSTRAINT fk_factura_detalle_factura FOREIGN KEY (id_factura)
                        REFERENCES factura (id_factura);
                """
                cursor.execute(sql)
           
                sql = """
                ALTER TABLE factura_detalle
                    ADD CONSTRAINT fk_factura_detalle_producto FOREIGN KEY (id_producto)
                        REFERENCES producto (id_producto);
                """
                cursor.execute(sql)
           
                sql = """
                ALTER TABLE factura
                    ADD CONSTRAINT fk_factura_vendedor FOREIGN KEY (vendedor_cedula)
                        REFERENCES vendedor (cedula);
                """
                cursor.execute(sql)
           
                sql = """
                ALTER TABLE material
                    ADD CONSTRAINT fk_material_materia_prima FOREIGN KEY (id_materia_prima)
                        REFERENCES materia_prima (id_materia_prima);
                """
                cursor.execute(sql)
           
                sql = """
                ALTER TABLE material
                    ADD CONSTRAINT fk_material_producto FOREIGN KEY (id_producto)
                        REFERENCES producto (id_producto);
                """
                cursor.execute(sql)
           
                sql = """
                ALTER TABLE pedido_despachar
                    ADD CONSTRAINT fk_pedido_despachar_bodeguero FOREIGN KEY (bodeguero_cedula)
                        REFERENCES bodeguero (cedula);
                """
                cursor.execute(sql)
           
                sql = """
                ALTER TABLE pedido_despachar
                    ADD CONSTRAINT fk_pedido_despachar_factura FOREIGN KEY (factura_id_factura)
                        REFERENCES factura (id_factura);
                """
                cursor.execute(sql)
           
                sql = """
                ALTER TABLE pedido_entrega
                    ADD CONSTRAINT fk_pedido_entrega_distribuidor FOREIGN KEY (distribuidor_cedula)
                        REFERENCES distribuidor (cedula);
                """
                cursor.execute(sql)

                sql = """
                ALTER TABLE pedido_entrega
                    ADD CONSTRAINT fk_pedido_entrega_pedido_despachar FOREIGN KEY (bodeguero_cedula, factura_id_factura)
                        REFERENCES pedido_despachar (bodeguero_cedula, factura_id_factura);
                """
                cursor.execute(sql)
           
                sql = """
                ALTER TABLE producto_sucursal
                    ADD CONSTRAINT fk_producto_sucursal_producto FOREIGN KEY (id_producto)
                        REFERENCES producto (id_producto);
                """
                cursor.execute(sql)
           
                sql = """
                ALTER TABLE producto_sucursal
                    ADD CONSTRAINT fk_producto_sucursal_sucursal FOREIGN KEY (id_sucursal)
                        REFERENCES sucursal (id_sucursal);
                """
                cursor.execute(sql)
           
                sql = """
                ALTER TABLE proveedor_materiaprima
                    ADD CONSTRAINT fk_proveedor_materiaprima_materia_prima FOREIGN KEY (id_materia_prima)
                        REFERENCES materia_prima (id_materia_prima);
                """
                cursor.execute(sql)
           
                sql = """
                ALTER TABLE proveedor_materiaprima
                    ADD CONSTRAINT fk_proveedor_materiaprima_proveedor FOREIGN KEY (id_proveedor)
                        REFERENCES proveedor (id_proveedor);
                """
                cursor.execute(sql)
           
                sql = """
                ALTER TABLE sucursal
                    ADD CONSTRAINT fk_sucursal_ciudad FOREIGN KEY (id_ciudad)
                        REFERENCES ciudad (id_ciudad);
                """
                cursor.execute(sql)
           
                # sql = """
                # ALTER TABLE sucursal
                #     ADD CONSTRAINT fk_sucursal_usuario FOREIGN KEY (jefe_cedula)
                #         REFERENCES usuario (cedula);
                # """
                # cursor.execute(sql)
           
                sql = """
                ALTER TABLE usuario
                    ADD CONSTRAINT fk_usuario_sucursal FOREIGN KEY (id_sucursal)
                        REFERENCES sucursal (id_sucursal);
                """
                cursor.execute(sql)
           
                sql = """
                ALTER TABLE vendedor
                    ADD CONSTRAINT fk_vendedor_usuario FOREIGN KEY (cedula)
                        REFERENCES usuario (cedula);
                """
                cursor.execute(sql)

            print("Se generaron las foraneas.")
        finally:
            pass