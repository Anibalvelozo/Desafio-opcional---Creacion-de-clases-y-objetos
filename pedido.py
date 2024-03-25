from te import Te

# Solicitar datos al usuario
sabor = int(input("Ingrese el número correspondiente al sabor de té (1: Té negro, 2: Té verde, 3: Agua de hierbas): "))
formato = int(input("Ingrese el formato de té (300 gr o 500 gr): "))

# Obtener tiempo, recomendación y precio
tiempo, recomendacion = Te.obtener_tiempo_y_recomendacion(sabor)
precio = Te.obtener_precio(formato)

# Mostrar detalle del pedido
print("\nDetalle del pedido:")
print("Sabor del té:", "Té negro" if sabor == 1 else ("Té verde" if sabor == 2 else "Agua de hierbas"))
print("Formato:", formato, "gr")
print("Precio: $", precio)
print("Tiempo de preparación:", tiempo, "minutos")
print("Recomendación:", recomendacion)
print("Gracias por su compra")