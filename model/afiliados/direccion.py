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

class direccion:

    # Para crear una dirección
    @staticmethod
    def crearDireccion(id_afiliado, id_ciudad, direccion, descripcion):
        try:
            sql = """
            INSERT INTO direcciones (id_afiliado, id_ciudad, direccion, descriptivo)
            VALUES (:id_afiliado, :id_ciudad, :direccion, :descriptivo)
            """

            valores = {
            'id_afiliado': id_afiliado,
            'id_ciudad': id_ciudad,
            'direccion': direccion,
            'descripcion': descripcion
            }

            # Ejecuta la consulta de inserción con los valores proporcionados
            cursor.execute(sql, valores)
            connection.commit()
            print(cursor.rowcount, "registro(s) ingresado(s) con éxito")
        finally:
            # Cerrar recursos
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    @staticmethod
    def eliminarDireccion(id_afiliado):
        try:
            query = "DELETE FROM afiliados WHERE id_afiliado = :id_afiliado"
        valores = {
            'id_afiliado': id_afiliado
        }

        # Ejecuta la consulta de eliminación con los valores proporcionados
        cursor.execute(query, valores)

        # Realiza el commit para guardar los cambios
        connection.commit()


    def mostrarDirecciones():
        # Consulta para obtener los datos de la tabla direcciones
        query = "SELECT id_afiliado, id_ciudad, direccion, descripcion FROM direccion"
        cursor.execute(query)

        # Itera sobre los resultados y muestra cada fila
        for row in cursor:
            print("ID Afiliado:", row[0],
                  "ID Ciudad:", row[1],
                  "Dirección:", row[2],
                  "Descriptivo:", row[3])


    def actualizarDireccion(id_afiliado, email_nuevo, telefono_nuevo):
        query = """
        UPDATE afiliados
        SET email = :email_nuevo, telefono = :telefono_nuevo
        WHERE id_afiliado = :id_afiliado
        """

        valores = {
            'id_afiliado': id_afiliado,
            'email_nuevo': email_nuevo,
            'telefono_nuevo': telefono_nuevo
        }

        # Ejecuta la consulta de actualización con los valores proporcionados
        cursor.execute(query, valores)

        # Realiza el commit para guardar los cambios
        connection.commit()


    # Llamada a la función para insertar un nuevo afiliados
    # crearAfiliado(1, 1, 'Pablo', 'Alborán', 'dasdfgasdfsa@example.com', '1234567890', 1)
    # eliminarAfiliado(64)

    # actualizarAfiliado(1, "juanpereza@gmail.com", 3199494949)

mostrarDirecciones()

# Cierra el cursor y la conexión
cursor.close()
connection.close()
