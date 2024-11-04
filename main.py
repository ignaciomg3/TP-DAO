import tkinter as tk
from Interfaz.gui import HotelApp
gestorBaseDatos = GestorDB()
gestorBaseDatos.borrar_base_de_datos()
gestorBaseDatos.crear_tablas()
if __name__ == "__main__":
    root = tk.Tk()
    app = HotelApp(root)
    root.mainloop()