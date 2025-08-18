# Shipping Cost Calculator

while True:
    try:
        peso = float(input("Ingresa el peso del paquete en kilogramos: "))
        if peso <= 0:
            print("El peso debe ser un número positivo.")
            continue
        break
    except ValueError:
        print("Por favor, ingresa un número válido para el peso.")

while True:
    try:
        tarifa = float(input("Ingresa la tarifa de envío por kilogramo: "))
        if tarifa < 0:
            print("La tarifa no puede ser negativa.")
            continue
        break
    except ValueError:
        print("Por favor, ingresa un número válido para la tarifa.")

costo_envio = peso * tarifa

print(f"Costo de Envío: {costo_envio:.2f} USD")


