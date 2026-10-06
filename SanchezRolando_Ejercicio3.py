class NodoSanchez:
    def __init__(self, palabra):
        self.palabra = palabra
        self.anterior = None

class PilaEditorSanchez:
    def __init__(self):
        self.tope = None

    def is_empty(self):
        return self.tope is None

    def push(self, palabra):
        nuevo_nodo = NodoSanchez(palabra)
        nuevo_nodo.anterior = self.tope
        self.tope = nuevo_nodo

    def pop(self):
        if self.is_empty():
            return None
        palabra_eliminada = self.tope.palabra
        self.tope = self.tope.anterior
        return palabra_eliminada

    def mostrar_texto(self):
        if self.is_empty():
            print("Texto actual: (vacio)")
            return
        
        palabras = []
        actual = self.tope
        while actual:
            palabras.append(actual.palabra)
            actual = actual.anterior
        palabras.reverse()
        print("Texto actual:", " ".join(palabras))

def menu_editor():
    editor_sanchez = PilaEditorSanchez()
    while True:
        print("\nEDITOR DE TEXTO SIMPLE")
        print("1. Escribir palabra")
        print("2. Deshacer ultima palabra")
        print("3. Mostrar texto actual")
        print("4. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            palabra = input("Ingrese una palabra: ").strip()
            editor_sanchez.push(palabra)
            print(f"Palabra '{palabra}' agregada.")
        elif opcion == "2":
            eliminada = editor_sanchez.pop()
            if eliminada:
                print(f"Deshecho: se elimino la palabra '{eliminada}'")
            else:
                print("No hay palabras para deshacer.")
        elif opcion == "3":
            editor_sanchez.mostrar_texto()
        elif opcion == "4":
            print("Saliendo del editor...")
            break
        else:
            print("Opcion invalida.")

if __name__ == "__main__":
    menu_editor()