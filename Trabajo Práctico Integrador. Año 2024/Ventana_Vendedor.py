import tkinter as tk
from tkinter import *
import json
from tkinter import messagebox

productos = []

def cargar_productos_desde_json():
    try:
        with open("CatalogodeProductos.json", "r") as file:
            contenido = file.read()
            print("Contenido del archivo JSON:")
            print(contenido)
            return json.loads(contenido)
    except FileNotFoundError:
        return []

def actualizar_stock(lista_productos):
    lista_productos.delete(0, tk.END)
    for producto in productos:
        lista_productos.insert(tk.END, f"{producto['nombre']} - Precio: {producto['precio']} - Cantidad: {producto['cantidad']}")

def vender_producto(lista_productos, entrada_cantidad):
    producto_seleccionado = lista_productos.curselection()
    cantidad_str = entrada_cantidad.get()
    if cantidad_str.isdigit():
        cantidad = int(cantidad_str)
        if producto_seleccionado:
            indice = producto_seleccionado[0]
            producto = productos[indice]
            cantidad_producto = int(producto['cantidad']) 
            if cantidad_producto >= cantidad:
                producto['cantidad'] = str(cantidad_producto - cantidad)  
                actualizar_stock(lista_productos)
                messagebox.showinfo("Venta Exitosa", f"Se han vendido {cantidad} unidades de {producto['nombre']}. Nuevo stock: {producto['cantidad']}")
            else:
                messagebox.showerror("Error", "No hay suficiente stock para esa cantidad.")
        else:
            messagebox.showerror("Error", "Por favor, seleccione un producto.")
    else:
        messagebox.showerror("Error", "La cantidad debe ser un número entero.")

def ventana_Vendedor():
    global productos
    productos = cargar_productos_desde_json()

    venta_vendedor = tk.Tk()
    venta_vendedor.geometry("600x400")
    venta_vendedor.title("Sistema de Farmacias")
    venta_vendedor.configure(bg="orange")

    etiqueta_cantidad = Label(venta_vendedor, text="Cantidad a vender:", bg="black", fg="green", font=("Arial", 12, "bold") )
    etiqueta_cantidad.place(x=200, y=50)
    entrada_cantidad = Entry(venta_vendedor)
    entrada_cantidad.place(x=370, y=50)

    lista_productos = Listbox(venta_vendedor, width=40, height=15)
    lista_productos.place(x=200, y=100)
    actualizar_stock(lista_productos)

    boton_vender = Button(venta_vendedor, text="Vender", command=lambda: vender_producto(lista_productos, entrada_cantidad), bg="black", fg="blue", font=("Arial", 12, "bold"))
    boton_vender.place(x=90, y=100)

    boton_salir = tk.Button(venta_vendedor, text="Salir", command=venta_vendedor.quit)
    boton_salir.place(x=50, y=350, width=110, height=30)
    boton_salir.configure(bg="black", fg="blue", font=("Arial", 12, "bold"))

    



