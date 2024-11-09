import tkinter as tk
from Interfaz.gestorInterfaces import GestorInterfaces
from Interfaz.ventanaPrincipal import HotelApp


if __name__ == "__main__":
    root = tk.Tk()
    gestor = GestorInterfaces(root)
    app = HotelApp(root, gestor)
    root.mainloop()