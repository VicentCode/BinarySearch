class busqueda:
    def busquedaBinaria(self, array, izq, der, objetivo):
        pasos = 0
        while izq <= der:
            medio = int(--(izq + der)/2)
            pasos = pasos+1
            try:
                if array[medio] == objetivo:
                    print("NUMERO DE PASOS:", pasos)
                    return medio
                if array[medio] < objetivo:
                    izq = medio + 1
                else:
                    der = medio -1
            except:
                print("NUMERO DE PASOS:", pasos)
                return None
        print("NUMERO DE PASOS:", pasos)

        return None

    def menu(self, objetivo, tipo):
        global resul
        if tipo is not None:
            x = ["Roger", "Martin", "Alfonso","Maria", "Gonzalo", "Florencia"
                    , "Rodolfo", "Soledad", "Octavio"]
            x.sort()
            size = len(x)
            resul = self.busquedaBinaria(x, 0, size, objetivo)
        else:
            x = list(range(0, 50000000, 3))
            print(x[8333333])
            size = len(x)
            resul = self.busquedaBinaria(x, 0, size, objetivo)
        if resul is None:
            print("No se encontro el elemento")
        else:
            print("El elemento:", objetivo, "fue encontrado en la posicion", resul,"de la lista")

b = busqueda()
g = True
while g:
    print("----------MENU----------")
    print("¿Que desea hacer?")
    print("Buscar la posicion de un numero entero: 1-.")
    print("Buscar la posicion de un de texto: 2-.")
    print("Salir 3-.")

    m = int(input("Seleccione una opcion: "))
    if m ==1:
        objetivo = int(input("Ingrese el numero del 3 al 500,000,000  y "
                                "multiplo de 3 para buscar su posicion: "))
        b.menu(objetivo, None)
    elif m == 2:
        print("Alfonso","Florencia","Gonzalo", "Maria"
                    , "Martin", "Octavio","Rodolfo","Roger", "Soledad", )
        objetivo = input("Ingrese el texto a buscar: ")
        b.menu(objetivo, "string")
    elif m == 3:
        print("Adios :)")
        g = False
    else:
        print("Opcion no valida, intente una opcion permitida en el menu")





## medio == 24999999, posicion 8333333