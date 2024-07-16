from antachawy.symboltable import SymbolTable
from antachawy.definitions import EtiquetasAntachawy
from anytree import Node

class SemanticError:
    def __init__(self, message, line):
        self.message = message
        self.line = line

    def __repr__(self):
        return f"Error en línea {self.line}: {self.message}"

class SemanticAnalyzer:
    def __init__(self, root: Node):
        self.root = root
        self.symbol_table = SymbolTable()
        self.errors = []

    def analyze(self):
        self.visit(self.root)
        return self.errors

    def visit(self, node: Node):
        method_name = f"visit_{node.name.lower()}"
        visitor = getattr(self, method_name, self.generic_visit)
        visitor(node)

    def generic_visit(self, node: Node):
        for child in node.children:
            self.visit(child)

    def visit_definicion(self, node: Node):
        self.visit(node.children[0])  # Visitamos ListaSentencias

    def visit_lista_sentencias(self, node: Node):
        for child in node.children:
            self.visit(child)

    def visit_sentencias(self, node: Node):
        if node.children[0].name == "Declaraciones":
            self.visit(node.children[0])
        elif node.children[0].name == "Asignaciones":
            self.visit(node.children[0])
        elif node.children[0].name == "Impresiones":
            self.visit(node.children[0])

    def visit_declaraciones(self, node):
        tipo_node = node.children[0]  # Tipo
        id_node = node.children[1]    # ID
        if tipo_node and id_node:
            tipo = tipo_node.name
            var_name = id_node.name
            print(f"Agregando variable '{var_name}' de tipo '{tipo}' a la tabla de símbolos.")
            try:
                self.symbol_table.add(var_name, tipo)
            except ValueError as e:
                self.errors.append(str(e))

    def visit_declaracionesprime(self, node: Node):
        if node.children:
            self.visit(node.children[0])  # ASIGNACION
            self.visit(node.children[1])  # Expresion

    def visit_asignaciones(self, node: Node):
        id_name = node.children[0].name
        if self.symbol_table.get(id_name) is None:
            self.errors.append(SemanticError(f"Variable '{id_name}' no definida.", node.line))
        self.visit(node.children[2])  # Expresion

    def visit_impresiones(self, node: Node):
        self.visit(node.children[1])  # ExpresionImpresion

    def visit_expresion(self, node: Node):
        self.visit(node.children[0])  # ExpresionMultiplicativa
        self.visit(node.children[1])  # ExpresionAditivaPrime

    def visit_expresionaditiva_prime(self, node: Node):
        if node.children:
            self.visit(node.children[0])  # OperadorAditivo
            self.visit(node.children[1])  # ExpresionMultiplicativa
            self.visit(node.children[2])  # ExpresionAditivaPrime

    def visit_expresionmultiplicativa(self, node: Node):
        self.visit(node.children[0])  # Termino
        self.visit(node.children[1])  # ExpresionMultiplicativaPrime

    def visit_expresionmultiplicativa_prime(self, node: Node):
        if node.children:
            self.visit(node.children[0])  # OperadorMultiplicativo
            self.visit(node.children[1])  # Termino
            self.visit(node.children[2])  # ExpresionMultiplicativaPrime

    def visit_termino(self, node: Node):
        if node.children[0].name == "Expresion":
            self.visit(node.children[0])  # Expresion
        # En caso de ID o ENTERO se puede verificar aquí si es válido según el contexto

    def visit_expresionimpresion(self, node: Node):
        self.visit(node.children[0])  # Expresion
        self.visit(node.children[1])  # ExpresionImpresionPrime

    def visit_expresionimpresionprime(self, node: Node):
        if node.children:
            self.visit(node.children[0])  # COMA
            self.visit(node.children[1])  # ExpresionImpresion