import tkinter as tk
from tkinter import ttk
from model.afiliados.afiliado import afiliado

# Clase para la ventana de registro de afiliados
class VentanaRegistroAfiliado:
    def __init__(self, root, sesion):
        self.root = root
        self.root.title("Registrar Afiliado")
        self.root.geometry("400x300")
        self.sesion = sesion

        # Etiquetas y campos para ingresar los datos del nuevo afiliado
        self.label_nombre = tk.Label(self.root, text="Nombre:")
        self.label_nombre.pack(padx=10, pady=5)

        self.entry_nombre = tk.Entry(self.root)
        self.entry_nombre.pack(padx=10, pady=5)

        self.label_apellido = tk.Label(self.root, text="Apellido:")
        self.label_apellido.pack(padx=10, pady=5)

        self.entry_apellido = tk.Entry(self.root)
        self.entry_apellido.pack(padx=10, pady=5)

        self.label_email = tk.Label(self.root, text="Email:")
        self.label_email.pack(padx=10, pady=5)

        self.entry_email = tk.Entry(self.root)
        self.entry_email.pack(padx=10, pady=5)

        self.label_telefono = tk.Label(self.root, text="Teléfono:")
        self.label_telefono.pack(padx=10, pady=5)

        self.entry_telefono = tk.Entry(self.root)
        self.entry_telefono.pack(padx=10, pady=5)

        # Botón para registrar el afiliado
        self.boton_guardar = tk.Button(self.root, text="Registrar", command=self.registrar_afiliado)
        self.boton_guardar.pack(padx=10, pady=20)

    def registrar_afiliado(self):
        # Obtener los datos de los campos
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        email = self.entry_email.get()
        telefono = self.entry_telefono.get()

        # Aquí puedes agregar el código para guardar el afiliado en la base de datos
        # Por ejemplo: afiliado.registrarAfiliado(nombre, apellido, email, telefono)
        afiliado.crearAfiliado(self.sesion.id_afiliado, nombre, apellido, email, telefono)

        print(f"Registrando afiliado: {nombre} {apellido}, Email: {email}, Teléfono: {telefono}")
        # Aquí podrías mostrar un mensaje de éxito o realizar alguna acción adicional.
        self.root.destroy()  # Cierra la ventana de registro
