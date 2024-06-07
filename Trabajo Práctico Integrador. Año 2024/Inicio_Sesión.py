import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import json
import os
from Ventana_Productos import Ventana_Productos_Vendedor
from Ventana_Vendedor import ventana_Vendedor

Farmaceuticos = []
Empleados = []

def cargar_usuarios():
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r") as file:
            try:
                return json.load(file)
            except json.decoder.JSONDecodeError:
                return {}
    else:
        return {}

def guardar_usuario(username, password, tipo_usuario):
    usuarios = cargar_usuarios()

    if username in usuarios:
        messagebox.showerror("Error", "El nombre de usuario ya existe")
        return

    nuevo_usuario = {
        "nombre": username,
        "contrasena": password
    }

    if tipo_usuario == "Farmaceutico":
        Farmaceuticos.append(nuevo_usuario)
    elif tipo_usuario == "Empleado":
        Empleados.append(nuevo_usuario)

    with open("usuarios.json", "w") as file:
        json.dump({"Farmaceuticos": Farmaceuticos, "empleados": Empleados}, file, indent=4)

    messagebox.showinfo("Éxito", "Usuario creado exitosamente")

def crear_usuario():
    ventana_creacion = tk.Toplevel()
    ventana_creacion.title("Crear Usuario")
    ventana_creacion.geometry("300x200")
    ventana_creacion.configure(bg="lightgreen")

    username_label_creacion = tk.Label(ventana_creacion, text="Nombre de Usuario:", bg="lightgreen", fg="navy", font=("Arial", 12, "bold"))
    username_label_creacion.pack()
    username_entry_creacion = tk.Entry(ventana_creacion)
    username_entry_creacion.pack()

    password_label_creacion = tk.Label(ventana_creacion, text="Contraseña:", bg="lightgreen", fg="navy", font=("Arial", 12, "bold"))
    password_label_creacion.pack()
    password_entry_creacion = tk.Entry(ventana_creacion, show="*")
    password_entry_creacion.pack()

    tipo_usuario_label_creacion = tk.Label(ventana_creacion, text="Tipo de Usuario:", bg="lightgreen", fg="navy", font=("Arial", 12, "bold"))
    tipo_usuario_label_creacion.pack()
    tipo_usuario_var_creacion = tk.StringVar()
    tipo_usuario_var_creacion.set("Farmaceutico")
    tipo_usuario_menu_creacion = tk.OptionMenu(ventana_creacion, tipo_usuario_var_creacion, "Farmaceutico", "Empleado")
    tipo_usuario_menu_creacion.pack()
    tipo_usuario_menu_creacion.configure(bg="black", fg="blue", font=("Arial", 12, "bold"))

    crear_usuario_button_creacion = tk.Button(ventana_creacion, text="Crear Usuario", command=lambda: guardar_usuario(username_entry_creacion.get(), password_entry_creacion.get(), tipo_usuario_var_creacion.get()), bg="black", fg="red", font=("Arial", 12, "bold"))
    crear_usuario_button_creacion.pack()

def login():
    username = username_entry.get()
    password = password_entry.get()
    tipo_usuario = tipo_usuario_var.get()

    usuarios = cargar_usuarios()

    if tipo_usuario == "Farmaceutico":
        if "Farmaceuticos" in usuarios:
            for usuario in usuarios["Farmaceuticos"]:
                if usuario["nombre"] == username and usuario["contrasena"] == password:
                    Ventana_Productos_Vendedor()
                    ventana_login.destroy()
                    return
        else:
            messagebox.showerror("Error", "No hay usuarios farmaceuticos registrados.")
    elif tipo_usuario == "Empleado":
        if "empleados" in usuarios:
            for usuario in usuarios["empleados"]:
                if usuario["nombre"] == username and usuario["contrasena"] == password:
                    ventana_Vendedor()
                    ventana_login.destroy()
                    return
        else:
            messagebox.showerror("Error", "No hay usuarios empleados registrados.")

    messagebox.showerror("Error", "Nombre de usuario o contraseña incorrectos")
#-----------------------------------------------------------------------------------
def mostrar_login():
    ventana_inicio.withdraw()
    ventana_login.deiconify()

def salir():
    ventana_inicio.destroy()

ventana_inicio = tk.Tk()
ventana_inicio.title("Sistema de Venta")
ventana_inicio.geometry("820x730")
ventana_inicio.configure(bg="lightblue")

imagen = Image.open("Sistema de Venta.jpg")
imagen_tk = ImageTk.PhotoImage(imagen)

canvas = tk.Canvas(ventana_inicio, width=820, height=730)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=imagen_tk)

canvas_width = 820
button_width = 150  

salir_button = tk.Button(ventana_inicio, text="Salir", command=salir, bg="red", fg="white", font=("Arial", 16, "bold"), width=10, height=2)
salir_button_window = canvas.create_window((canvas_width / 2) - (button_width * 1.5), 680, window=salir_button)

continuar_button = tk.Button(ventana_inicio, text="Continuar", command=mostrar_login, bg="green", fg="white", font=("Arial", 16, "bold"), width=10, height=2)
continuar_button_window = canvas.create_window((canvas_width / 2) + (button_width / 2), 680, window=continuar_button)

ventana_login = tk.Toplevel(ventana_inicio)
ventana_login.title("Inicio de Sesión")
ventana_login.geometry("300x280")
ventana_login.configure(bg="lightgreen")
ventana_login.withdraw()

titulo = tk.Label(ventana_login, text="Inicio de Sesión", bg="lightgreen", fg="red", font=("Arial", 20, "bold"))
titulo.pack(pady=10)

username_label = tk.Label(ventana_login, text="Nombre de Usuario:", bg="lightgreen", fg="navy", font=("Arial", 12, "bold"))
username_label.pack()
username_entry = tk.Entry(ventana_login)
username_entry.pack()

password_label = tk.Label(ventana_login, text="Contraseña:", bg="lightgreen", fg="navy", font=("Arial", 12, "bold"))
password_label.pack()
password_entry = tk.Entry(ventana_login, show="*")
password_entry.pack()

tipo_usuario_label = tk.Label(ventana_login, text="Tipo de Usuario:", bg="lightgreen", fg="navy", font=("Arial", 12, "bold"))
tipo_usuario_label.pack()
tipo_usuario_var = tk.StringVar()
tipo_usuario_var.set("Farmaceutico")
tipo_usuario_menu = tk.OptionMenu(ventana_login, tipo_usuario_var, "Farmaceutico", "Empleado")
tipo_usuario_menu.pack()
tipo_usuario_menu.configure(bg="black", fg="red", font=("Arial", 12, "bold"))

login_button = tk.Button(ventana_login, text="Iniciar Sesión", command=login, bg="black", fg="blue", font=("Arial", 12, "bold"))
login_button.pack()

registro_button = tk.Button(ventana_login, text="Registrar Usuario", command=crear_usuario, bg="black", fg="blue", font=("Arial", 12, "bold"))
registro_button.pack()

ventana_inicio.mainloop()