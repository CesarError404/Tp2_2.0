import tkinter as tk
from tkinter import *
import json
from tkinter import messagebox

productos = []
ventas = []

def cargar_productos_desde_json():
    try:
        with open("CatalogodeProductos.json", "r") as file:
            contenido = file.read()
            print("Contenido del archivo JSON:")
            print(contenido)
            return json.loads(contenido)
    except FileNotFoundError:
        return []

def guardar_ventas_en_json():
    try:
        with open("Ventas.json", "w") as file:
            json.dump(ventas, file, indent=4)
    except Exception as e:
        print(f"Error al guardar las ventas: {e}")

def actualizar_stock(lista_productos):
    lista_productos.delete(0, tk.END)
    for producto in productos:
        nombre = producto.get('nombre', 'N/A')
        precio = producto.get('precio', 'N/A')
        cantidad = producto.get('cantidad', 'N/A')
        codigo = producto.get('codigo', 'N/A')
        fecha = producto.get('fecha de vencimiento', 'N/A')
        presentacion = producto.get('presentacion', 'N/A')
        lista_productos.insert(tk.END, f"Nombre: {nombre} - Precio: {precio} - Cantidad: {cantidad} - Codigo: {codigo} - Fecha: {fecha} - Presentacion: {presentacion}")

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
                ventas.append({'nombre': producto['nombre'], 'precio': producto['precio'], 'cantidad': cantidad})  
                actualizar_stock(lista_productos)
                messagebox.showinfo("Venta Exitosa", f"Se han vendido {cantidad} unidades de {producto['nombre']}. Nuevo stock: {producto['cantidad']}")
                guardar_ventas_en_json()  
            else:
                messagebox.showerror("Error", "No hay suficiente stock para esa cantidad.")
        else:
            messagebox.showerror("Error", "Por favor, seleccione un producto.")
    else:
        messagebox.showerror("Error", "La cantidad debe ser un número entero.")

def buscar_producto(lista_productos, entrada_busqueda):
    busqueda = entrada_busqueda.get().lower()
    lista_productos.delete(0, tk.END)
    for producto in productos:
        nombre = producto.get('nombre', 'N/A')
        precio = producto.get('precio', 'N/A')
        cantidad = producto.get('cantidad', 'N/A')
        codigo = producto.get('codigo', 'N/A')
        fecha = producto.get('fecha de vencimiento', 'N/A')
        presentacion = producto.get('presentacion', 'N/A')
        if busqueda in nombre.lower() or busqueda in codigo.lower():
            lista_productos.insert(tk.END, f"Nombre: {nombre} - Precio: {precio} - Cantidad: {cantidad} - Codigo: {codigo} - Fecha: {fecha} - Presentacion: {presentacion}")

def informe_ventas():
    total_ventas = 0
    informe = "Informe de Ventas:\n\n"
    for venta in ventas:
        nombre = venta['nombre']
        precio = float(venta['precio'])
        cantidad = venta['cantidad']
        total_venta = precio * cantidad
        total_ventas += total_venta
        informe += f"Producto: {nombre} - Cantidad: {cantidad} - Precio Unitario: {precio} - Total Venta: {total_venta}\n"
    informe += f"\nTotal de Ventas: {total_ventas}"
    messagebox.showinfo("Informe de Ventas", informe)
   
    with open("Ventas.json", "w") as file:
        json.dump({"ventas": ventas, "total_ventas": total_ventas}, file, indent=4)

def ventana_Vendedor():
    global productos
    productos = cargar_productos_desde_json()

    venta_vendedor = tk.Tk()
    venta_vendedor.geometry("1000x625")
    venta_vendedor.title("Sistema de Farmacias")
    venta_vendedor.configure(bg="orange")

    etiqueta_cantidad = Label(venta_vendedor, text="Cantidad a vender:", bg="black", fg="green", font=("Arial", 12, "bold") )
    etiqueta_cantidad.place(x=200, y=50)
    entrada_cantidad = Entry(venta_vendedor)
    entrada_cantidad.place(x=370, y=50)

    lista_productos = Listbox(venta_vendedor, width=80, height=20)
    lista_productos.place(x=200, y=100)
    actualizar_stock(lista_productos)

    scrollbar_vertical = tk.Scrollbar(venta_vendedor, orient=tk.VERTICAL)
    scrollbar_vertical.place(x=683, y=100, height=320)
    lista_productos.config(yscrollcommand=scrollbar_vertical.set)
    scrollbar_vertical.config(command=lista_productos.yview)

    scrollbar_horizontal = tk.Scrollbar(venta_vendedor, orient=tk.HORIZONTAL)
    scrollbar_horizontal.place(x=200, y=420, width=485)
    lista_productos.config(xscrollcommand=scrollbar_horizontal.set)
    scrollbar_horizontal.config(command=lista_productos.xview)

    boton_vender = Button(venta_vendedor, text="Vender", command=lambda: vender_producto(lista_productos, entrada_cantidad), bg="black", fg="blue", font=("Arial", 12, "bold"))
    boton_vender.place(x=90, y=100)

    boton_salir = tk.Button(venta_vendedor, text="Salir", command=venta_vendedor.quit)
    boton_salir.place(x=50, y=350, width=110, height=30)
    boton_salir.configure(bg="black", fg="blue", font=("Arial", 12, "bold"))

    etiqueta_busqueda = Label(venta_vendedor, text="Buscar Producto:", bg="black", fg="green", font=("Arial", 12, "bold") )
    etiqueta_busqueda.place(x=200, y=450)
    entrada_busqueda = Entry(venta_vendedor)
    entrada_busqueda.place(x=350, y=450)

    boton_buscar = Button(venta_vendedor, text="Buscar", command=lambda: buscar_producto(lista_productos, entrada_busqueda), bg="black", fg="blue", font=("Arial", 12, "bold"))
    boton_buscar.place(x=500, y=450)

    boton_informe = Button(venta_vendedor, text="Informe de Ventas", command=informe_ventas, bg="black", fg="blue", font=("Arial", 12, "bold"))
    boton_informe.place(x=750, y=100)

