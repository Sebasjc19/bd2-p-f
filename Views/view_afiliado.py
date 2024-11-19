import tkinter as tk
from tkinter import ttk
from proyecto_final_nexus.Views.view_ventas import VentanaVentas
from proyecto_final_nexus.Views.view_despachos import VentanaDespachos
from proyecto_final_nexus.Views.view_productos import VentanaProductos
from proyecto_final_nexus.model.Afiliado.afiliado import Sesion


# Clase para la ventana principal

class VentanaPrincipal(tk.Tk):
    def __init__(self, sesion: Sesion):
        super().__init__()
        self.title("Gestión de Afiliados")
        self.geometry("900x500")  # Tamaño de la ventana
        self.configure(bg="#f0f0f0")  # Fondo de la ventana

        # Guardamos el objeto sesion
        self.sesion = sesion

        self.create_widgets()

    def create_widgets(self):
        # Título principal
        title_label = ttk.Label(self, text="Gestión de Afiliados", font=("Arial", 16, "bold"), background="#f0f0f0")
        title_label.pack(pady=(20, 10))  # Espaciado arriba y abajo

        # Información del Afiliado
        info_frame = ttk.Frame(self, padding=10)
        info_frame.pack(fill="x", padx=20)

        # Acceder a los datos del afiliado desde el objeto 'sesion'
        self.nombre_label = ttk.Label(info_frame, text=f"Nombre: {self.sesion.nombre}", font=("Arial", 12), background="#f0f0f0")
        self.email_label = ttk.Label(info_frame, text=f"Email: {self.sesion.email}", font=("Arial", 12), background="#f0f0f0")
        self.rango_label = ttk.Label(info_frame, text=f"Rango: {self.sesion.id_rango}", font=("Arial", 12), background="#f0f0f0")

        self.nombre_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.email_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.rango_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        # Botones de acción
        buttons_frame = ttk.Frame(self, padding=10)
        buttons_frame.pack(fill="x", padx=20, pady=10)

        ttk.Button(buttons_frame, text="Ver Productos", width=20, command=self.abrir_ventana_productos).pack(pady=5)
        ttk.Button(buttons_frame, text="Ver Ventas", width=20, command=self.ver_ventas).pack(pady=5)
        ttk.Button(buttons_frame, text="Ver Despachos", width=20, command=self.ver_despachos).pack(pady=5)
        ttk.Button(buttons_frame, text="Exportar Reporte", width=20).pack(pady=5)

        # Si necesitas una tabla o dashboard, puedes añadirla aquí
        self.create_dashboard()

    def ver_ventas(self):
        print("Acción para ver ventas")

    def create_dashboard(self):
        # Frame para la tabla (dashboard)
        table_frame = ttk.Frame(self, padding=10)
        table_frame.pack(fill="both", expand=True, padx=20, pady=20)

        tabla = ttk.Treeview(table_frame, columns=("col1", "col2", "col3"), show="headings", height=5)
        tabla.pack(side="left", fill="both", expand=True)

        # Configuración de las columnas
        tabla.heading("col1", text="Cantidad Afiliados")
        tabla.heading("col2", text="Total Ventas")
        tabla.heading("col3", text="Ganancias")
        tabla.column("col1", width=50, anchor="center")
        tabla.column("col2", width=150, anchor="center")
        tabla.column("col3", width=200, anchor="center")

        # Scrollbar para la tabla
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tabla.yview)
        scrollbar.pack(side="right", fill="y")
        tabla.configure(yscrollcommand=scrollbar.set)
    def ver_ventas(self):
        VentanaVentas(self)

    def ver_despachos(self):
        VentanaDespachos(self)

    def abrir_ventana_productos (self):
        VentanaProductos(self)



