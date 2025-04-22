capital_inicial = float(input("Ingrese el capital inicial: "))
tasa_porcentual = float(input("Ingrese la tasa de interés anual (en %): "))
años = int(input("Ingrese la cantidad de años: "))

tasa_decimal = tasa_porcentual / 100
factor_interes = (1 + tasa_decimal) ** años
monto_final = capital_inicial * factor_interes
interes_ganado = monto_final - capital_inicial

print("\n--- Cálculo de Interés Compuesto ---")
print("Capital inicial:", round(capital_inicial, 2))
print("Tasa de interés anual:", tasa_porcentual, "%")
print("Años:", años)
print("Monto final:", round(monto_final, 2))
print("Interés ganado:", round(interes_ganado, 2))
