import tkinter as tk
from tkinter import ttk, messagebox
from proyecto_final_nexus.Views.view_ventas import VentanaVentas
from proyecto_final_nexus.Views.view_despachos import VentanaDespachos
from proyecto_final_nexus.Views.view_productos import VentanaProductos
from proyecto_final_nexus.model.Afiliado.afiliado import afiliado
from proyecto_final_nexus.model.Afiliado.afiliado import Sesion
from proyecto_final_nexus.Views.view_registro_afiliados import RegistroAfiliado


# Clase para la ventana principal

class VentanaPrincipal(tk.Tk):
    def __init__(self, sesion: Sesion):
        super().__init__()
        self.title("Gestión de Afiliados")
        self.geometry("900x500")  # Tamaño de la ventana
        self.configure(bg="#f0f0f0")  # Fondo de la ventana

        self.sesion = sesion

        self.create_widgets()

    def create_widgets(self):
        # Frame para el botón de desvincular, alineado a la derecha
        desvincular_frame = ttk.Frame(self, padding=10)
        desvincular_frame.grid(row=1, column=1, sticky="ne", padx=20, pady=(10, 20))  # 'ne' para alinear a la esquina superior derecha

        # Botón para desvincularse (ubicado en el frame de la parte superior derecha)
        desvincular_button = ttk.Button(desvincular_frame, text="¿Deseas desvincularte?", width=20, command= self.desvincular)
        desvincular_button.grid(row=1, column=4)  # Colocamos el botón a la derecha dentro del frame

        # Título principal
        title_label = ttk.Label(self, text="Gestión de Afiliados", font=("Arial", 16, "bold"), background="#f0f0f0")
        title_label.grid(row=1, column=2, columnspan=2, pady=(20, 10))  # Centrado

        # Información del Afiliado
        info_frame = ttk.Frame(self, padding=10)
        info_frame.grid(row=2, column=0, columnspan=2, padx=20, pady=(10, 20), sticky="ew")

        # Acceder a los datos del afiliado desde el objeto 'sesion'
        self.nombre_label = ttk.Label(info_frame, text=f"Nombre: {self.sesion.nombre}", font=("Arial", 12), background="#f0f0f0")
        self.email_label = ttk.Label(info_frame, text=f"Email: {self.sesion.email}", font=("Arial", 12), background="#f0f0f0")
        self.rango_label = ttk.Label(info_frame, text=f"Rango: {self.sesion.id_rango}", font=("Arial", 12), background="#f0f0f0")

        # Colocamos las etiquetas en el grid
        self.nombre_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.email_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.rango_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        # Botones adicionales
        buttons_frame = ttk.Frame(self, padding=10)
        buttons_frame.grid(row=3, column=1, columnspan=2, padx=20, pady=10, sticky="ew")
        ttk.Button(buttons_frame, text="Registrar afiliado", width=20, command=self.abrir_ventana_registros).grid(row=0, column=0, pady=5)
        ttk.Button(buttons_frame, text="Ver Productos", width=20, command=self.abrir_ventana_productos).grid(row=1, column=0, pady=5)
        ttk.Button(buttons_frame, text="Ver Ventas", width=20, command=self.ver_ventas).grid(row=2, column=0, pady=5)
        ttk.Button(buttons_frame, text="Ver Despachos", width=20, command=self.ver_despachos).grid(row=3, column=0, pady=5)
        ttk.Button(buttons_frame, text="Exportar Reporte", width=20).grid(row=4, column=0, pady=5)

        # Crear dashboard (tabla o panel)
        self.create_dashboard()

    def ver_ventas(self):
        print("Acción para ver ventas")

    def create_dashboard(self):
        # Frame para el dashboard
        table_frame = ttk.Frame(self, padding=10)
        table_frame.grid(row=3, column=2, columnspan=2, padx=20, pady=20, sticky="nsew")

        tabla = ttk.Treeview(table_frame, columns=("col1", "col2", "col3"), show="headings", height=5)
        tabla.grid(row=0, column=0, sticky="nsew")

        # Configuración de las columnas
        tabla.heading("col1", text="Cantidad Afiliados")
        tabla.heading("col2", text="Total Ventas")
        tabla.heading("col3", text="Ganancias")
        tabla.column("col1", width=50, anchor="center")
        tabla.column("col2", width=150, anchor="center")
        tabla.column("col3", width=200, anchor="center")

        # Scrollbar para la tabla
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tabla.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        tabla.configure(yscrollcommand=scrollbar.set)
    def ver_ventas(self):
        VentanaVentas(self)

    def ver_despachos(self):
        VentanaDespachos(self)

    def abrir_ventana_productos (self):
        VentanaProductos(self)

    def abrir_ventana_registros(self):
        RegistroAfiliado(self, self.sesion.id_afiliado)

    def desvincular(self):

        confirmacion = messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas desvincularte?")
        if confirmacion:
            try:
                id_afiliado = self.sesion.id_afiliado

                afiliado.eliminarAfiliado(id_afiliado)

                messagebox.showinfo("Éxito", "Afiliado desvinculado correctamente")
                self.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Error al desvincularte: {e}")