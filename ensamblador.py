from Stack import Stack
import math

# Abrir fichero
lineas = []
palabras = []
callStack = Stack(10)  # call stack

registros = {  # registros para los "tréboles"
    "$t2": 2,
    "$t3": 3,
    "$t4": 4,
    "$t5": 5,
    "$t6": 6,
    "$t7": 7,
    "$t8": 8,
    "$t9": 9,
    "$t10": 10,
    "$res": 0,  # registro auxiliar para resultados
    "$aux": 0
}

etiquetas = {}  # diccionario para las etiquetas (sirve para los saltos)

with open("lenguaje_plano.txt", 'r') as fichero:
    for linea in fichero:
        linea = linea.replace("\n", "")  # eliminar saltos de línea
        lineas.append(linea)
        palabra = linea.split()  # separar la línea en palabras
        palabras.append(palabra)

# Mostrar resultados
print(palabras)

# Registrar etiquetas antes del bucle principal
for i in range(len(palabras)):
    if palabras[i][0] == 'tag':
        etiquetas[palabras[i][1]] = i  # nombre de la etiqueta + índice de línea

i = 0  # contador

while i < len(palabras):
    if palabras[i][0] == 'mov':
        try:
            registros[palabras[i][1]] = registros[palabras[i][2]]
        except:
            registros[palabras[i][1]] = int([palabras[i][2]])
        

    elif palabras[i][0] == 'call':
        callStack.push(i + 1)  # guardar posición de retorno
        funcion = palabras[i][1]
        reg1, reg2, reg_res = palabras[i][2], palabras[i][3], palabras[i][4]

        if funcion == 'sum':
            try:
                registros[reg_res] = registros[reg1] + registros[reg2]
            except:
                registros[reg_res] = registros[reg1] + int(reg2)

        elif funcion == 'sub':
            try:
                registros[reg_res] = registros[reg1] - registros[reg2]
            except:
                registros[reg_res] = registros[reg1] - int(reg2)

        elif funcion == 'mul':
            try:
                registros[reg_res] = registros[reg1] * registros[reg2]
            except:
                registros[reg_res] = registros[reg1] * int(reg2)

        elif funcion == 'div':
            try:
                registros[reg_res] = registros[reg1] // registros[reg2] if registros[reg2] != 0 else 0
            except:
                divisor = int(reg2)
                registros[reg_res] = registros[reg1] // divisor if divisor != 0 else 0

        elif funcion == 'pow':
            try:
                registros[reg_res] = registros[reg1] ** registros[reg2]
            except:
                registros[reg_res] = registros[reg1] ** int(reg2)

        elif funcion == 'slt':  # set lower than
            try:
                registros[reg_res] = registros[reg1] < registros[reg2]
            except:
                registros[reg_res] = registros[reg1] < int(reg2)

        elif funcion == 'sgt':  # set greater than
            try:
                registros[reg_res] = registros[reg1] > registros[reg2]
            except:
                registros[reg_res] = registros[reg1] > int(reg2)

    elif palabras[i][0] == 'jmp':  # salto incondicional
        etiqueta = palabras[i][1]
        if etiqueta in etiquetas:
            i = etiquetas[etiqueta]
            continue
        else:
            print('Etiqueta no encontrada')

    elif palabras[i][0] == 'svc2':  # print
        var = palabras[i][1]
        print(int(registros[var]))

    elif palabras[i][0] == 'svc1':  # terminar ejecución
        print("Terminando ejecución")
        break

    elif palabras[i][0] == 'ret':
        if not callStack.isEmpty():
            i = callStack.pop()
            continue
        else:
            print("Error: callstack vacía")

    elif palabras[i][0] == 'jeq':  # salto si son iguales
        reg1, reg2, etiqueta = palabras[i][1], palabras[i][2], palabras[i][3]
        if registros[reg1] == registros[reg2]:
            if etiqueta in etiquetas:
                i = etiquetas[etiqueta]
                continue
            else:
                print("Etiqueta no encontrada")

    elif palabras[i][0] == 'jne':  # salto si son diferentes
        reg1, reg2, etiqueta = palabras[i][1], palabras[i][2], palabras[i][3]
        if registros[reg1] != registros[reg2]:
            if etiqueta in etiquetas:
                i = etiquetas[etiqueta]
                continue
            else:
                print("Etiqueta no encontrada")

    i += 1

# Depuración final
print("\n--- Estado final ---")
print("Registros:", registros)
print("Pila de llamadas:", callStack)
print("Etiquetas:", etiquetas)
