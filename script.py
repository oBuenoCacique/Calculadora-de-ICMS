def calcular_icms(valor_nota, aliquota):
    return valor_nota * (aliquota / 100)

print("=== Calculadora de ICMS ===")

valor_nota = float(input("Valor da nota fiscal: R$ "))
aliquota = float(input("Alíquota do ICMS (%): "))

valor_icms = calcular_icms(valor_nota, aliquota)

print("\nResultado")
print("-" * 20)
print(f"Valor da Nota: R$ {valor_nota:.2f}")
print(f"Alíquota: {aliquota}%")
print(f"ICMS Calculado: R$ {valor_icms:.2f}")