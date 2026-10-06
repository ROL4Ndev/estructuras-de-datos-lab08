class NodoSanchez:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None

class ColaSanchez:
    def __init__(self):
        self.frente = None
        self.final = None

    def is_empty(self):
        return self.frente is None

    def enqueue(self, nombre):
        nuevo_nodo = NodoSanchez(nombre)
        if self.is_empty():
            self.frente = nuevo_nodo
            self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo

    def dequeue(self):
        if self.is_empty():
            return None
        persona = self.frente.nombre
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        return persona

class SistemaBancoSanchez:
    def __init__(self):
        self.cola_clientes = ColaSanchez()
        self.cola_no_clientes = ColaSanchez()
        self.turno_v2_no_cliente = True

    def agregar_persona(self):
        nombre = input("Ingrese el nombre de la persona: ")
        es_cliente = input("Es cliente? (s/n): ").strip().lower()
        if es_cliente == 's':
            self.cola_clientes.enqueue(nombre)
            print(f"{nombre} agregado a la cola de CLIENTES.")
        else:
            self.cola_no_clientes.enqueue(nombre)
            print(f"{nombre} agregado a la cola de NO CLIENTES.")

    def atender_ventanilla_1(self):
        persona = self.cola_clientes.dequeue()
        if persona:
            print(f"Ventanilla 1 atendio a CLIENTE: {persona}")
        else:
            print("Ventanilla 1: No hay clientes en espera.")

    def atender_ventanilla_2(self):
        if self.turno_v2_no_cliente:
            persona = self.cola_no_clientes.dequeue()
            if persona:
                print(f"Ventanilla 2 atendio a NO CLIENTE: {persona}")
                self.turno_v2_no_cliente = False
            else:
                persona = self.cola_clientes.dequeue()
                if persona:
                    print(f"Ventanilla 2 atendio a CLIENTE (alternativo): {persona}")
                else:
                    print("Ventanilla 2: No hay personas en ninguna cola.")
        else:
            persona = self.cola_clientes.dequeue()
            if persona:
                print(f"Ventanilla 2 atendio a CLIENTE: {persona}")
                self.turno_v2_no_cliente = True
            else:
                persona = self.cola_no_clientes.dequeue()
                if persona:
                    print(f"Ventanilla 2 atendio a NO CLIENTE (alternativo): {persona}")
                else:
                    print("Ventanilla 2: No hay personas en ninguna cola.")

def menu():
    banco_sanchez = SistemaBancoSanchez()
    while True:
        print("\nMENU BANCO")
        print("1. Agregar persona")
        print("2. Atender en Ventanilla 1 (Solo Clientes)")
        print("3. Atender en Ventanilla 2 (Alternado)")
        print("4. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            banco_sanchez.agregar_persona()
        elif opcion == "2":
            banco_sanchez.atender_ventanilla_1()
        elif opcion == "3":
            banco_sanchez.atender_ventanilla_2()
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion invalida, intente de nuevo.")

if __name__ == "__main__":
    menu()