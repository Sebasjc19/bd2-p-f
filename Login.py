import tkinter as tk
from tkinter import ttk, messagebox
from model.afiliados.afiliado import afiliado
from views import inicio_afiliado


class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Inicio de sesión")
        self.geometry("400x400")

        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure("Framed.TFrame", background="#f0f0f0", borderwidth=5, relief="sunken")
        style.configure("Title.TLabel", font=("Arial", 16, "bold"))

        main_frame = ttk.Frame(self, style="Framed.TFrame")
        main_frame.place(relx=0.5, rely=0.5, anchor="center")

        title_label = ttk.Label(main_frame, text="Inicio de Sesión", style="Title.TLabel")
        title_label.grid(row=0, columnspan=2, pady=10)

        self.username_label = ttk.Label(main_frame, text="Usuario:", font=("Arial", 12))
        self.password_label = ttk.Label(main_frame, text="Contraseña:", font=("Arial", 12))
        self.username_entry = ttk.Entry(main_frame, font=("Arial", 12))
        self.password_entry = ttk.Entry(main_frame, show="*", font=("Arial", 12))
        self.login_button = ttk.Button(main_frame, text="Iniciar sesión", command=self.abrir_inicio_afiliado)

        self.username_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.password_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.username_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        self.password_entry.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        self.login_button.grid(row=3, column=1, padx=10, pady=10, sticky="e")



    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

    def abrir_inicio_afiliado(self):
        ventana_inicio = inicio_afiliado.VentanAfiliado(self.root)



if __name__ == "__main__":
   login_window = LoginWindow()
login_window.mainloop()