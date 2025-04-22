inventario_inicial = int(input("Ingrese la cantidad inicial en inventario: "))
productos_recibidos = int(input("Ingrese la cantidad de productos recibidos: "))
productos_vendidos = int(input("Ingrese la cantidad de productos vendidos: "))

inventario_actual = inventario_inicial + productos_recibidos - productos_vendidos

print("\n--- Reporte de Inventario ---")
print("Inventario inicial:", inventario_inicial)
print("Productos recibidos:", productos_recibidos)
print("Productos vendidos:", productos_vendidos)
print("Inventario final disponible:", inventario_actual)
