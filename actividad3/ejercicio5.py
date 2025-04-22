litros_totales = float(input("Ingrese el total de litros consumidos en el mes: "))
cantidad_personas = int(input("Ingrese la cantidad de personas en la vivienda: "))

consumo_mensual_por_persona = litros_totales / cantidad_personas
consumo_diario_por_persona = consumo_mensual_por_persona / 30

print("\n--- Reporte de Consumo de Agua ---")
print("Consumo total del mes:", litros_totales, "litros")
print("Cantidad de personas en la vivienda:", cantidad_personas)
print("Consumo mensual por persona:", round(consumo_mensual_por_persona, 2), "litros")
print("Consumo diario por persona:", round(consumo_diario_por_persona, 2), "litros")
