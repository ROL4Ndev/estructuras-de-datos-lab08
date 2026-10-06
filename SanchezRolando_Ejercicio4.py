class StackSanchez:
    def __init__(self):
        self.elementos = []

    def push(self, item):
        self.elementos.append(item)

    def pop(self):
        if not self.is_empty():
            return self.elementos.pop()
        return None

    def is_empty(self):
        return len(self.elementos) == 0

def decimal_a_binario_sanchez(numero_decimal):
    if numero_decimal == 0:
        return "0"

    stack_sanchez = StackSanchez()
    numero_actual = abs(numero_decimal)

    while numero_actual > 0:
        residuo = numero_actual % 2
        stack_sanchez.push(residuo)
        numero_actual = numero_actual // 2

    representacion_binaria = ""
    while not stack_sanchez.is_empty():
        representacion_binaria += str(stack_sanchez.pop())

    if numero_decimal < 0:
        representacion_binaria = "-" + representacion_binaria

    return representacion_binaria

if __name__ == "__main__":
    numeros_prueba = [10, 45, 128, 255]
    for num in numeros_prueba:
        resultado = decimal_a_binario_sanchez(num)
        print(f"El numero decimal {num} en binario es: {resultado}")