import oracledb

host = "localhost"
port = 1521
sid = "xe"
user = "LANTHA"
password = "eldenring"


dsn = f"{host}:{port}/{sid}"

oracledb.init_oracle_client()
connection = oracledb.connect(user=user, password=password, dsn=dsn)
cursor = connection.cursor()

class despacho:

    @staticmethod
    def insertarfactura_venta(id_factura_venta, id_estadoventa, id_afiliado, fecha):
        try:
            sql = """
                INSERT INTO Factura_Venta (id_factura_venta, id_estadoventa, id_afiliado, fecha)
                VALUES (:1, :2, :3, :4)
            """
            valores = (id_factura_venta, id_estadoventa, id_afiliado, fecha)
            cursor.execute(sql, valores)

            # Confirmar los cambios
            connection.commit()
            print(cursor.rowcount, "registro(s) ingresado(s) con éxito")

        finally:
            # Cerrar recursos
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    @staticmethod
    def borrarDespacho(id_despacho):
        try:
            sql = "DELETE FROM Despacho WHERE id_despacho = :1"
            valores = (id_despacho,)
            cursor.execute(sql, valores)

            # Confirmar los cambios
            connection.commit()
            print(cursor.rowcount, "registro(s) eliminado(s) con éxito")

        finally:
            # Cerrar recursos
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    @staticmethod
    def actualizarDespacho(id_despacho, id_factura_venta, id_direccion, id_transportadora, fecha_salida, hora_salida,
                           guia):
        try:
            sql = """
                UPDATE Despacho
                SET id_factura_venta = :2,
                    id_direccion = :3,
                    id_transportadora = :4,
                    fecha_salida = :5,
                    hora_salida = :6,
                    guia = :7
                WHERE id_despacho = :1
            """
            valores = (id_despacho, id_factura_venta, id_direccion, id_transportadora, fecha_salida, hora_salida, guia)
            cursor.execute(sql, valores)

            # Confirmar los cambios
            connection.commit()
            print(cursor.rowcount, "registro(s) actualizado(s) con éxito")

        finally:
            # Cerrar recursos
            if cursor:
                cursor.close()
            if connection:
                connection.close()

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



