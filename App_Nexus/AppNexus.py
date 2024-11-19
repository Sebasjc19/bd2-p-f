import tkinter as tk
from proyecto_final_nexus.Views.view_afiliado import VentanaPrincipal
from proyecto_final_nexus.Login import LoginWindow


class AppNexus(tk.Tk):
    def __init__(self):
        super().__init__()
        self.vistas = {}
        self.cargar_vistas()
        self.cambiar_vista("LoginWindow")

    def cargar_vistas(self):
        self.vistas["LoginWindow"] = LoginWindow(self, self)
        self.vistas["VentanaPrincipal"] = VentanaPrincipal(self)

    def cambiar_vista(self, vista_nombre):
        for vista in self.vistas.values():
            vista.pack_forget()

        vista = self.vistas[vista_nombre]
        vista.pack(fill="both", expand=True)
