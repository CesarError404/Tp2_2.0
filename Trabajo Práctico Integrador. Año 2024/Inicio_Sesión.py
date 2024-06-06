import tkinter as tk
from tkinter import messagebox
import json
import os
from Ventana_Productos import Ventana_Productos_Vendedor
from Ventana_Vendedor import ventana_Vendedor

Administradores = []
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

    if tipo_usuario == "Administrador":
        Administradores.append(nuevo_usuario)
    elif tipo_usuario == "Empleado":
        Empleados.append(nuevo_usuario)

    with open("usuarios.json", "w") as file:
        json.dump({"administradores": Administradores, "empleados": Empleados}, file, indent=4)

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
    tipo_usuario_var_creacion.set("Administrador") 
    tipo_usuario_menu_creacion = tk.OptionMenu(ventana_creacion, tipo_usuario_var_creacion, "Administrador", "Empleado")
    tipo_usuario_menu_creacion.pack()
    tipo_usuario_menu_creacion.configure(bg="black", fg="blue", font=("Arial", 12, "bold"))
  
    crear_usuario_button_creacion = tk.Button(ventana_creacion, text="Crear Usuario", command=lambda: guardar_usuario(username_entry_creacion.get(), password_entry_creacion.get(), tipo_usuario_var_creacion.get()), bg="black", fg="red", font=("Arial", 12, "bold"))
    crear_usuario_button_creacion.pack()

    
def login():
    username = username_entry.get()
    password = password_entry.get()
    tipo_usuario = tipo_usuario_var.get()

    usuarios = cargar_usuarios()

    if tipo_usuario == "Administrador":
        if "administradores" in usuarios:
            for usuario in usuarios["administradores"]:
                if usuario["nombre"] == username and usuario["contrasena"] == password:
                    Ventana_Productos_Vendedor()
                    
                    ventana_login.destroy()
                    return
        else:
            messagebox.showerror("Error", "No hay usuarios administradores registrados.")
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


ventana_login = tk.Tk()
ventana_login.title("Inicio de Sesión")
ventana_login.geometry("300x280")
ventana_login.configure(bg="lightgreen")

titulo = tk.Label(text="Inicio de Sesión", bg="lightgreen", fg="red", font=("Arial", 20, "bold"))
titulo.pack(pady=10)

username_label = tk.Label(ventana_login, text="Nombre de Usuario:", bg="lightgreen", fg="navy", font=("Arial", 12, "bold") )
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
tipo_usuario_var.set("Administrador") 
tipo_usuario_menu = tk.OptionMenu(ventana_login, tipo_usuario_var, "Administrador", "Empleado")
tipo_usuario_menu.pack()
tipo_usuario_menu.configure(bg="black", fg="red", font=("Arial", 12, "bold"))

login_button = tk.Button(ventana_login, text="Iniciar Sesión", command=login,bg="black", fg="blue", font=("Arial", 12, "bold"))
login_button.pack()

registro_button = tk.Button(ventana_login, text="Registrar Usuario", command=crear_usuario, bg="black", fg="blue", font=("Arial", 12, "bold"))
registro_button.pack()

ventana_login.mainloop()