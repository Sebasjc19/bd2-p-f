import tkinter as tk
from tkinter import ttk, messagebox
from model.afiliados.afiliado import afiliado
from views import inicio_afiliado



class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Inicio de sesión")
        self.geometry("600x600")
        self.create_widgets()

    def create_widgets(self):
        # Estilo
        style = ttk.Style()
        style.configure("Framed.TFrame", background="#f0f0f0", borderwidth=5, relief="sunken")
        style.configure("Title.TLabel", font=("Arial", 16, "bold"))

        # Marco principal
        main_frame = ttk.Frame(self, style="Framed.TFrame")
        main_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Título
        title_label = ttk.Label(main_frame, text="Inicio de Sesión", style="Title.TLabel")
        title_label.grid(row=0, columnspan=2, pady=10)

        self.username_label = ttk.Label(main_frame, text="Usuario:", font=("Arial", 12))
        self.password_label = ttk.Label(main_frame, text="Contraseña:", font=("Arial", 12))
        self.username_entry = ttk.Entry(main_frame, font=("Arial", 12))
        self.password_entry = ttk.Entry(main_frame, show="*", font=("Arial", 12))
        self.login_button = ttk.Button(main_frame, text="Iniciar sesión", command=self.autenticar)


        self.username_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.password_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.username_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        self.password_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        self.login_button.grid(row=3, column=1, padx=10, pady=10, sticky="e")

    def autenticar(self):
        # Obtener usuario y contraseña desde las entradas
        user = self.username_entry.get()
        password = self.password_entry.get()

        # Verificar que los campos no estén vacíos
        if not user or not password:
            messagebox.showinfo("Alerta", "Por favor, ingrese el nombre de usuario y la contraseña")
            return

        # Configuración del DSN
        dsn = f"{host}:{port}/{sid}"
        oracledb.init_oracle_client(lib_dir="C:/Users/migue/Desktop/instantclient_23_6")

        try:
            # Intentar la conexión a la base de datos
            connection = oracledb.connect(user=user, password=password, dsn=dsn)
            messagebox.showinfo("Autenticación exitosa", "Conexión exitosa a la base de datos")


            id_afiliado = re.sub("Password_", "", password)

            afiliadoEncontrar = afiliado.afiliado.buscarAfiliado(id_afiliado)
            nombre_rango= afiliado.afiliado.obtener_nombre_rango(afiliadoEncontrar[1])
            if not afiliadoEncontrar:
                raise ValueError("Afiliado no encontrado")

            sesion = Sesion(
                id_afiliado=afiliadoEncontrar[0],
                id_rango=nombre_rango,
                id_promotor=afiliadoEncontrar[2],
                nombre=afiliadoEncontrar[3],
                apellido=afiliadoEncontrar[4],
                email=afiliadoEncontrar[5],
                fecha_afiliacion=afiliadoEncontrar[6],
                telefono=afiliadoEncontrar[7],
                activo=afiliadoEncontrar[8],
            )

            self.destroy()
            VentanaPrincipal(sesion)

        except oracledb.DatabaseError as db_error:
            messagebox.showerror("Error de autenticación", f"Error en la base de datos: {db_error}")

        except ValueError as ve:
            messagebox.showerror("Error de autenticación", str(ve))



if __name__ == "__main__":
   login_window = LoginWindow()
   login_window.mainloop()
