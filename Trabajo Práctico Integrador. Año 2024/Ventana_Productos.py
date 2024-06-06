import tkinter as tk
from tkinter import *
import json
from tkinter import messagebox

def salir():
    Venta_Proveedores.destroy()

def salirM():
    abrir_modificar_venta
    

def dar_de_alta():
    if validar_campos():
        nombre = entrada_nombre.get()
        precio = entrada_precio.get()
        cantidad = entrada_cantidad.get()
        codigo = entrada_codigo.get()
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad,
            "codigo": codigo
        }
        lista_productos.append(producto)
        guardar_json()
        actualizar_lista()

def validar_campos():
    nombre = entrada_nombre.get()
    precio = entrada_precio.get()
    cantidad = entrada_cantidad.get()
    codigo = entrada_codigo.get()
    
    if not nombre or not precio or not cantidad or not codigo:
        messagebox.showerror("Error", "Por favor ingrese todos los campos.")
        return False
    
    if not nombre.isalpha():
        messagebox.showerror("Error", "El nombre no puede contener números.")
        return False
    
    try:
        float(precio)
        float(cantidad)
        float(codigo)
    except ValueError:
        messagebox.showerror("Error", "El precio, la cantidad y el código deben ser números.")
        return False
    
    return True

# Función para guardar los datos en un archivo JSON
def guardar_json():
    with open("CatalogodeProductos.json", "w") as file:
        json.dump(lista_productos, file, indent=4)

precioM_entrada = None
cantidadS_M_entrada = None
codigoM_entrada = None

# Función para abrir la ventana de modificación de productos
def abrir_modificar_venta():
    global precioM_entrada, cantidadS_M_entrada, codigoM_entrada

    ventana_modificar = tk.Toplevel(Venta_Proveedores)
    ventana_modificar.title("Modificar Productos")
    ventana_modificar.geometry("400x210")
    ventana_modificar.configure(bg="lightblue")

    precioM = tk.Label(ventana_modificar, text="Precio:", bg="black", fg="red", font=("Arial", 12, "bold"))
    precioM.pack()

    precioM_entrada = tk.Entry(ventana_modificar)
    precioM_entrada.pack(pady=5)

    cantidadS_M = tk.Label(ventana_modificar, text="Cantidad de Stock:", bg="black", fg="red", font=("Arial", 12, "bold"))
    cantidadS_M.pack(pady=5)
    
    cantidadS_M_entrada = tk.Entry(ventana_modificar)
    cantidadS_M_entrada.pack(pady=5)
    
    codigoM = tk.Label(ventana_modificar, text="Código:", bg="black", fg="red", font=("Arial", 12, "bold"))
    codigoM.pack(pady=5)
    codigoM_entrada = tk.Entry(ventana_modificar)
    codigoM_entrada.pack()

    boton_M = tk.Button(ventana_modificar, text="Modificar", command=modificar, bg="black", fg="green", font=("Arial", 12, "bold"))
    boton_M.pack(pady=10)
   
    boton_M = tk.Button(ventana_modificar, text="Salir", command=salirM, bg="black", fg="green", font=("Arial", 12, "bold"))
    boton_M.pack(pady=10)
   


def modificar():
    global precioM_entrada, cantidadS_M_entrada, codigoM_entrada

    seleccionado = marco.curselection()
    if seleccionado:
        indice = seleccionado[0]
        producto = lista_productos[indice]
        nuevo_precio = precioM_entrada.get()
        nueva_cantidad = cantidadS_M_entrada.get()
        nuevo_codigo = codigoM_entrada.get()

        if nuevo_precio.isdigit() and nueva_cantidad.isdigit() and nuevo_codigo.isdigit():
            producto["precio"] = nuevo_precio
            producto["cantidad"] = nueva_cantidad
            producto["codigo"] = nuevo_codigo
            guardar_json()
            actualizar_lista()
        else:
            messagebox.showerror("Error", "Los valores modificados deben ser números.")

# Función para eliminar un producto de la lista
def eliminar():
    seleccionado = marco.curselection()
    if seleccionado:
        indice = seleccionado[0]
        lista_productos.pop(indice)
        guardar_json()
        actualizar_lista()


def actualizar_lista():
    marco.delete(0, tk.END)
    for producto in lista_productos:
        nombre = producto.get('nombre', 'N/A')
        precio = producto.get('precio', 'N/A')
        cantidad = producto.get('cantidad', 'N/A')
        codigo = producto.get('codigo', 'N/A')
        marco.insert(tk.END, f"{nombre} - Precio: {precio} - Cantidad: {cantidad} - Código: {codigo}")

# Función para cargar los datos desde un archivo JSON
def cargar_datos_json():
    global lista_productos
    try:
        with open("CatalogodeProductos.json", "r") as file:
            lista_productos = json.load(file)
    except FileNotFoundError:
        lista_productos = []

# Función principal para crear la ventana del vendedor
def Ventana_Productos_Vendedor():
    global marco, lista_productos, Venta_Proveedores, entrada_nombre, entrada_precio, entrada_cantidad, entrada_codigo

    cargar_datos_json()

    Venta_Proveedores = tk.Tk()
    Venta_Proveedores.geometry("1080x550")
    Venta_Proveedores.title("Sistema de Farmacias")
    Venta_Proveedores.configure(bg="blue")
    
    etiqueta_nombre = Label(Venta_Proveedores, text="Nombre del Producto:", bg="black", fg="red", font=("Arial", 12, "bold"))
    etiqueta_nombre.place(x=200, y=20)
    entrada_nombre = Entry(Venta_Proveedores)
    entrada_nombre.place(x=380, y=20)

    etiqueta_precio = Label(Venta_Proveedores, text="Precio del Producto:", bg="black", fg="red", font=("Arial", 12, "bold"))
    etiqueta_precio.place(x=200, y=50)
    entrada_precio = Entry(Venta_Proveedores)
    entrada_precio.place(x=370, y=50)

    etiqueta_cantidad = Label(Venta_Proveedores, text="Cantidad en Stock:", bg="black", fg="red", font=("Arial", 12, "bold"))
    etiqueta_cantidad.place(x=200, y=80)
    entrada_cantidad = Entry(Venta_Proveedores)
    entrada_cantidad.place(x=370, y=80)
    
    etiqueta_codigo = Label(Venta_Proveedores, text="Código del producto:", bg="black", fg="red", font=("Arial", 12, "bold"))
    etiqueta_codigo.place(x=200, y=110)
    entrada_codigo = Entry(Venta_Proveedores)
    entrada_codigo.place(x=375, y=110)

    boton_alta = Button(Venta_Proveedores, text="Agregar Producto", command=dar_de_alta, bg="black", fg="green", font=("Arial", 12, "bold"))
    boton_alta.place(x=540, y=150)

    boton_eliminar = Button(Venta_Proveedores, text="Eliminar Producto", command=eliminar, bg="black", fg="green", font=("Arial", 12, "bold"))
    boton_eliminar.place(x=370, y=150)

    boton_modificar_producto = Button(Venta_Proveedores, text="Modificar producto", command=abrir_modificar_venta, bg="black", fg="green", font=("Arial", 12, "bold"))
    boton_modificar_producto.place(x=200, y=150)

    boton_Salir = tk.Button(Venta_Proveedores, text="Salir", command=salir)
    boton_Salir.place(x=50, y=155, width=110, height=30)
    boton_Salir.configure(bg="black", fg="green", font=("Arial", 12, "bold"))

    marco = Listbox(Venta_Proveedores, width=80, height=20)
    marco.place(x=200, y=190)

    scrollbar = tk.Scrollbar(Venta_Proveedores, orient=tk.VERTICAL)
    scrollbar.place(x=1080, y=150, height=320)

    actualizar_lista()

