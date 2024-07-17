from anytree import Node

class IntermediateCodeGenerator:
    def __init__(self):
        self.instructions = []
        self.temp_counter = 0

    def new_temp(self):
        temp = f"t{self.temp_counter}"
        self.temp_counter += 1
        return temp

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
        return None

    def visit_programa(self, node):
        for child in node.children:
            self.visit(child)

    def visit_definicion(self, node):
        for child in node.children:
            self.visit(child)

    def visit_lista_sentencias(self, node):
        for child in node.children:
            self.visit(child)

    def visit_sentencias(self, node):
        for child in node.children:
            self.visit(child)

    def visit_declaraciones(self, node):
        if len(node.children) > 2:
            result = self.visit(node.children[2])
            var_name = node.children[1].children[0].name
            self.instructions.append(f"{var_name} = {result}")

    def visit_asignaciones(self, node):
        result = self.visit(node.children[2])
        var_name = node.children[0].children[0].name
        self.instructions.append(f"{var_name} = {result}")

    def visit_expresion(self, node):
        return self.visit(node.children[0])

    def visit_expresion_multiplicativa(self, node):
        result = self.visit(node.children[0])
        return result
    
    def visit_expresion_aditiva_prime(self, node):
        if node.children:
            left = self.visit(node.children[1])
            right = self.visit(node.children[2])
            temp = self.new_temp()
            operator = node.children[0].children[0].name
            self.instructions.append(f"{temp} = {left} {operator} {right}")
            return temp
        return None

    def visit_expresion_multiplicativa_prime(self, node):
        if node.children:
            left = self.visit(node.children[1])
            right = self.visit(node.children[2])
            temp = self.new_temp()
            operator = node.children[0].children[0].name
            self.instructions.append(f"{temp} = {left} {operator} {right}")
            return temp
        return None

    def visit_termino(self, node):
        child = node.children[0]
        if child.name == "ID":
            return child.children[0].name
        elif child.name == "ENTERO":
            return child.children[0].name

    def generate(self, root):
        self.visit(root)
        return self.instructions