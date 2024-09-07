from antachawy.symboltable import SymbolTable
from antachawy.shared import print_table
from antachawy.sourcecode import SourceCode
from tabulate import tabulate
import os

class SemanticAnalyzer:
    def __init__(self, source_code: SourceCode):
        self.symbol_table = SymbolTable()
        self.errors = []
        self.current_scope = "global"
        self.print_table = print_table
        self.source_code = source_code

    def get_current_line_content(self, line):
        return self.source_code.get_line(line)

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
        elif node.name == "OperadorMultiplicativo":
            return node.children[0].name
        elif node.name == "OperadorAditivo":
            return node.children[0].name
        elif node.name == "Impresiones":
            self.visit_impresiones(node)
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
        tipo, _ = self.visit(node.children[0])          #Se va a la función visit_tipo
        nombre = node.children[1].children[0].name      #Se obtiene el nombre de la variable
        _, valor = self.visit(node.children[2])         #Se va a la función visit_declaraciones_prime
        try:
            self.symbol_table.add(nombre, tipo, self.current_scope, valor)
        except Exception as e:
            self.errors.append(str(e))

    def visit_declaraciones_prime(self, node):
        if len(node.children) > 1:
            return self.visit(node.children[1])         #Se va a la funcion visit_Expresion
        return None, None

    def visit_asignaciones(self, node):
        nombre = node.children[0].children[0].name
        line = node.children[0].children[0].children[0].name
        expresion_tipo, valor = self.visit(node.children[2])        #Se va a la funcion visit_expresion
        tipo = self.symbol_table.get(nombre)
        if tipo is None:
            self.errors.append({
                "mensaje": f"Error: Variable '{nombre}' no declarada.",
                "linea": line,
                "contenido": self.get_current_line_content(line)})
        if tipo != expresion_tipo:
            self.errors.append({
                "mensaje": f"Error de tipo: Variable '{nombre}' es de tipo '{tipo}' y la expresión es de tipo '{expresion_tipo}'.",
                "linea": line,
                "contenido": self.get_current_line_content(line)})
        else:
            self.symbol_table.set_value(nombre, valor)

    def visit_expresion(self, node):
        left_type, left_value = self.visit(node.children[0])        #Se va a la funcion visit_expresion_multiplicativa
        if node.children[1].children:
            operator = node.children[1].children[0].children[0].name
            line = node.children[1].children[0].children[0].children[0].name
            right_type, right_value = self.visit(node.children[1])  #Se va a la funcion visit_expresion_aditiva_prime
            if left_value and right_value:
                if left_type != right_type:
                    self.errors.append({
                        "mensaje": f"Error de tipo: operación entre tipos '{left_type}' y '{right_type}' no permitida.",
                        "linea": line,
                        "contenido": self.get_current_line_content(line)})
                valor = f"{left_value} {operator} {right_value}"
                return left_type, valor
        return left_type, left_value

    def visit_expresion_multiplicativa(self, node):
        left_type, left_value, left_line = self.visit(node.children[0])     #Se va a la funcion visit_termino
        if node.children[1].children:
            operator = node.children[1].children[0].children[0].name
            right_type, right_value = self.visit(node.children[1])          #Se va a la funcion visit_expresion_multiplicativa_prime
            if left_value and right_value:
                if left_type != right_type:
                    self.errors.append({
                        "mensaje": f"Error de tipo: operación entre tipos '{left_type}' y '{right_type}' no permitida.",
                        "linea": left_line,
                        "contenido": self.get_current_line_content(left_line)})
                valor = f"{left_value} {operator} {right_value}"
                return left_type, valor
        return left_type, left_value
    
    def visit_expresion_aditiva_prime(self, node):
        if node.children:
            left_type, left_value = self.visit(node.children[1])            #Se va a la funcion visit_expresion_multiplicativa
            operator = node.children[0].children[0].name
            line = node.children[0].children[0].children[0].name
            right_type, right_value = self.visit(node.children[2])          #Se va a la funcion visit_expresion_aditiva_prime
            if left_value and right_value:
                if left_type != right_type:
                    self.errors.append({
                        "mensaje": f"Error de tipo: operación entre tipos '{left_type}' y '{right_type}' no permitida.",
                        "linea": line,
                        "contenido": self.get_current_line_content(line)})
                valor = f"{left_value} {operator} {right_value}"
                return left_type, valor
            elif left_value and not right_value:
                valor = f"{operator} {left_value}"
                return left_type, valor
            return left_type, left_value
        return None, None
    
    def visit_expresion_multiplicativa_prime(self, node):
        if node.children:
            left_type, left_value, left_line = self.visit(node.children[1])   #Se va a la funcion visit_termino
            if node.children[2].children:
                operator = self.visit(node.children[2].children[0])                          #Se obtiene el operador
            right_type, right_value = self.visit(node.children[2])         #Se va a la funcion visit_expresion_multiplicativa_prime
            if left_value and right_value:
                if left_type != right_type:
                    self.errors.append({
                        "mensaje": f"Error de tipo: operación entre tipos '{left_type}' y '{right_type}' no permitida.",
                        "linea": left_line,
                        "contenido": self.get_current_line_content(left_line)})
                valor = f"{left_value} {operator} {right_value}"
                return left_type, valor
            return left_type, left_value
        return None, None
        
    def visit_termino(self, node):
        child = node.children[0]
        if child.name == "ID":
            var_name = child.children[0].name
            var_type = self.symbol_table.get(var_name)
            var_value = self.symbol_table.get_value(var_name)
            var_line = child.children[0].children[0].name
            if var_type is None:
                self.errors.append({
                    "mensaje": f"Error: variable '{var_name}' no está definida.",
                    "linea": var_line,
                    "contenido": self.get_current_line_content(var_line)})
            return var_type, var_value, var_line
        elif child.name == "ENTERO":
            return "yupay", int(child.children[0].name), child.children[0].children[0].name
        elif child.name == "FLOTANTE":
            return "chunkayuq", float(child.children[0].name), child.children[0].children[0].name
        elif child.name == "TRUE":
            return "bool", child.children[0].name, child.children[0].children[0].name
        elif child.name == "FALSE":
            return "bool", child.children[0].name, child.children[0].children[0].name
        elif child.name == "CARACTER":
            return "sananpa", child.children[0].name, child.children[0].children[0].name
        elif child.name == "CADENA":
            return "qaytu", child.children[0].name, child.children[0].children[0].name
    
    def visit_tipo(self, node):
        return node.children[0].name, None
    
    def visit_impresiones(self, node):
        self.print_table.add_table()
        table_index = len(self.print_table.tables) - 1
        expresion_impresion = node.children[2]
        valores = self.visit_expresion_impresion(expresion_impresion)
        for valor, tipo in valores:
            self.print_table.add_entry(table_index, valor, tipo)

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
    
    def get_print_table(self):
        return self.print_table

    def analyze(self, root):
        self.visit(root)

    def save_symbol_table(self, filename="symbol_table.txt"):
        os.makedirs("outputs/semantic", exist_ok=True)
        filepath = os.path.join("outputs/semantic", filename)
        with open(filepath, "w") as file:
            headers = ["Nombre", "Tipo", "Ámbito", "Valor"]
            rows = [[name, info["type"], info["scope"], info["value"]] for name, info in self.symbol_table.symbols.items()]
            file.write("Tabla de Símbolos:\n")
            file.write(tabulate(rows, headers, tablefmt="grid"))

    def save_print_table(self, filename="print_table.txt"):
        os.makedirs("outputs/semantic", exist_ok=True)
        filepath = os.path.join("outputs/semantic", filename)
        with open(filepath, "w") as file:
            for i, table in enumerate(self.print_table.tables):
                file.write(f"\nSentencia de Impresión {i + 1}:\n")
                headers = ["siqiy", "Tipo"]
                rows = [(entry_value, entry_type) for entry_value, entry_type in table]
                file.write(tabulate(rows, headers, tablefmt="grid"))