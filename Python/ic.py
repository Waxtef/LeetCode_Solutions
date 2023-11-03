monto_inicial = 0  # Monto inicial de la inversión
inversion_mensual = 20000  # Inversión mensual adicional
tasa_anual = 0.10  # Tasa de interés anual (10%)

# Número de años para calcular
num_anios = 4  # Puedes cambiar este valor según tu necesidad

# Inicializar el saldo total
saldo_total = monto_inicial

# Calcular el saldo total después de cada año
for _ in range(num_anios):
    saldo_total += inversion_mensual * 12  # Inversión anual
    saldo_total *= 1 + tasa_anual  # Interés compuesto

# Imprimir el saldo total al final de los años especificados
print("El saldo total después de", num_anios, "años es:", round(saldo_total, 2))
