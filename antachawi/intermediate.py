from antachawi.shared import symbol_table
from tabulate import tabulate
import os

class IntermediateCodeGenerator:
    def __init__(self):
        self.symbol_table = symbol_table
        self.current_scope = "global"
        self.intermediate_code = []
        self.temp_count = 0
        self.label_count = 0

    def new_temp(self):
        temp_name = f"t{self.temp_count}"
        self.temp_count += 1
        return temp_name
    
    def new_label(self):
        label_name = f"L{self.label_count}"
        self.label_count += 1
        return label_name

    def visit(self, node):
        if node.name == "Programa":
            self.visit_programa(node)
        elif node.name == "Definicion":
            self.visit_definicion(node)
        elif node.name == "ListaSentencias":
            self.visit_lista_sentencias(node)
        elif node.name == "Sentencias":
            self.visit_sentencias(node)
        elif node.name == "Declaraciones":
            self.visit_declaraciones(node)
        elif node.name == "DeclaracionesPrime":
            return self.visit_declaraciones_prime(node)
        elif node.name == "Asignaciones":
            self.visit_asignaciones(node)
        elif node.name == "Impresiones":
            self.visit_impresiones(node)
        elif node.name == "Condicional":
            self.visit_condicional(node)
        elif node.name == "CondicionalPrime":
            self.visit_condicional_prime(node)
        elif node.name == "ExpresionCondicion":
            self.visit_expresion_condicion(node)
        elif node.name == "ExpresionRelacional":
            self.visit_expresion_relacional(node)
        elif node.name == "ExpresionCondicionPrime":
            self.visit_expresion_condicion_prime(node)
        elif node.name == "Expresion":
            return self.visit_expresion(node)
        elif node.name == "ExpresionMultiplicativa":
            return self.visit_expresion_multiplicativa(node)
        elif node.name == "ExpresionAditivaPrime":
            return self.visit_expresion_aditiva_prime(node)
        elif node.name == "ExpresionMultiplicativaPrime":
            return self.visit_expresion_multiplicativa_prime(node)
        elif node.name == "Termino":
            return self.visit_termino(node)
        elif node.name == "Tipo":
            return self.visit_tipo(node)
        return None, None

    def visit_programa(self, node):
        for child in node.children:
            self.visit(child)

    def visit_definicion(self, node):
        self.current_scope = "local"
        for child in node.children:
            self.visit(child)
        self.current_scope = "global"

    def visit_lista_sentencias(self, node):
        for child in node.children:
            self.visit(child)

    def visit_sentencias(self, node):
        for child in node.children:
            self.visit(child)

    def visit_declaraciones(self, node):
        tipo, _ = self.visit(node.children[0])
        nombre = node.children[1].children[0].name
        _, valor = self.visit(node.children[2])
        self.symbol_table.add(nombre, tipo, self.current_scope, valor)
        if valor:
            self.intermediate_code.append(f"{nombre} = {valor}")

    def visit_declaraciones_prime(self, node):
        if len(node.children) > 1:
            return self.visit(node.children[1])
        return None, None

    def visit_asignaciones(self, node):
        nombre = node.children[0].children[0].name
        _, valor = self.visit(node.children[2])
        self.symbol_table.set_value(nombre, valor)
        self.intermediate_code.append(f"{nombre} = {valor}")

    def visit_impresiones(self, node):
        expresion_impresion = node.children[2]
        valores = self.visit_expresion_impresion(expresion_impresion)
        for valor, _ in valores:
            self.intermediate_code.append(f"PRINT {valor}")

    def visit_expresion_impresion(self, node):
        valores = []
        child = node.children[0]
        left_type, left_value = self.visit(child)
        valores.append((left_value, left_type))
        if node.children[1].children:
            valores.extend(self.visit_expresion_impresion_prime(node.children[1]))
        return valores

    def visit_expresion_impresion_prime(self, node):
        valores = []
        if node.children:
            valores.extend(self.visit_expresion_impresion(node.children[1]))
        return valores
    
    def visit_expresion(self, node):
        left_type, left_value = self.visit(node.children[0])
        if node.children[1].children:
            operator = node.children[1].children[0].children[0].name
            _, right_value = self.visit(node.children[1])
            if left_value and right_value:
                temp = self.new_temp()
                self.intermediate_code.append(f"{temp} = {left_value} {operator} {right_value}")
                return left_type, temp
        return left_type, left_value

    def visit_expresion_multiplicativa(self, node):
        left_type, left_value = self.visit(node.children[0])
        if node.children[1].children:
            operator = node.children[1].children[0].children[0].name
            _, right_value = self.visit(node.children[1])
            if left_value and right_value:
                temp = self.new_temp()
                self.intermediate_code.append(f"{temp} = {left_value} {operator} {right_value}")
                return left_type, temp
        return left_type, left_value
    
    def visit_expresion_aditiva_prime(self, node):
        if node.children:
            left_type, left_value = self.visit(node.children[1])
            operator = node.children[0].children[0].name
            _, right_value = self.visit(node.children[2])
            if left_value and right_value:
                temp = self.new_temp()
                self.intermediate_code.append(f"{temp} = {left_value} {operator} {right_value}")
                return left_type, temp
            return left_type, left_value
        return None, None
    
    def visit_expresion_multiplicativa_prime(self, node):
        if node.children:
            left_type, left_value = self.visit(node.children[1])
            operator = node.children[0].children[0].name
            _, right_value = self.visit(node.children[2])
            if left_value and right_value:
                temp = self.new_temp()
                self.intermediate_code.append(f"{temp} = {left_value} {operator} {right_value}")
                return left_type, temp
            return left_type, left_value
        return None, None
    
    def visit_condicional(self, node):
        # Etiquetas para manejar el flujo condicional
        etiqueta_else = self.new_label()  # Para el bloque "else if" o "else"
        etiqueta_fin = self.new_label()  # Para el final del condicional

        # Evaluamos la condición del if (ari)
        condicion_temp = self.visit_expresion_condicion(node.children[2])

        # Código para el salto condicional
        self.intermediate_code.append(f"IF NOT {condicion_temp} GOTO {etiqueta_else}")

        # Visitamos el bloque de sentencias dentro del "if"
        self.visit_lista_sentencias(node.children[7])

        # Salto al final del condicional
        self.intermediate_code.append(f"GOTO {etiqueta_fin}")

        # Etiqueta para el bloque else if o else
        self.intermediate_code.append(f"{etiqueta_else}:")

        # Visitamos el bloque "else if" o "else" si existen
        if node.children[10].children:
            self.visit_condicional_prime(node.children[10])

        # Etiqueta para el final del condicional
        self.intermediate_code.append(f"{etiqueta_fin}:")

    def visit_condicional_prime(self, node): #Visita todos los nodos de la condicional prime
        if node.children[0].name == "mana_chayqa_ari":
            # Etiqueta para el siguiente bloque else if o else
            etiqueta_else = self.new_label()

            # Evaluamos la nueva condición del else if (mana_chayqa_ari)
            condicion_temp = self.visit_expresion_condicion(node.children[2])

            # Código para el salto condicional
            self.intermediate_code.append(f"IF NOT {condicion_temp} GOTO {etiqueta_else}")

            # Visitamos el bloque de sentencias dentro del "else if"
            self.visit_lista_sentencias(node.children[7])

            # Salto al final del condicional
            etiqueta_fin = self.new_label()
            self.intermediate_code.append(f"GOTO {etiqueta_fin}")

            # Etiqueta para el bloque else if o else
            self.intermediate_code.append(f"{etiqueta_else}:")

            # Visitamos el próximo "else if" o "else" si existe
            if node.children[10].children:
                self.visit_condicional_prime(node.children[10])

            # Etiqueta final para saltar fuera del condicional
            self.intermediate_code.append(f"{etiqueta_fin}:")
        elif node.name == "mana_chayqa":
            # Si hay un bloque "else", visitamos sus sentencias
            self.visit_lista_sentencias(node.children[4])

    def visit_expresion_condicion(self, node):
        print("Visitando expresion condicion")
        left_value = self.visit(node.children[0])                                   # Visitamos la primera expresión relacional
        print(left_value)
        # Si hay operadores lógicos adicionales (AND, OR)
        right_value = self.visit_expresion_condicion_prime(node.children[1])        # Visitamos la siguiente expresión condicional si existe
        temp = self.new_temp()
        if right_value:
            self.intermediate_code.append(f"{temp} = {left_value} {right_value}")
            return temp
        else:
            self.intermediate_code.append(f"{temp} = {left_value}")
        return temp

    def visit_expresion_relacional(self, node):
        print("Visitando expresion relacional")
        _, left_value = self.visit(node.children[0])            # Visitamos el primer término
        operator = node.children[1].children[0].name            # Obtenemos el operador relacional
        _, right_value = self.visit(node.children[2])           # Visitamos el segundo término
        temp = f"{left_value} {operator} {right_value}"         # Concatenamos los valores para la expresión relacional
        return temp                                             # Retornamos el nombre del temporal a la funcion visit_expresion_condicion
    
    def visit_expresion_condicion_prime(self, node):
        if node.children:
            operator = node.children[0].children[0].name
            _, right_value = self.visit(node.children[1])
            print(node.children[1].name)
            print(operator, right_value)
        return None
        
    def visit_termino(self, node):
        child = node.children[0]
        if child.name == "ID":
            var_name = child.children[0].name
            var_type = self.symbol_table.get(var_name)
            var_value = self.symbol_table.get_value(var_name)
            return var_type, var_value
        elif child.name == "ENTERO":
            return "yupay", int(child.children[0].name)
        elif child.name == "FLOTANTE":
            return "chunkayuq", float(child.children[0].name)
        elif child.name == "TRUE":
            return "bool", child.children[0].name
        elif child.name == "FALSE":
            return "bool", child.children[0].name
        elif child.name == "CARACTER":
            return "sananpa", child.children[0].name
        elif child.name == "CADENA":
            return "qaytu", child.children[0].name
    
    def visit_tipo(self, node):
        return node.children[0].name, None

    def analyze(self, root):
        self.visit(root)
        return self.intermediate_code
    
    def save_intermediate_code(self, filename="intermediate_code.txt"):
        os.makedirs("outputs/intermediate", exist_ok=True)
        filepath = os.path.join("outputs/intermediate", filename)
        with open(filepath, "w") as file:
            for line in self.intermediate_code:
                file.write(line + "\n")

    def save_symbol_table(self, filename="symbol_table.txt"):
        os.makedirs("outputs/intermediate", exist_ok=True)
        filepath = os.path.join("outputs/intermediate", filename)
        with open(filepath, "w") as file:
            headers = ["Nombre", "Tipo", "Ámbito", "Valor"]
            rows = [[name, info["type"], info["scope"], info["value"]] for name, info in self.symbol_table.symbols.items()]
            file.write("Tabla de Símbolos:\n")
            file.write(tabulate(rows, headers, tablefmt="grid"))