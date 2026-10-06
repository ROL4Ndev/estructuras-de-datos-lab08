class NodoSanchez:
    def __init__(self, nombre_doc, paginas):
        self.nombre_doc = nombre_doc
        self.paginas = paginas
        self.siguiente = None

class ColaImpresionSanchez:
    def __init__(self):
        self.frente = None
        self.final = None

    def is_empty(self):
        return self.frente is None

    def enqueue(self, nombre_doc, paginas):
        nuevo_nodo = NodoSanchez(nombre_doc, paginas)
        if self.is_empty():
            self.frente = nuevo_nodo
            self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo

    def dequeue(self):
        if self.is_empty():
            return None
        doc_atendido = self.frente
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        return doc_atendido

    def mostrar_esperando(self):
        if self.is_empty():
            print("No hay documentos esperando.")
            return
        actual = self.frente
        print("Documentos esperando en cola:")
        while actual:
            print(f"- {actual.nombre_doc} ({actual.paginas} paginas)")
            actual = actual.siguiente

cola_sanchez = ColaImpresionSanchez()

print("EVENTO 1: Enviar Informe.pdf")
cola_sanchez.enqueue("Informe.pdf", 10)

print("EVENTO 2: Enviar Contrato.pdf")
cola_sanchez.enqueue("Contrato.pdf", 5)

print("EVENTO 3: Impresora termina primer documento")
doc = cola_sanchez.dequeue()
if doc:
    print(f"Impreso con exito: {doc.nombre_doc}")

print("EVENTO 4: Enviar Presentacion.pdf")
cola_sanchez.enqueue("Presentacion.pdf", 15)

print("EVENTO 5: Enviar Resumen.pdf")
cola_sanchez.enqueue("Resumen.pdf", 3)

print("EVENTO 6: Impresora termina siguiente documento")
doc = cola_sanchez.dequeue()
if doc:
    print(f"Impreso con exito: {doc.nombre_doc}")

print("EVENTO 7: Luis envia Manual.pdf")
cola_sanchez.enqueue("Manual.pdf", 20)

print("EVENTO 8: Impresora termina siguiente documento")
doc = cola_sanchez.dequeue()
if doc:
    print(f"Impreso con exito: {doc.nombre_doc}")

print("\nESTADO FINAL DE LA COLA")
cola_sanchez.mostrar_esperando()