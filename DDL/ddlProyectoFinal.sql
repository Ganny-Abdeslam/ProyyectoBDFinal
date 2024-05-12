-- Generado por Oracle SQL Developer Data Modeler 23.1.0.087.0806
--   en:        2024-05-07 23:24:09 COT
--   sitio:      Oracle Database 11g
--   tipo:      Oracle Database 11g



-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

--BODEGUERO YA
CREATE TABLE bodeguero (
    cedula      NUMBER NOT NULL,
    jefe_cedula NUMBER
);

ALTER TABLE bodeguero ADD CONSTRAINT bodeguero_pk PRIMARY KEY ( cedula );

--CIUDAD YA
CREATE TABLE ciudad (
    id_ciudad       NUMBER NOT NULL,
    nombre          VARCHAR2(255 BYTE) NOT NULL,
    id_departamento NUMBER NOT NULL
);

ALTER TABLE ciudad ADD CONSTRAINT ciudad_pk PRIMARY KEY ( id_ciudad );

--CLIENTES YA
CREATE TABLE cliente (
    id_cliente       NUMBER NOT NULL,
    nombre           VARCHAR2(255 BYTE) NOT NULL,
    direccion        VARCHAR2(255 BYTE) NOT NULL,
    telefono         VARCHAR2(255 BYTE) NOT NULL,
    email            VARCHAR2(255 BYTE) NOT NULL,
    ciudad_id_ciudad NUMBER NOT NULL
);

ALTER TABLE cliente ADD CONSTRAINT cliente_pk PRIMARY KEY ( id_cliente );

--COTIZACION YA
CREATE TABLE cotizacion (
    id_cotizacion   NUMBER NOT NULL,
    fecha           DATE NOT NULL,
    total           NUMBER NOT NULL,
    vendedor_cedula NUMBER NOT NULL
);

ALTER TABLE cotizacion ADD CONSTRAINT cotizacion_pk PRIMARY KEY ( id_cotizacion );

--COTIZACIONDT YA
CREATE TABLE cotizacion_detalle (
    id_cotizacion NUMBER NOT NULL,
    id_producto   NUMBER NOT NULL,
    cantidad      NUMBER NOT NULL
);

ALTER TABLE cotizacion_detalle ADD CONSTRAINT cotizacion_detalle_pk PRIMARY KEY ( id_cotizacion,
                                                                                  id_producto );

--DEPARTAMENTO YA
CREATE TABLE departamento (
    id_departamento NUMBER NOT NULL,
    nombre          VARCHAR2(255 BYTE) NOT NULL,
    id_pais         NUMBER NOT NULL
);

ALTER TABLE departamento ADD CONSTRAINT departamento_pk PRIMARY KEY ( id_departamento );

--DISTRIBUIDOR YA
CREATE TABLE distribuidor (
    placa_vehiculo VARCHAR2(255 BYTE) NOT NULL,
    cedula         NUMBER NOT NULL
);

ALTER TABLE distribuidor ADD CONSTRAINT distribuidor_pk PRIMARY KEY ( cedula );

--FACTURA YA
CREATE TABLE factura (
    id_factura      NUMBER NOT NULL,
    fecha           DATE NOT NULL,
    total           NUMBER,
    id_cliente      NUMBER NOT NULL,
    vendedor_cedula NUMBER NOT NULL
);

ALTER TABLE factura ADD CONSTRAINT factura_pk PRIMARY KEY ( id_factura );

--FACTUDT YA
CREATE TABLE factura_detalle (
    id_factura  NUMBER NOT NULL,
    id_producto NUMBER NOT NULL,
    cantidad    NUMBER NOT NULL,
    precio      NUMBER NOT NULL
);

ALTER TABLE factura_detalle ADD CONSTRAINT factura_detalle_pk PRIMARY KEY ( id_producto,
                                                                            id_factura );

--MATERIAPRIMA YA
CREATE TABLE materia_prima (
    id_materia_prima NUMBER NOT NULL,
    nombre           VARCHAR2(255 BYTE) NOT NULL,
    descripcion      VARCHAR2(255 BYTE) NOT NULL,
    cantidad         NUMBER
);

ALTER TABLE materia_prima ADD CONSTRAINT materia_prima_pk PRIMARY KEY ( id_materia_prima );

--MATERIAL YA
CREATE TABLE material (
    id_materia_prima NUMBER NOT NULL,
    id_producto      NUMBER NOT NULL
);

ALTER TABLE material ADD CONSTRAINT material_pk PRIMARY KEY ( id_materia_prima,
                                                              id_producto );

--PAIS YA
CREATE TABLE pais (
    id_pais NUMBER NOT NULL,
    nombre  VARCHAR2(255 BYTE) NOT NULL
);

ALTER TABLE pais ADD CONSTRAINT pais_pk PRIMARY KEY ( id_pais );

--pedido_despachar ya
CREATE TABLE pedido_despachar (
    bodeguero_cedula   NUMBER NOT NULL,
    factura_id_factura NUMBER NOT NULL,
    fecha              DATE NOT NULL,
    estado             VARCHAR2(255 BYTE) NOT NULL
);

ALTER TABLE pedido_despachar ADD CONSTRAINT pedido_despachar_pk PRIMARY KEY ( bodeguero_cedula,
                                                                              factura_id_factura );

--pedido_entrega ya
CREATE TABLE pedido_entrega (
    bodeguero_cedula    NUMBER NOT NULL,
    factura_id_factura  NUMBER NOT NULL,
    fecha               DATE NOT NULL,
    estado              VARCHAR2(255 BYTE) NOT NULL,
    distribuidor_cedula NUMBER NOT NULL
);

ALTER TABLE pedido_entrega ADD CONSTRAINT pedido_entrega_pk PRIMARY KEY ( factura_id_factura,
                                                                          bodeguero_cedula );

--PRODUCTO YA
CREATE TABLE producto (
    id_producto NUMBER NOT NULL,
    nombre      VARCHAR2(255 BYTE) NOT NULL,
    descripcion VARCHAR2(255 BYTE) NOT NULL,
    precio      NUMBER NOT NULL,
    cantidad    NUMBER
);

ALTER TABLE producto ADD CONSTRAINT producto_pk PRIMARY KEY ( id_producto );

--producto_sucursal ya
CREATE TABLE producto_sucursal (
    id_producto NUMBER NOT NULL,
    id_sucursal NUMBER NOT NULL
);

ALTER TABLE producto_sucursal ADD CONSTRAINT producto_sucursal_pk PRIMARY KEY ( id_producto,
                                                                                id_sucursal );

--PROVEEDOR YA
CREATE TABLE proveedor (
    id_proveedor NUMBER NOT NULL,
    nombre       VARCHAR2(255 BYTE) NOT NULL,
    direccion    VARCHAR2(255 BYTE) NOT NULL,
    email        VARCHAR2(255 BYTE) NOT NULL,
    telefono     VARCHAR2(255 BYTE) NOT NULL
);

ALTER TABLE proveedor ADD CONSTRAINT proveedor_pk PRIMARY KEY ( id_proveedor );

--proveedor_materiaprima ya
CREATE TABLE proveedor_materiaprima (
    id_materia_prima NUMBER NOT NULL,
    id_proveedor     NUMBER NOT NULL
);

ALTER TABLE proveedor_materiaprima ADD CONSTRAINT proveedor_materiaprima_pk PRIMARY KEY ( id_materia_prima,
                                                                                          id_proveedor );

--SUCURSAL YA
CREATE TABLE sucursal (
    id_sucursal NUMBER NOT NULL,
    direccion   VARCHAR2(255 BYTE) NOT NULL,
    telefono    VARCHAR2(255 BYTE) NOT NULL,
    email       VARCHAR2(255 BYTE) NOT NULL,
    jefe_cedula NUMBER NOT NULL,
    id_ciudad   NUMBER NOT NULL
);

ALTER TABLE sucursal ADD CONSTRAINT sucursal_pk PRIMARY KEY ( id_sucursal );

--USUARIO YA
CREATE TABLE usuario (
    cedula           NUMBER NOT NULL,
    primer_nombre    VARCHAR2(255 BYTE) NOT NULL,
    segundo_nombre   VARCHAR2(255 BYTE),
    primer_apellido  VARCHAR2(255 BYTE) NOT NULL,
    segundo_apellido VARCHAR2(255 BYTE) NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    telefono         VARCHAR2(255 BYTE) NOT NULL,
    direccion        VARCHAR2(255 BYTE) NOT NULL,
    email            VARCHAR2(255 BYTE) NOT NULL,
    salario          NUMBER NOT NULL,
    username         VARCHAR2(255 BYTE) NOT NULL,
    password         VARCHAR2(255 BYTE) NOT NULL,
    id_sucursal      NUMBER NOT NULL
);

ALTER TABLE usuario ADD CONSTRAINT usuario_pk PRIMARY KEY ( cedula );

--VENDEDOR YA
CREATE TABLE vendedor (
    comision_venta NUMBER,
    cedula         NUMBER NOT NULL
);

ALTER TABLE vendedor ADD CONSTRAINT vendedor_pk PRIMARY KEY ( cedula );

ALTER TABLE bodeguero
    ADD CONSTRAINT bodeguero_bodeguero_fk FOREIGN KEY ( jefe_cedula )
        REFERENCES bodeguero ( cedula );

ALTER TABLE bodeguero
    ADD CONSTRAINT bodeguero_usuario_fk FOREIGN KEY ( cedula )
        REFERENCES usuario ( cedula );

ALTER TABLE ciudad
    ADD CONSTRAINT ciudad_departamento_fk FOREIGN KEY ( id_departamento )
        REFERENCES departamento ( id_departamento );

ALTER TABLE cliente
    ADD CONSTRAINT cliente_ciudad_fk FOREIGN KEY ( ciudad_id_ciudad )
        REFERENCES ciudad ( id_ciudad );

--  ERROR: FK name length exceeds maximum allowed length(30) 
ALTER TABLE cotizacion_detalle
    ADD CONSTRAINT cotizacion_detalle_cotizacion_fk FOREIGN KEY ( id_cotizacion )
        REFERENCES cotizacion ( id_cotizacion );

ALTER TABLE cotizacion_detalle
    ADD CONSTRAINT cotizacion_detalle_producto_fk FOREIGN KEY ( id_producto )
        REFERENCES producto ( id_producto );

ALTER TABLE cotizacion
    ADD CONSTRAINT cotizacion_vendedor_fk FOREIGN KEY ( vendedor_cedula )
        REFERENCES vendedor ( cedula );

ALTER TABLE departamento
    ADD CONSTRAINT departamento_pais_fk FOREIGN KEY ( id_pais )
        REFERENCES pais ( id_pais );

ALTER TABLE distribuidor
    ADD CONSTRAINT distribuidor_usuario_fk FOREIGN KEY ( cedula )
        REFERENCES usuario ( cedula );

ALTER TABLE factura
    ADD CONSTRAINT factura_cliente_fk FOREIGN KEY ( id_cliente )
        REFERENCES cliente ( id_cliente );

ALTER TABLE factura_detalle
    ADD CONSTRAINT factura_detalle_factura_fk FOREIGN KEY ( id_factura )
        REFERENCES factura ( id_factura );

ALTER TABLE factura_detalle
    ADD CONSTRAINT factura_detalle_producto_fk FOREIGN KEY ( id_producto )
        REFERENCES producto ( id_producto );

ALTER TABLE factura
    ADD CONSTRAINT factura_vendedor_fk FOREIGN KEY ( vendedor_cedula )
        REFERENCES vendedor ( cedula );

ALTER TABLE material
    ADD CONSTRAINT material_materia_prima_fk FOREIGN KEY ( id_materia_prima )
        REFERENCES materia_prima ( id_materia_prima );

ALTER TABLE material
    ADD CONSTRAINT material_producto_fk FOREIGN KEY ( id_producto )
        REFERENCES producto ( id_producto );

ALTER TABLE pedido_despachar
    ADD CONSTRAINT pedido_despachar_bodeguero_fk FOREIGN KEY ( bodeguero_cedula )
        REFERENCES bodeguero ( cedula );

ALTER TABLE pedido_despachar
    ADD CONSTRAINT pedido_despachar_factura_fk FOREIGN KEY ( factura_id_factura )
        REFERENCES factura ( id_factura );

ALTER TABLE pedido_entrega
    ADD CONSTRAINT pedido_entrega_distribuidor_fk FOREIGN KEY ( distribuidor_cedula )
        REFERENCES distribuidor ( cedula );

--  ERROR: FK name length exceeds maximum allowed length(30) 
ALTER TABLE pedido_entrega
    ADD CONSTRAINT pedido_entrega_pedido_despachar_fk FOREIGN KEY ( bodeguero_cedula,
                                                                    factura_id_factura )
        REFERENCES pedido_despachar ( bodeguero_cedula,
                                      factura_id_factura );

ALTER TABLE producto_sucursal
    ADD CONSTRAINT producto_sucursal_producto_fk FOREIGN KEY ( id_producto )
        REFERENCES producto ( id_producto );

ALTER TABLE producto_sucursal
    ADD CONSTRAINT producto_sucursal_sucursal_fk FOREIGN KEY ( id_sucursal )
        REFERENCES sucursal ( id_sucursal );

--  ERROR: FK name length exceeds maximum allowed length(30) 
ALTER TABLE proveedor_materiaprima
    ADD CONSTRAINT proveedor_materiaprima_materia_prima_fk FOREIGN KEY ( id_materia_prima )
        REFERENCES materia_prima ( id_materia_prima );

--  ERROR: FK name length exceeds maximum allowed length(30) 
ALTER TABLE proveedor_materiaprima
    ADD CONSTRAINT proveedor_materiaprima_proveedor_fk FOREIGN KEY ( id_proveedor )
        REFERENCES proveedor ( id_proveedor );

ALTER TABLE sucursal
    ADD CONSTRAINT sucursal_ciudad_fk FOREIGN KEY ( id_ciudad )
        REFERENCES ciudad ( id_ciudad );

ALTER TABLE sucursal
    ADD CONSTRAINT sucursal_usuario_fk FOREIGN KEY ( jefe_cedula )
        REFERENCES usuario ( cedula );

ALTER TABLE usuario
    ADD CONSTRAINT usuario_sucursal_fk FOREIGN KEY ( id_sucursal )
        REFERENCES sucursal ( id_sucursal );

ALTER TABLE vendedor
    ADD CONSTRAINT vendedor_usuario_fk FOREIGN KEY ( cedula )
        REFERENCES usuario ( cedula );



-- Informe de Resumen de Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                            21
-- CREATE INDEX                             0
-- ALTER TABLE                             48
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   4
-- WARNINGS                                 0
