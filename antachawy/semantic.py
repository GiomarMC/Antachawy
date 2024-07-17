from antachawy.symboltable import SymbolTable

class SemanticError:
    def __init__(self, message, line):
        self.message = message
        self.line = line

    def __repr__(self):
        return f"Error en línea {self.line}: {self.message}"

class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.errors = []
        self.current_scope = "global"

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
        return None

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
        tipo = self.visit(node.children[0])
        nombre = node.children[1].children[0].name
        try:
            self.symbol_table.add(nombre, tipo, self.current_scope)
        except Exception as e:
            self.errors.append(e)
        if len(node.children) > 2:
            self.visit(node.children[2])

    def visit_asignaciones(self, node):
        nombre = node.children[0].children[0].name
        expresion_tipo = self.visit(node.children[2])
        tipo = self.symbol_table.get(nombre)
        if tipo is None:
            self.errors.append(f"Error: Variable '{nombre}' no declarada.")
        
        if tipo != expresion_tipo:
            self.errors.append(f"Error de tipo: Variable '{nombre}' es de tipo '{tipo}' y la expresión es de tipo '{expresion_tipo}'.")

    def visit_expresion(self, node):
        return self.visit(node.children[0])

    def visit_expresion_multiplicativa(self, node):
        return self.visit(node.children[0])
    
    def visit_expresion_aditiva_prime(self, node):
        if node.children:
            left_type = self.visit(node.children[1])
            right_type = self.visit(node.children[2])
            if left_type != right_type:
                self.errors.append(f"Error de tipo: operación entre tipos '{left_type}' y '{right_type}' no permitida.")
            return left_type
    def visit_expresion_multiplicativa_prime(self, node):
        if node.children:
            left_type = self.visit(node.children[1])
            right_type = self.visit(node.children[2])
            if left_type != right_type:
                self.errors.append(f"Error de tipo: operación entre tipos '{left_type}' y '{right_type}' no permitida.")
            return left_type
        
    def visit_termino(self, node):
        child = node.children[0]
        if child.name == "ID":
            var_name = child.children[0].name
            var_type = self.symbol_table.get(var_name)
            if var_type is None:
                self.errors.append(f"Error: variable '{var_name}' no está definida.")
            return var_type
        elif child.name == "ENTERO":
            return "yupay"
        elif child.name == "FLOTANTE":
            return "chunkayuq"
        elif child.name == "TRUE" or child.name == "FALSE":
            return "bool"
        elif child.name == "CARACTER":
            return "sananpa"
        elif child.name == "CADENA":
            return "qaytu"
    
    def visit_tipo(self, node):
        return node.children[0].name

    def analyze(self, root):
        self.visit(root)
        if not self.errors:
            print("--> Semantic Analysis Passed")
        else:
            print("--> Semantic Analysis Failed")
        self.symbol_table.print_table()