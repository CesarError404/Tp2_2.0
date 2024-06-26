import tkinter as tk
from tkinter import *
import json
from tkinter import messagebox

def salir():
    Venta_Proveedores.destroy()

def dar_de_alta():
    if validar_campos():
        nombre = entrada_nombre.get()
        precio = entrada_precio.get()
        cantidad = entrada_cantidad.get()
        codigo = entrada_codigo.get()
        fecha = entrada_fecha.get()
        presentacion = entrada_presentacion.get()
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad,
            "codigo": codigo,
            "fecha de vencimiento": fecha,
            "presentacion": presentacion
        }
        lista_productos.append(producto)
        guardar_json()
        actualizar_lista()
        
        entrada_nombre.delete(0, tk.END)
        entrada_precio.delete(0, tk.END)
        entrada_cantidad.delete(0, tk.END)
        entrada_codigo.delete(0, tk.END)
        entrada_fecha.delete(0, tk.END)
        entrada_presentacion.delete(0, tk.END)


def validar_campos():
    nombre = entrada_nombre.get()
    precio = entrada_precio.get()
    cantidad = entrada_cantidad.get()
    codigo = entrada_codigo.get()
    fecha = entrada_fecha.get()
    presentacion = entrada_presentacion.get()
    
    if not nombre or not precio or not cantidad or not codigo or not fecha or not presentacion:
        messagebox.showerror("Error", "Por favor ingrese todos los campos.")
        return False
    
    if not nombre.isalpha():
        messagebox.showerror("Error", "El nombre no puede contener números.")
        return False
    if not presentacion.isalpha():
        messagebox.showerror("Error", "La presentación no puede contener números")
        return False
    
    try:
        float(precio)
        float(cantidad)
        if not all(char.isdigit() or char == '/' for char in fecha):
            messagebox.showerror("Error en Fecha", "La fecha de vencimiento solo puede contener números y '/'.")
            return False
        int(fecha.split('/')[2])
    except ValueError as e:
        messagebox.showerror("Error", f"El precio y la cantidad deben ser números.")
        return False
    else:
        return True


def guardar_json():
    with open("CatalogodeProductos.json", "w") as file:
        json.dump(lista_productos, file, indent=4)

precioM_entrada = None
cantidadS_M_entrada = None
codigoM_entrada = None
fechaM_entrada = None
presentacionM_entrada = None
ventana_modificar = None

def abrir_modificar_venta():
    global precioM_entrada, cantidadS_M_entrada, codigoM_entrada, fechaM_entrada, precioM_entrada, presentacionM_entrada, ventana_modificar

    ventana_modificar = tk.Toplevel(Venta_Proveedores)
    ventana_modificar.title("Modificar Productos")
    ventana_modificar.geometry("400x323")
    ventana_modificar.configure(bg="lightblue")

    precioM = tk.Label(ventana_modificar, text="Precio:", bg="black", fg="red", font=("Arial", 12, "bold"))
    precioM.pack(pady=5)
    precioM_entrada = tk.Entry(ventana_modificar)
    precioM_entrada.pack()

    cantidadS_M = tk.Label(ventana_modificar, text="Cantidad de Stock:", bg="black", fg="red", font=("Arial", 12, "bold"))
    cantidadS_M.pack(pady=5)
    cantidadS_M_entrada = tk.Entry(ventana_modificar)
    cantidadS_M_entrada.pack()
    
    codigoM = tk.Label(ventana_modificar, text="Código:", bg="black", fg="red", font=("Arial", 12, "bold"))
    codigoM.pack(pady=5)
    codigoM_entrada = tk.Entry(ventana_modificar)
    codigoM_entrada.pack()

    fecha_M = tk.Label(ventana_modificar, text="Fecha de Vencimiento:", bg="black", fg="red", font=("Arial", 12, "bold"))
    fecha_M.pack(pady=5)
    fechaM_entrada = tk.Entry(ventana_modificar)
    fechaM_entrada.pack()
    
    presentacion_M = tk.Label(ventana_modificar, text="Presentación:", bg="black", fg="red", font=("Arial", 12, "bold"))
    presentacion_M.pack(pady=5)
    presentacionM_entrada = tk.Entry(ventana_modificar)
    presentacionM_entrada.pack()
    
    boton_M = tk.Button(ventana_modificar, text="Modificar", command=modificar_producto, bg="black", fg="green", font=("Arial", 12, "bold"))
    boton_M.pack(pady=10)

def modificar_producto():
    global precioM_entrada, cantidadS_M_entrada, codigoM_entrada, fechaM_entrada, presentacionM_entrada, ventana_modificar

    seleccionado = marco.curselection()
    if seleccionado:
        indice = seleccionado[0]
        producto = lista_productos[indice]

        nuevo_precio = precioM_entrada.get()
        nueva_cantidad = cantidadS_M_entrada.get()
        nuevo_codigo = codigoM_entrada.get()
        nueva_fecha = fechaM_entrada.get()
        nueva_presentacion = presentacionM_entrada.get()
        if validar_campos_modificacion(nuevo_precio, nueva_cantidad, nuevo_codigo, nueva_fecha, nueva_presentacion):
            producto["precio"] = nuevo_precio
            producto["cantidad"] = nueva_cantidad
            producto["codigo"] = nuevo_codigo
            producto["fecha de vencimiento"] = nueva_fecha
            producto["presentacion"] = nueva_presentacion

            guardar_json()
            actualizar_lista()
            ventana_modificar.destroy()
           
def validar_campos_modificacion(precio, cantidad, codigo, fecha, presentacion):
    if not precio or not cantidad or not codigo or not fecha or not presentacion:
        messagebox.showerror("Error", "Por favor ingrese todos los campos.")
        return False
    if not presentacion.isalpha():
        messagebox.showerror("Error", "La presentación no puede contener números")
        return False
    try:
        float(precio)
        float(cantidad)
        if not all(char.isdigit() or char == '/' for char in fecha):
            messagebox.showerror("Error en Fecha", "La fecha de vencimiento solo puede contener números y '/'.")
            return False
        int(fecha.split('/')[2])
    except ValueError:
        messagebox.showerror("Error", "El precio y la cantidad deben ser números válidos.")
        return False

    return True

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
        fecha = producto.get('fecha de vencimiento', 'N/A')
        presentacion = producto.get('presentacion', 'N/A')
        marco.insert(tk.END, f"{nombre} - Precio: {precio} - Cantidad: {cantidad} - Código: {codigo} - Fecha de Vencimiento: {fecha} - Presentacion: {presentacion}")

def cargar_datos_json():
    global lista_productos
    try:
        with open("CatalogodeProductos.json", "r") as file:
            lista_productos = json.load(file)
    except FileNotFoundError:
        lista_productos = []
        
def buscar_producto():
    busqueda = entrada_busqueda.get().lower()
    marco.delete(0, tk.END)
    for producto in lista_productos:
        nombre = producto.get('nombre', 'N/A')
        precio = producto.get('precio', 'N/A')
        cantidad = producto.get('cantidad', 'N/A')
        codigo = producto.get('codigo', 'N/A')
        fecha = producto.get('fecha de vencimiento', 'N/A')
        presentacion = producto.get('presentacion', 'N/A')
        if busqueda in nombre.lower() or busqueda in codigo.lower():
            marco.insert(tk.END, f"{nombre} - Precio: {precio} - Cantidad: {cantidad} - Código: {codigo} - Fecha de Vencimiento: {fecha}- Presentacion: {presentacion}")


def Ventana_Productos():
    global marco, lista_productos, Venta_Proveedores, entrada_nombre, entrada_precio, entrada_cantidad, entrada_codigo, entrada_fecha, entrada_presentacion, entrada_busqueda

    cargar_datos_json()

    Venta_Proveedores = tk.Tk()
    Venta_Proveedores.geometry("1000x625")
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
    
    etiqueta_fecha =  Label(Venta_Proveedores, text="Fecha de Vencimiento:", bg="black", fg="red", font=("Arial", 12, "bold"))
    etiqueta_fecha.place(x=200, y=140)
    entrada_fecha = Entry(Venta_Proveedores)
    entrada_fecha.place(x=385, y=140)

    etiqueta_presentacion =  Label(Venta_Proveedores, text="Presentación:", bg="black", fg="red", font=("Arial", 12, "bold"))
    etiqueta_presentacion.place(x=200, y=170)
    entrada_presentacion = Entry(Venta_Proveedores)
    entrada_presentacion.place(x=395, y=170)


    boton_alta = Button(Venta_Proveedores, text="Agregar Producto", command=dar_de_alta, bg="black", fg="green", font=("Arial", 12, "bold"))
    boton_alta.place(x=540, y=200)

    boton_eliminar = Button(Venta_Proveedores, text="Eliminar Producto", command=eliminar, bg="black", fg="green", font=("Arial", 12, "bold"))
    boton_eliminar.place(x=370, y=200)

    boton_modificar_producto = Button(Venta_Proveedores, text="Modificar producto", command=abrir_modificar_venta, bg="black", fg="green", font=("Arial", 12, "bold"))
    boton_modificar_producto.place(x=200, y=200)

    boton_Salir = tk.Button(Venta_Proveedores, text="Salir", command=salir)
    boton_Salir.place(x=50, y=200, width=110, height=30)
    boton_Salir.configure(bg="black", fg="green", font=("Arial", 12, "bold"))
    
    marco = Listbox(Venta_Proveedores, width=80, height=20)
    marco.place(x=200, y=239)

    scrollbar = tk.Scrollbar(Venta_Proveedores, orient=tk.VERTICAL)
    scrollbar.place(x=682, y=239, height=320)
    
    marco.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=marco.yview)

    scrollbar_horizontal = tk.Scrollbar(Venta_Proveedores, orient=tk.HORIZONTAL)
    marco.config(xscrollcommand=scrollbar_horizontal.set)
    
    scrollbar_horizontal.place(x=200, y=559, width=485)
    scrollbar_horizontal.config(command=marco.xview)

    etiqueta_busqueda =  Label(Venta_Proveedores, text="Buscar Producto:", bg="black", fg="red", font=("Arial", 12, "bold"))
    etiqueta_busqueda.place(x=200, y=590)
    entrada_busqueda = Entry(Venta_Proveedores)
    entrada_busqueda.place(x=350, y=590)
    
    boton_buscar = Button(Venta_Proveedores, text="Buscar", command=buscar_producto, bg="black", fg="green", font=("Arial", 12, "bold"))
    boton_buscar.place(x=490, y=590)
    actualizar_lista()
   
