from tkinter import messagebox

import oracledb

host = "localhost"
port = 1521
sid = "xe"



def autenticar(user: str, password: str):
    dsn = f"{host}:{port}/{sid}"
    oracledb.init_oracle_client(lib_dir="C:/Users/migue/Desktop/instantclient_23_6")
    try:
        connection = oracledb.connect(user=user, password=password, dsn=dsn)
        print("Autenticado correctamente.")
        connection.close()
    except oracledb.DatabaseError as e:
        print("Error de autenticación: Nombre de usuario o contraseña incorrectos.")

if __name__ == "__main__":
    user = input("Ingresa el nombre de usuario: ")
    password = input("Ingresa la contraseña: ")
    autenticar(user, password)