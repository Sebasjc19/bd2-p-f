import oracledb

# Configura los parámetros de conexión
host = "localhost"
port = 1521
sid = "xe"
user = "LANTHA"
password = "eldenring"

# Define el DSN
dsn = f"{host}:{port}/{sid}"

# se establece una conexión directa
oracledb.init_oracle_client()
# Conéctate a la base de datos
connection = oracledb.connect(user=user, password=password, dsn=dsn)

# Crea un cursor para ejecutar la consulta
cursor = connection.cursor()


class direccion:


    @staticmethod
    def buscarDireccion(id_direccion):
        try:

            # Consulta para obtener los datos de la tabla direcciones
            sql = """SELECT id_afiliado, id_ciudad, direccion, descripcion 
            FROM direccion
            WHERE id_direccion = :1"""
            valores = (id_direccion,)
            cursor.execute(sql, valores)

            despacho = cursor.fetchone()

            if despacho:
                print("Registro encontrado", despacho)
                return despacho
            else:
                print("No se encontró un registro con id_afiliado =", id_direccion)
                return None
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()


