import tkinter as tk
from tkinter import ttk


class VentanaVentas:
    def __init__(self, root, sesion):
        self.root = root
        self.sesion = sesion
        self.root.title("Ventas")
        self.root.geometry("600x400")

        # Título de la ventana
        self.label_titulo = tk.Label(self.root, text="Listado de Ventas", font=("Arial", 16))
        self.label_titulo.pack(padx=10, pady=10)

        # Crear Treeview para mostrar las ventas
        self.tree = ttk.Treeview(self.root, columns=("id_venta", "cliente", "fecha", "total"), show="headings")
        self.tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Definir encabezados de la tabla
        self.tree.heading("id_venta", text="ID Venta")
        self.tree.heading("cliente", text="Cliente")
        self.tree.heading("fecha", text="Fecha")
        self.tree.heading("total", text="Total")

        # Configurar ancho de columnas
        self.tree.column("id_venta", width=100)
        self.tree.column("cliente", width=200)
        self.tree.column("fecha", width=150)
        self.tree.column("total", width=100, anchor="e")  # Alinear a la derecha

        # Botón para actualizar la lista de ventas
        self.boton_actualizar = tk.Button(self.root, text="Actualizar Ventas", command=self.cargar_ventas)
        self.boton_actualizar.pack(padx=10, pady=10)

    def cargar_ventas(self):
        print("Cargando Ventas")
