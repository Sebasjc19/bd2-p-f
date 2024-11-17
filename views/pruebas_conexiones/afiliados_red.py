import tkinter as tk
from tkinter import ttk
from model.afiliados.afiliado import afiliado
from views.pruebas_propias.registro_afiliado import VentanaRegistroAfiliado


# Clase para la ventana de Afiliados
class VentanaAfiliados:
    def __init__(self, root, sesion):
        self.root = root
        self.root.title("Lista de Afiliados")
        self.root.geometry("400x300")
        self.sesion = sesion  # Guardamos el objeto sesión

        # Crear un Treeview para mostrar la lista de afiliados
        tree = ttk.Treeview(self.root, columns=("ID", "Nombre", "Rango"), show="headings")
        tree.heading("ID", text="ID Afiliado")
        tree.heading("Nombre", text="Nombre")
        tree.heading("Rango", text="Rango")

        # Botón para registrar un nuevo afiliado
        self.boton_registrar = tk.Button(self.root, text="Registrar Afiliado", command=self.abrir_ventana_registro)
        self.boton_registrar.pack(padx=10, pady=20)

        lista_afiliados = afiliado.mostrarAfiliadosPromotor(sesion.id_afiliado)

        # Insertar los afiliados en el Treeview
        for elemento in lista_afiliados:
            tree.insert("", tk.END, values=elemento)

        # Colocar el Treeview en la ventana
        tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def abrir_ventana_registro(self):
        # Abrir la ventana de registro de afiliado
        ventana_registro = tk.Toplevel(self.root)
        VentanaRegistroAfiliado(ventana_registro, self.sesion)
