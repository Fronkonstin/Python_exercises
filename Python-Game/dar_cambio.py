import random

def generar_compra():
    return round(random.uniform(3, 200), 2)

def generar_pago(compra):
    return round(random.uniform(compra + 0.01, compra * 2), 2)

def calcular_cambio(compra, pago):
    return round(pago - compra, 2)

def juego():
    while True:
        compra = generar_compra()
        pago = generar_pago(compra)
        print("\n")
        print(f"La compra es de {compra} euros\n")
        print(f"El cliente paga con {pago} euros\n")
        while True:
            try:
                cambio_usuario = float(input("¿Cuánto cambio crees que debes dar? (solo números enteros o con decimales)\n"))
                break
            except ValueError:
                print("Error: solo se pueden introducir números enteros o con decimales. Por favor, inténtelo de nuevo.\n")
        cambio_real = calcular_cambio(compra, pago)
        if cambio_usuario < cambio_real:
            print(f"Te has quedado corto. El cambio correcto es {cambio_real} euros\n")
        elif cambio_usuario > cambio_real:
            print(f"Te has pasado con el cambio. El cambio correcto es {cambio_real} euros\n")
        else:
            print("Gracias, hasta otra\n")
        respuesta = input("¿Te gustaría atender a otro cliente? (si/no)\n").lower()
        if respuesta != "si":
            break

juego()