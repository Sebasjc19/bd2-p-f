import oracledb

host = "localhost"
port = 1521
sid = "xe"
user = "nexus"
password = "admin1234"


dsn = f"{host}:{port}/{sid}"

oracledb.init_oracle_client()
connection = oracledb.connect(user=user, password=password, dsn=dsn)
cursor = connection.cursor()

class producto:


    @staticmethod
    def buscarProducto(id_producto):
        try:
            sql = """
                SELECT *
                FROM vista_productos
                WHERE id_producto = :1
            """
            valores = (id_producto,)
            cursor.execute(sql, valores)

            # Obtener el resultado de la consulta
            registro = cursor.fetchone()

            if registro:
                print("Registro encontrado:", registro)
                return registro
            else:
                print("No se encontró un registro con id_producto =", id_producto)
                return None

        finally:
            # Cerrar recursos
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    @staticmethod
    def obtenerProductos():
        try:
            sql = """
                    SELECT *
                    FROM vista_productos
                """
            cursor.execute(sql)

            # Obtener el resultado de la consulta
            registro = cursor.fetchall()

            if registro:
                print("Productos encontrados:", registro)
                return registro
            else:
                print("No se encontró productos")
                return None

        finally:
            # Cerrar recursos
            if cursor:
                cursor.close()
            if connection:
                connection.close()

