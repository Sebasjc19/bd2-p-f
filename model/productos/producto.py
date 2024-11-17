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
    def buscarDespacho(id_despacho):
        try:
            sql = """
                SELECT id_despacho, id_factura_venta, id_direccion, id_transportadora, fecha_salida, hora_salida, guia
                FROM Despacho
                WHERE id_despacho = :1
            """
            valores = (id_despacho,)
            cursor.execute(sql, valores)

            # Obtener el resultado de la consulta
            registro = cursor.fetchone()

            if registro:
                print("Registro encontrado:", registro)
                return registro
            else:
                print("No se encontró un registro con id_despacho =", id_despacho)
                return None

        finally:
            # Cerrar recursos
            if cursor:
                cursor.close()
            if connection:
                connection.close()



