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

class ingrediente:

    @staticmethod
    def buscarIngredientesProducto(id_producto):
        try:
            sql = """
                SELECT *
                FROM vista_ingredientes_productos
                WHERE id_producto = :1
            """
            valores = (id_producto,)
            cursor.execute(sql, valores)

            # Obtener el resultado de la consulta
            registros = cursor.fetchall()

            if registros:
                print("Registros encontrados:", registros)
                return registros
            else:
                print("No se encontró ingrediente con id_producto=", id_producto)
                return None

        finally:
            # Cerrar recursos
            if cursor:
                cursor.close()
            if connection:
                connection.close()