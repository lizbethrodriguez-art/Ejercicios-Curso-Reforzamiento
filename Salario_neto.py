# Programa para calcular salario neto 
salario_bruto = float(input("Salario bruto: "))
porcentaje = float(input("% Impuestos: "))
deduciones =float(input("Deduciones: "))
impuesto = salario_bruto *(porcentaje / 100)
salario_neto = salario_bruto - impuesto - deduciones
print("Salario neto:", salario_neto)