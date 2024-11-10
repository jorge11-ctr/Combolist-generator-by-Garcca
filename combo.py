import random
import string
import tkinter as tk
from tkinter import messagebox

# Listas de sílabas comunes para nombres y apellidos
silabas_nombre = ['an', 'bel', 'car', 'dan', 'el', 'fer', 'gar', 'hel', 'iv', 'jon', 'kar', 'le', 'mar', 'no', 'os', 'per', 'qui', 'ra', 'san', 'ti']
silabas_apellido = ['al', 'bal', 'con', 'del', 'es', 'fer', 'gon', 'hez', 'il', 'jan', 'kil', 'laz', 'mez', 'noz', 'os', 'per', 'qui', 'rez', 'sal', 'tor']
dominios = ['gmail.com', 'yahoo.com', 'outlook.com']

# Función para generar nombres ficticios
def generar_nombre():
    nombre = ''.join(random.choices(silabas_nombre, k=2)).capitalize()
    apellido = ''.join(random.choices(silabas_apellido, k=2)).capitalize()
    return nombre, apellido

# Función para generar correos electrónicos más realistas
def generar_email(nombre, apellido):
    dominio = random.choice(dominios)
    return f'{nombre}.{apellido}@{dominio}'

# Función para generar contraseñas más complejas y relacionadas con el correo
def generar_password(nombre, apellido):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    base_password = nombre[:3] + apellido[:3]  # Usamos los primeros 3 caracteres del nombre y apellido
    additional_chars = ''.join(random.choices(caracteres, k=6))
    password = base_password + additional_chars
    return password

# Función para generar la combolist
def generar_combolist(cantidad):
    with open('combolist.txt', 'w') as file:
        for _ in range(cantidad):
            nombre, apellido = generar_nombre()
            email = generar_email(nombre, apellido)
            password = generar_password(nombre, apellido)
            file.write(f'{email}:{password}\n')

    messagebox.showinfo("Éxito", f"Combolist generada y guardada en combolist.txt con {cantidad} entradas")

# Función para manejar el botón de generación
def on_generate_button_click():
    try:
        cantidad = int(entry.get())
        if cantidad > 0:
            generar_combolist(cantidad)
        else:
            messagebox.showerror("Error", "Por favor, ingresa un número positivo")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido")

# Configurar la interfaz gráfica de usuario
root = tk.Tk()
root.title("Generador de Combolist")

tk.Label(root, text="Cantidad de correos a generar:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Generar", command=on_generate_button_click).pack(pady=20)

root.mainloop()

