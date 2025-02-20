# Recibir_lista es una función que retorna una lista cargada por el usuario
def recibir_lista():
    # Recibimos el tamaño de la lista de base de datos
    tam = int(input("Ingrese el tamaño de la lista: "))

    # Recibimos los números en una sola línea y verificamos que cumplan con el tamaño especificado
    listNumBD = list(map(int, input(f"Ingrese {tam} números separados por espacios: ").split()))

    # Validamos que el usuario ingrese exactamente "tam" números
    while len(listNumBD) != tam:
        print(f"Debe ingresar exactamente {tam} números.")
        listNumBD = list(map(int, input(f"Ingrese {tam} números nuevamente: ").split()))
    return listNumBD

# Función que busca los vecinos de un número en una lista
def buscar_vecinos(listaBD, num):
    vMenor = None  # Vecino menor al consultado (mayor menor)
    vMayor = None  # Vecino mayor al consultado (menor mayor)

    for numIterador in listaBD:
        if numIterador < num:
            vMenor = numIterador
        elif numIterador > num and vMayor is None:
            vMayor = numIterador
            break  # Detenemos el ciclo ya que la lista está ordenada

    return vMenor, vMayor

# Utilizamos la anterior función para recibir las listas de BD y evaluación
print("\n**** Lista de BD ****")
listaBD = recibir_lista()
print("\n**** Lista a evaluar ****")
listaEvaluar = recibir_lista()

# Aseguramos que la lista de BD esté ordenada
listaBD.sort()

# Recorremos la lista de evaluación para hallar los números vecinos
print("\n\n**** Vecinos ****")
for num in listaEvaluar:
    menor, mayor = buscar_vecinos(listaBD, num)
    #Ahora imprimimos los numeros 
    print(f" {menor if menor is not None else 'X'} {mayor if mayor is not None else 'X'}\n")




