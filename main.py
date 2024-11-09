import tkinter as tk
from tkinter import ttk
from Interfaz.ventanaPrincipal import HotelApp


if __name__ == "__main__":
    root = tk.Tk()
    #Se debe ejecutar el Gestor Interfaces 
    #y este mismo tiene que llamar a la ventana principal (Menu)
    app = HotelApp(root)
    root.mainloop()