class Calculadora:
    def suma(self, a, b):
        c = a + b
        #print(c)
        return c

    def resta(self, a, b):
        c = a - b
        #print(c)
        return c

    def divide(self, a, b):
        if b == 0:
            raise ValueError("División por cero detectada")

        c = a / b
        #print(c)
        return c

    # En el PDF no se pide método de multiplicar asi que jijiijjji
    # Ya que yo no voy a correr el código directamente,
    # imprimir el valor de "c" no sirve de nada.

    # Adicionalmente, en test_calculadora.py se espera
    # un error "ValueError", por lo que debo definirlo
    # explícitamente o se arrojará un ZeroDivisonError