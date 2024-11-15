import oracledb

# Configura los parámetros de conexión
host = "localhost"
port = 1521
sid = "xe"
user = "nexus"
password = "admin1234"

# Define el DSN
dsn = f"{host}:{port}/{sid}"

# se establece una conexión directa
oracledb.init_oracle_client()
# Conéctate a la base de datos
connection = oracledb.connect(user=user, password=password, dsn=dsn)

# Crea un cursor para ejecutar la consulta
cursor = connection.cursor()

# Ejecuta una consulta sencilla
query = ("SELECT id_producto, id_tipo_producto, id_marca, nombre_producto, descripcion_producto,"
         "tamanio, precio_venta, precio_compra FROM producto")
cursor.execute(query)

# Itera sobre los resultados y muestra cada fila
for row in cursor:
    print("ID Producto:", row[0],
          "ID Tipo Producto:", row[1],
          "ID Marca:", row[2],
          "Nombre Producto:", row[3],
          "Descripción Producto:", row[4],
          "Tamaño:", row[5],
          "Precio Venta:", row[6],
          "Precio Compra:", row[7])

# Cierra el cursor y la conexión
cursor.close()
connection.close()
