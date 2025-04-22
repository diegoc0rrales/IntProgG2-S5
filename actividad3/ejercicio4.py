distancia_km = float(input("Ingrese la distancia recorrida (en km): "))
litros_consumidos = float(input("Ingrese la cantidad de litros consumidos: "))
precio_por_litro = 47.82

rendimiento = distancia_km / litros_consumidos
gasto_total = litros_consumidos * precio_por_litro

print("\n--- Reporte de Consumo de Combustible ---")
print("Distancia recorrida:", distancia_km, "km")
print("Litros consumidos:", litros_consumidos, "litros")
print("Precio por litro: C$", precio_por_litro)
print("Rendimiento del vehículo:", round(rendimiento, 2), "km/l")
print("Gasto total en combustible: C$", round(gasto_total, 2))