from te import Te

# Crear instancias
te1 = Te()
te2 = Te()

# Obtener tipos de datos de las instancias
tipo_te1 = type(te1)
tipo_te2 = type(te2)

# Mostrar tipos de datos almacenados
print("Tipo de te1:", tipo_te1)
print("Tipo de te2:", tipo_te2)

# Verificar si los tipos son iguales
if tipo_te1 == tipo_te2:
    print("Ambos objetos son del mismo tipo")
else:
    print("Los objetos no son del mismo tipo")
