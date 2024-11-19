import oracledb
import tkinter as tk
from tkinter import messagebox

from proyecto_final_nexus.model.Afiliado import afiliado


class RegistroAfiliado:
    def __init__(self, parent, id_afiliado):
        self.parent = parent
        self.id_afiliado = id_afiliado

        # Ventana de registro
        self.ventana_registro = tk.Toplevel(self.parent)
        self.ventana_registro.title("Registro de Afiliado")

        # Marco para los widgets
        frame_registro = tk.Frame(self.ventana_registro)
        frame_registro.pack(padx=20, pady=20, fill="both", expand=True)

        # Título de la ventana
        self.titulo = tk.Label(frame_registro, text="Formulario de Registro", font=("Helvetica", 14))
        self.titulo.pack(pady=10)

        # Campos de entrada
        self.nombre_label = tk.Label(frame_registro, text="Nombre Completo:")
        self.nombre_label.pack(pady=5)
        self.nombre_entry = tk.Entry(frame_registro, width=30)
        self.nombre_entry.pack(pady=5)

        self.apellido_label = tk.Label(frame_registro, text="Apellido:")
        self.apellido_label.pack(pady=5)
        self.apellido_entry = tk.Entry(frame_registro, width=30)
        self.apellido_entry.pack(pady=5)

        self.email_label = tk.Label(frame_registro, text="Correo Electrónico:")
        self.email_label.pack(pady=5)
        self.email_entry = tk.Entry(frame_registro, width=30)
        self.email_entry.pack(pady=5)

        self.telefono_label = tk.Label(frame_registro, text="Teléfono:")
        self.telefono_label.pack(pady=5)
        self.telefono_entry = tk.Entry(frame_registro, width=30)
        self.telefono_entry.pack(pady=5)

        self.registrar_button = tk.Button(frame_registro, text="Registrar", command=self.registrar_afiliado)
        self.registrar_button.pack(pady=20)

    def registrar_afiliado(self):
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()
        email = self.email_entry.get()
        telefono = self.telefono_entry.get()

        try:
            afiliado.afiliado.crearAfiliado(nombre, apellido, email, telefono, self.id_afiliado)
            messagebox.showinfo("Éxito", "Afiliado registrado correctamente")
            self.ventana_registro.destroy()  # Cerrar ventana de registro
        except Exception as e:
            messagebox.showerror("Error", f"Error al registrar afiliado: {e}")
