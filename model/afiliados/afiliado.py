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


class afiliado:

    @staticmethod
    def crearAfiliado(id_rango, id_promotor, nombre, apellido, email, telefono, activo):
        try:
            query = """
            INSERT INTO afiliado (id_rango, id_promotor, nombre, apellido, email, fecha_afiliacion, telefono, activo)
            VALUES (:id_rango, :id_promotor, :nombre, :apellido, :email, SYSDATE, :telefono, :activo)
            """

            valores = {
                'id_rango': id_rango,
                'id_promotor': id_promotor,
                'nombre': nombre,
                'apellido': apellido,
                'email': email,
                'telefono': telefono,
                'activo': activo
            }

            # Ejecuta la consulta de inserción con los valores proporcionados
            cursor.execute(query, valores)

            # Realiza el commit para guardar los cambios
            connection.commit()

        finally:
            # Cerrar recursos
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    @staticmethod
    def mostrarAfiliados():
        try:
            # Consulta para obtener los datos de la tabla
            query = "SELECT id_afiliado, id_rango, id_promotor, nombre, apellido, email, fecha_afiliacion, telefono, activo FROM afiliado"
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
        finally:
            # Cerrar recursos
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    @staticmethod
    def actualizarAfiliado(id_afiliado, email_nuevo, telefono_nuevo):
        try:
            query = """
            UPDATE afiliado
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
        finally:
            # Cerrar recursos
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    @staticmethod
    def eliminarAfiliado(id_afiliado):
        try:
            query = "DELETE FROM afiliado WHERE id_afiliado = :id_afiliado"

            valores = {
                'id_afiliado': id_afiliado
            }

            # Ejecuta la consulta de eliminación con los valores proporcionados
            cursor.execute(query, valores)

            # Realiza el commit para guardar los cambios
            connection.commit()
        finally:
            # Cerrar recursos
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    @staticmethod
    def buscarAfiliado(id_afiliado):
        try:
            sql = """
                SELECT id_afiliado, id_rango, id_promotor, nombre, apellido, email, fecha_afiliacion, telefono, activo
                FROM afiliado
                WHERE id_afiliado = :1
            """
            valores = (id_afiliado,)
            cursor.execute(sql, valores)

            # Obtener el resultado de la consulta
            registro = cursor.fetchone()

            if registro:
                print("Afiliado encontrado:", registro)
                return registro
            else:
                print(f"No se encontró un afiliado con id_afiliado = {id_afiliado}")
                return None

        except Exception as e:
            print(f"Error al buscar el afiliado: {e}")
            return None

        finally:
            # Cerrar recursos
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    # mostrarAfiliados()
    buscarAfiliado(4)

