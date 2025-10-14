class Interpreter:
    def __init__(self):
        self.palabras = []
        self.etiquetas = {}
        self.i = 0
        self.halted = False
        self.output_lines = []
        self.reset_registros()
        self.load_file()

    def load_file(self):
        self.palabras = []
        self.etiquetas = {}
        self.i = 0
        self.halted = False
        self.output_lines = []
        with open("lenguaje_plano.txt", "r") as fichero:
            for linea in fichero:
                linea = linea.replace("\n", "")
                linea = linea.replace(",", "")
                if linea == "":
                    continue
                palabra = linea.split()
                self.palabras.append(palabra)
        # registrar etiquetas
        for idx in range(len(self.palabras)):
            if self.palabras[idx][0] == "tag" and len(self.palabras[idx]) > 1:
                self.etiquetas[self.palabras[idx][1]] = idx

    def reset_registros(self):
        self.registros = {
          "$t2": 2,
          "$t3": 3,
          "$t4": 4,
          "$t5": 5,
          "$t6": 6,
          "$t7": 7,
          "$t8": 8,
          "$t9": 9,
          "$t10": 10,
          "$res": 0,
          "$aux": 0
        }

    def current_instruction_str(self):
        if 0 <= self.i < len(self.palabras):
            return " ".join(self.palabras[self.i])
        else:
            return "(fin)"

    def step(self):
        if self.halted:
            return
        if not (0 <= self.i < len(self.palabras)):
            self.halted = True
            return

        palabras = self.palabras
        registros = self.registros
        etiquetas = self.etiquetas
        idx = self.i
        funcion = palabras[idx][0]

        # Obtener valor (registro o literal)
        def val(x):
            if x in registros:
                return registros[x]
            try:
                return int(x)
            except ValueError:
                return x

        # Instrucciones básicas
        if funcion == "mov":
            registros[palabras[idx][1]] = val(palabras[idx][2])

        elif funcion == "sum":
            registros[palabras[idx][1]] = val(palabras[idx][2]) + val(palabras[idx][3])

        elif funcion == "sub":
            registros[palabras[idx][1]] = val(palabras[idx][2]) - val(palabras[idx][3])

        elif funcion == "mul":
            registros[palabras[idx][1]] = val(palabras[idx][2]) * val(palabras[idx][3])

        elif funcion == "div":
            divisor = val(palabras[idx][3])
            registros[palabras[idx][1]] = val(palabras[idx][2]) // divisor if divisor != 0 else 0

        elif funcion == "pow":
            registros[palabras[idx][1]] = val(palabras[idx][2]) ** val(palabras[idx][3])

        elif funcion == "slt":
            registros[palabras[idx][1]] = 1 if val(palabras[idx][2]) < val(palabras[idx][3]) else 0

        elif funcion == "sgt":
            registros[palabras[idx][1]] = 1 if val(palabras[idx][2]) > val(palabras[idx][3]) else 0

        # Saltos
        elif funcion == "jmp":
            etiqueta = palabras[idx][1]
            if etiqueta in etiquetas:
                self.i = etiquetas[etiqueta]
                return
            self.output_lines.append("Etiqueta no encontrada")

        elif funcion == "jeq":
            reg1, reg2, etiqueta = palabras[idx][1], palabras[idx][2], palabras[idx][3]
            if val(reg1) == val(reg2):
                if etiqueta in etiquetas:
                    self.i = etiquetas[etiqueta]
                    return
                self.output_lines.append("Etiqueta no encontrada")

        elif funcion == "jne":
            reg1, reg2, etiqueta = palabras[idx][1], palabras[idx][2], palabras[idx][3]
            if val(reg1) != val(reg2):
                if etiqueta in etiquetas:
                    self.i = etiquetas[etiqueta]
                    return
                self.output_lines.append("Etiqueta no encontrada")

        # Llamadas al sistema
        elif funcion == "svc1":
            self.output_lines.append("FIN")
            self.halted = True
            return

        elif funcion == "svc2":
            var = palabras[idx][1]
            self.output_lines.append(str(int(registros.get(var, 0))))

        # Avanzar
        self.i += 1
