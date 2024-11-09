import tkinter as tk
from tkinter import ttk
from Interfaz.ventanaPrincipal import HotelApp

if __name__ == "__main__":
    root = tk.Tk()
    app = HotelApp(root)
    root.mainloop()