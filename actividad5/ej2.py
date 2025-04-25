sueldo=float(input("Ingrese su sueldo: "))
bono=0

if sueldo > 3000:
    bono= sueldo * 0.1
    print(f"Su sueldo es de: {sueldo}, y su bono es de: {bono:.2f}")
elif sueldo > 1500 and sueldo <= 3000:
    bono= sueldo * 0.05
    print(f"Su sueldo es de: {sueldo}, y su bono es de: {bono:.2f}")
elif sueldo <= 1500 and sueldo >= 0:
    print("Usted no tiene bono a su favor.")
else:
    print("Error, salario no valido")

print(f"Salario total {sueldo + bono:.2f}")