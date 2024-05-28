-- Dataset Bade de datos

-- Usuario
INSERT INTO usuario (cedula, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, fecha_nacimiento, telefono, direccion, email, salario, username, password, id_sucursal) VALUES 
('12345678', 'Carlos', 'Andrés', 'Gómez', 'Pérez', CAST('1985-06-15' AS DATE), '111-222-3333', 'Calle 1', 'carlos.gomez@example.com', 2500.00, 'cgomez', 'password123', 5),
('23456789', 'María', 'Elena', 'López', 'Rodríguez', CAST('1990-08-25' AS DATE), '222-333-4444', 'Avenida 2', 'maria.lopez@example.com', 3000.00, 'mlopez', 'password234', 3),
('34567890', 'Juan', 'José', 'Martínez', 'García', CAST('1988-12-05' AS DATE), '333-444-5555', 'Boulevard 3', 'juan.martinez@example.com', 2800.00, 'jmartinez', 'password345', 1),
('45678901', 'Ana', 'Isabel', 'Fernández', 'González', CAST('1992-03-18' AS DATE), '444-555-6666', 'Carretera 4', 'ana.fernandez@example.com', 3200.00, 'afernandez', 'password456', 2),
('56789012', 'Luis', 'Alberto', 'Ramírez', 'Sánchez', CAST('1987-11-22' AS DATE), '555-666-7777', 'Pasaje 5', 'luis.ramirez@example.com', 2700.00, 'lramirez', 'password567', 4);

--Vendedor
INSERT INTO vendedor (comision_venta, cedula) VALUES
(1000.00, '12345678'),
(1500.50, '23456789'),
(800.25, '34567890'),
(1200.75, '45678901'),
(900.30, '56789012');

-- Sucursal
INSERT INTO sucursal (id_sucursal, direccion, telefono, email, jefe_cedula, id_ciudad) VALUES 
(1, 'Calle Comercio 123', '111-222-3333', 'sucursal1@example.com', 0, 4),
(2, 'Avenida Empresa 456', '222-333-4444', 'sucursal2@example.com', 0, 7),
(3, 'Boulevard Negocios 789', '333-444-5555', 'sucursal3@example.com', 0, 2),
(4, 'Carretera Servicios 101', '444-555-6666', 'sucursal4@example.com', 0, 5),
(5, 'Pasaje Industria 202', '555-666-7777', 'sucursal5@example.com', 0, 9);

-- Cliente
INSERT INTO cliente (nombre, direccion, telefono, email, ciudad_id_ciudad) VALUES 
('Juan Pérez', 'Calle Principal 123', '111-222-3333', 'juan.perez@example.com', 3),
('María López', 'Avenida Secundaria 456', '222-333-4444', 'maria.lopez@example.com', 7),
('Carlos García', 'Boulevard Terciario 789', '333-444-5555', 'carlos.garcia@example.com', 5),
('Ana Martínez', 'Carretera Cuarta 101', '444-555-6666', 'ana.martinez@example.com', 9),
('Luis Rodríguez', 'Pasaje Quinto 202', '555-666-7777', 'luis.rodriguez@example.com', 2);

-- Cotizacion
INSERT INTO cotizacion (fecha, total, vendedor_cedula) VALUES 
(NOW(), 239.97, '12345678'),
(NOW(), 259.98, '23456789'), 
(NOW(), 999.99, '12345678'), 
(NOW(), 2799.96, '23456789'), 
(NOW(), 1499.95, '12345678')

INSERT INTO factura (fecha, total, id_cliente, vendedor_cedula) VALUES 
(NOW(), 239.97, 3, '12345678'),
(NOW(), 259.98, 5, '23456789'),
(NOW(), 999.99, 2, '12345678'),
(NOW(), 2799.96, 1, '23456789'),
(NOW(), 1499.95, 4, '12345678')

-- Producto
INSERT INTO producto (nombre, descripcion, precio, cantidad) VALUES 
('Taladro Eléctrico', 'Taladro eléctrico de 500W con múltiples velocidades', 79.99, 50),
('Silla de Oficina', 'Silla ergonómica con soporte lumbar y ajuste de altura', 129.99, 100),
('Laptop Ultrabook', 'Laptop ultrabook con procesador i7 y 16GB de RAM', 999.99, 30),
('Teléfono Inteligente', 'Teléfono inteligente con pantalla AMOLED de 6.5 pulgadas', 699.99, 75),
('Cámara Digital', 'Cámara digital de 20MP con zoom óptico de 10x', 299.99, 40)

-- Materia Prima
INSERT INTO materia_prima (nombre, descripcion, cantidad) VALUES 
('Acero Inoxidable', 'Material utilizado para la fabricación de herramientas y maquinaria', 500),
('Plástico ABS', 'Material plástico utilizado en carcasas y componentes electrónicos', 200),
('Cobre', 'Material conductor utilizado en cables y circuitos eléctricos', 300),
('Madera de Roble', 'Madera de alta calidad utilizada en la fabricación de muebles', 150),
('Aluminio', 'Material ligero utilizado en la fabricación de estructuras y componentes', 400)

-- Proveedor
INSERT INTO proveedor (nombre, direccion, email, telefono) VALUES 
('Metales S.A.', 'Calle Fábrica 123, Ciudad Industrial', 'contacto@metalessa.com', '123-456-7890'),
('Plásticos y Más', 'Avenida Innovación 456, Zona Norte', 'ventas@plasticosymas.com', '234-567-8901'),
('Eléctricos del Sur', 'Boulevard Energía 789, Sector Eléctrico', 'info@electricossur.com', '345-678-9012'),
('Maderas del Norte', 'Carretera Madera 101, Parque Industrial', 'soporte@maderasnorte.com', '456-789-0123'),
('Aluminio Premium', 'Avenida Metalurgia 202, Distrito Central', 'contacto@aluminiopremium.com', '567-890-1234')

-- DetalleFactura
INSERT INTO factura_detalle (id_factura, id_producto, cantidad, precio) VALUES 
(1, 1, 3, 239.97),   
(2, 2, 2, 259.98), 
(3, 3, 1, 999.99), 
(4, 4, 4, 2799.96), 
(5, 5, 5, 1499.95)