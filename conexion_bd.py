from tkinter import messagebox

import oracledb

# Configuración de la base de datos (ajusta estos parámetros según tu configuración)
host = "localhost"
port = 1521
sid = "xe"
conectado = False

# Función para autenticarse en la base de datos
def autenticar(user: str, password: str):
    # Configura el DSN
    dsn = f"{host}:{port}/{sid}"

    # se establece una conexión directa
    oracledb.init_oracle_client()
    try:
        # Intenta conectarte a la base de datos
        connection = oracledb.connect(user=user, password=password, dsn=dsn)
        conectado = True
        # Si la conexión es exitosa
        connection.close()
    except oracledb.DatabaseError as e:
        # Si la conexión falla, muestra un mensaje de error
        messagebox.showerror("Error de autenticación", "Nombre de usuario o contraseña incorrectos")