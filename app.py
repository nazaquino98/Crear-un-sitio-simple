import tkinter as tk

# Función para actualizar el contenido de la caja de texto
def update_text():
    display_box.delete(0, tk.END)
    display_box.insert(0, text_box.get())

# Función para cambiar el color de fondo y texto
color_index = 0
colors = [
    {"bg": "white", "fg": "black"},
    {"bg": "black", "fg": "white"},
    {"bg": "lightblue", "fg": "red"}
]

def change_color():
    global color_index
    color_index = (color_index + 1) % len(colors)
    display_box.config(bg=colors[color_index]["bg"], fg=colors[color_index]["fg"])

# Crear ventana principal
root = tk.Tk()
root.title("Sitio Simple")
root.geometry("400x200")

# Crear widgets
text_box = tk.Entry(root, font=("Arial", 14))
text_box.pack(pady=10)

enter_button = tk.Button(root, text="Enviar", command=update_text)
enter_button.pack(pady=5)

color_button = tk.Button(root, text="Cambiar Color", command=change_color)
color_button.pack(pady=5)

display_box = tk.Entry(root, font=("Arial", 14))
display_box.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
