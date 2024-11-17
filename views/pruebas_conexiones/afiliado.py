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

#Para crear un afiliados
query = """
INSERT INTO afiliados (id_afiliado, id_rango, id_promotor, nombre, apellido, email, fecha_afiliacion, telefono, activo)
VALUES (:id_afiliado, :id_rango, :id_promotor, :nombre, :apellido, :email, SYSDATE, :telefono, :activo)
"""

# Los valores a insertar (deberías obtenerlos de alguna forma, como por ejemplo un formulario o entrada del usuario)
valores = {
    'id_afiliado': 12,           # Este es solo un ejemplo, el id puede ser generado automáticamente por la base de datos si es secuencial
    'id_rango': 1,
    'id_promotor': 1,
    'nombre': 'Pablo',
    'apellido': 'Alborán',
    'email': 'pablo.alboran@example.com',
    'telefono': '1234567890',
    'activo': 1  # Asumiendo 'S' para activo y 'N' para inactivo
}

# Ejecuta la consulta de inserción con los valores proporcionados
cursor.execute(query, valores)


# Ejecuta una consulta sencilla
query = ("SELECT id_afiliado, id_rango, id_promotor, nombre, apellido, email, fecha_afiliacion, telefono, activo "
         "FROM afiliados")
cursor.execute(query)

# Itera sobre los resultados y muestra cada fila
for row in cursor:
    print("ID Afiliado:", row[0],
          "ID Rango:", row[1],
          "ID Promotor:", row[2],
          "Nombre:", row[3],
          "Apellido:", row[4],
          "Email:", row[5],
          "Fecha de Afiliación:", row[6],
          "Teléfono:", row[7],
          "Activo:", row[8])

# Cierra el cursor y la conexión
cursor.close()
connection.close()
