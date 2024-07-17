from anytree import Node

class IntermediateCodeGenerator:
    def __init__(self):
        self.temp_counter = 0
        self.code = []

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
        elif node.name == "Impresiones":
            self.visit_impresiones(node)
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
        for child in node.children:
            self.visit(child)

    def visit_lista_sentencias(self, node):
        for child in node.children:
            self.visit(child)

    def visit_sentencias(self, node):
        for child in node.children:
            self.visit(child)

    def visit_declaraciones(self, node):
        pass

    def visit_asignaciones(self, node):
        var_name = node.children[0].children[0].name
        expre_code = self.visit(node.children[2])
        self.code.append(f"{var_name} = {expre_code}")

    def visit_impresiones(self, node):
        expre_code = self.visit(node.children[1])
        self.code.append(f"print {expre_code}")

    def visit_expresion(self, node):
        left = self.visit(node.children[0])
        if len(node.children) > 1:
            op = node.children[1].children[0].name
            right = self.visit(node.children[2])
            temp = self.new_temp()
            self.code.append(f"{temp} = {left} {op} {right}")
            return temp
        return left
    
    def visit_expresion_multiplicativa(self, node):
        left = self.visit(node.children[0])
        if len(node.children) > 1:
            op = node.children[0].name
            right = self.visit(node.children[2])
            temp = self.new_temp()
            self.code.append(f"{temp} = {left} {op} {right}")
            return temp
        return left
    
    def visit_expresion_aditiva_prime(self, node):
        if node.children:
            left = self.visit(node.children[1])
            return left
        
    def visit_expresion_multiplicativa_prime(self, node):
        if node.children:
            left = self.visit(node.children[1])
            return left
        
    def visit_termino(self, node):
        child = node.children[0]
        if child.name in ["ID", "ENTERO", "FLOTANTE", "CARACTER", "CADENA"]:
            return child.children[0].name
        return None
    
    def visit_tipo(self, node):
        return node.children[0].name
    
    def generate_code(self, root):
        self.visit(root)
        return self.code