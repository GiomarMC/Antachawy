from antachawy.definitions import LexemasAntachawy, EtiquetasAntachawy, primeros
from antachawy.scanner import Scanner

from anytree import Node, RenderTree
from anytree.exporter import UniqueDotExporter

def render_tree(root: object):
    for pre, fill, node in RenderTree(root):
        print("%s%s" % (pre, node.name))

def export_tree(root: object, filename: str):
    UniqueDotExporter(root).to_dotfile(filename + ".dot")
    UniqueDotExporter(root).to_picture(filename + ".png")

class RecursiveDescentParser:
    def __init__(self, scanner: Scanner):
        self.scanner = scanner
        self.tokens = []
        self.current_token_idx = 0
        self.current_token = None
        self.root = None
        self.errors = []

    def parse(self):
        self.tokens = self.scanner.tokens
        self.current_token_idx = 0
        self.current_token = self.tokens[self.current_token_idx]
        self.root = self.programa()

        if self.current_token is not None:
            raise SyntaxError(f"Token inesperado '{self.current_token.lexema}' en la línea {self.current_token.linea}")
        
        if not self.errors:
            render_tree(self.root)
            print("-->Accepted Program")
            export_tree(self.root,"AbstracSyntaxTree")
        else:
            print("-->Rejected Program")
            for error in self.errors:
                print(f"Error en la línea {error['linea']}: {error['mensaje']}")    
        return self.root
    
    def consume(self, expected_tag, parent: Node):
        if self.current_token is not None and self.current_token.etiqueta == expected_tag:
            if self.current_token.etiqueta == EtiquetasAntachawy.SALTO_LINEA:
                Node('\\n', parent=parent)
            elif self.current_token.etiqueta == EtiquetasAntachawy.CARACTER:
                Node(self.current_token.lexema[1:-1], parent=parent)
            elif self.current_token.etiqueta == EtiquetasAntachawy.CADENA:
                Node(self.current_token.lexema[1:-1], parent=parent)
            else:
                Node(self.current_token.lexema, parent=parent)
            self.current_token_idx += 1
            if self.current_token_idx < len(self.tokens):
                self.current_token = self.tokens[self.current_token_idx]
            else:
                self.current_token = None
        else:
            self.errors.append({
                "mensaje": f"Token inesperado '{self.current_token.lexema}'",
                "linea": self.current_token.linea
            })
            self.panic_mode(expected_tag)
        
    def panic_mode(self, *expected_tags):
        print(f"Entrando en modo pánico. Tokens esperados: {expected_tags}. Token actual: {self.current_token.etiqueta if self.current_token else 'None'} en la línea {self.current_token.linea if self.current_token else 'N/A'}")
        while self.current_token is not None and self.current_token.etiqueta not in expected_tags:
            self.current_token_idx += 1
            if self.current_token_idx < len(self.tokens):
                self.current_token = self.tokens[self.current_token_idx]
            else:
                self.current_token = None
        
        if self.current_token is None:
            print("No se encontraron tokens esperados. Finalizando análisis sintáctico.")
        else:
            print(f"Token encontrado: {self.current_token.etiqueta} en la línea {self.current_token.linea}")
    
    def programa(self):
        node = Node("Programa")
        node_definicion = self.definicion()
        node.children = [node_definicion]
        return node
    
    def definicion(self):
        try:
            node = Node("Definicion")
            self.consume(EtiquetasAntachawy.PROGRAMA, node)
            self.consume(EtiquetasAntachawy.PAREN_IZQ, node)
            self.consume(EtiquetasAntachawy.PAREN_DER, node)
            self.consume(EtiquetasAntachawy.SALTO_LINEA, node)
            self.consume(EtiquetasAntachawy.LLAVE_IZQ, node)
            self.consume(EtiquetasAntachawy.SALTO_LINEA, node)
            node_lista_sentencias = self.lista_sentencias()
            node_lista_sentencias.parent = node
            self.consume(EtiquetasAntachawy.LLAVE_DER, node)
        except SyntaxError:
            self.errors.append({
                "mensaje": "Error en la definición del programa",
                "linea": self.current_token.linea
            })
            error_node = Node("Error")
            error_node.children = [error_node]
            self.panic_mode(EtiquetasAntachawy.SALTO_LINEA, EtiquetasAntachawy.LLAVE_DER)
        return node
    
    def lista_sentencias(self):
        node = Node("ListaSentencias")
        if self.current_token.etiqueta in primeros["ListaSentencias"]:
            node_sentencia = self.sentencias()
            node_sentencia.parent = node
            node_lista_sentencias = self.lista_sentencias()
            node_lista_sentencias.parent = node
        return node
    
    def sentencias(self):
        node = Node("Sentencias")
        if self.current_token.etiqueta in primeros["Declaraciones"]:
            node_declaraciones = self.declaraciones()
            node_declaraciones.parent = node
        elif self.current_token.etiqueta in primeros["Asignaciones"]:
            node_asignaciones = self.asignaciones()
            node_asignaciones.parent = node
        elif self.current_token.etiqueta in primeros["Impresiones"]:
            node_impresion = self.impresion()
            node_impresion.parent = node
        else:
            self.errors.append({
                "mensaje": f"Token inesperado '{self.current_token.lexema}'",
                "linea": self.current_token.linea
            })
            self.panic_mode(EtiquetasAntachawy.SALTO_LINEA)
            error_node = Node("Error")
            error_node.children = [error_node]
        self.consume(EtiquetasAntachawy.SALTO_LINEA, node)
        return node
    
    def declaraciones(self):
        node = Node("Declaraciones")
        node_tipo = self.tipo()
        node_tipo.parent = node
        node_id = Node(self.current_token.etiqueta)
        node_id.parent = node
        self.consume(EtiquetasAntachawy.ID, node_id)
        node_declaraciones_prime = self.declaraciones_prime()
        node_declaraciones_prime.parent = node
        return node
    
    def declaraciones_prime(self):
        node = Node("DeclaracionesPrime")
        if self.current_token.etiqueta in primeros["DeclaracionesPrime"]:
            node_asignacion = Node(self.current_token.etiqueta)
            node_asignacion.parent = node
            self.consume(EtiquetasAntachawy.ASIGNACION, node_asignacion)
            node_expresion = self.expresion()
            node_expresion.parent = node
        return node
    
    def asignaciones(self):
        node = Node("Asignaciones")
        node_id = Node(self.current_token.etiqueta, parent=node)
        self.consume(EtiquetasAntachawy.ID, node_id)
        node_asignacion = Node(self.current_token.etiqueta, parent=node)
        self.consume(EtiquetasAntachawy.ASIGNACION, node_asignacion)
        node_expresion = self.expresion()
        node_expresion.parent = node
        return node
    
    def impresion(self):
        node = Node("Impresiones")
        self.consume(EtiquetasAntachawy.IMPRESION, node)
        self.consume(EtiquetasAntachawy.PAREN_IZQ, node)
        node_expresion_impresion = self.expresion_impresion()
        node_expresion_impresion.parent = node
        self.consume(EtiquetasAntachawy.PAREN_DER, node)
        return node
    
    def tipo(self):
        node = Node("Tipo")
        if self.current_token.etiqueta in primeros["Tipo"]:
            node_tipo = Node(self.current_token.etiqueta)
            Node(self.current_token.lexema, parent=node_tipo)
            self.consume(self.current_token.etiqueta, node)
        else:
            self.errors.append({
                "mensaje": f"Token inesperado '{self.current_token.lexema}'",
                "linea": self.current_token.linea
            })
            self.panic_mode(EtiquetasAntachawy.ID)
            error_node = Node("Error")
            error_node.children = [error_node]
        return node
    
    def expresion(self):
        node = Node("Expresion")
        node_termino = self.termino()
        node_termino.parent = node
        node_expresion_prime = self.expresion_prime()
        node_expresion_prime.parent = node
        return node
    
    def expresion_prime(self):
        node = Node("ExpresionPrime")
        if self.current_token.etiqueta in primeros["ExpresionPrime"]:
            node_operador = self.operador()
            node_operador.parent = node
            node_termino = self.termino()
            node_termino.parent = node
            node_expresion_prime = self.expresion_prime()
            node_expresion_prime.parent = node
        return node
    
    def operador(self):
        node = Node("Operador")
        if self.current_token.etiqueta in primeros["Operador"]:
            node_operador = Node(self.current_token.etiqueta)
            Node(self.current_token.lexema, parent=node_operador)
            self.consume(self.current_token.etiqueta, node)
        else:
            self.errors.append({
                "mensaje": f"Token inesperado '{self.current_token.lexema}'",
                "linea": self.current_token.linea
            })
            self.panic_mode(EtiquetasAntachawy.SALTO_LINEA)
            error_node = Node("Error")
            error_node.children = [error_node]
        return node
    
    def termino(self):
        node = Node("Termino")
        if self.current_token.etiqueta in primeros["Termino"]:
            if self.current_token.etiqueta == EtiquetasAntachawy.PAREN_IZQ:
                self.consume(EtiquetasAntachawy.PAREN_IZQ, node)
                node_expresion = self.expresion()
                node_expresion.parent = node
                self.consume(EtiquetasAntachawy.PAREN_DER, node)
            else:
                node_termino = Node(self.current_token.etiqueta)
                node_termino.parent = node
                self.consume(self.current_token.etiqueta, node_termino)

        else:
            self.errors.append({
                "mensaje": f"Token inesperado '{self.current_token.lexema}'",
                "linea": self.current_token.linea
            })
            self.panic_mode(EtiquetasAntachawy.SALTO_LINEA)
            error_node = Node("Error")
            error_node.children = [error_node]
        return node
    
    def expresion_impresion(self):
        node = Node("ExpresionImpresion")
        node_expresion = self.expresion()
        node_expresion.parent = node
        node_expresion_impresion_prime = self.expresion_impresion_prime()
        node_expresion_impresion_prime.parent = node
        return node
    
    def expresion_impresion_prime(self):
        node = Node("ExpresionImpresionPrime")
        if self.current_token.etiqueta in primeros["ExpresionImpresionPrime"]:
            self.consume(EtiquetasAntachawy.COMA, node)
            node_expresion_impresion = self.expresion_impresion()
            node_expresion_impresion.parent = node
        return node