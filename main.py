import tkinter as tk
from Interfaz.gestorInterfaces import GestorInterfaces
from Interfaz.ventanaPrincipal import HotelApp
from Datos.gestor_db import GestorDB

if __name__ == "__main__":
    root = tk.Tk()
    gestorBD = GestorDB()
    gestorI = GestorInterfaces(root, gestorBD)
    print("Abriendo ventana principal por main")
    gestorI.abrir_Ventana_Principal()
    #app = HotelApp(root, gestorI)
    #root.mainloop()