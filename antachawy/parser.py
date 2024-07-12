from antachawy.definitions import LexemasAntachawy, EtiquetasAntachawy, primeros, segundos
from antachawy.scanner import Scanner

from anytree import Node, RenderTree
from anytree.exporter import UniqueDotExporter

def render_tree(root: object):
    for pre, fill, node in RenderTree(root):
        print("%s%s" % (pre, node.name))

class RecursiveDescentParser:
    def __init__(self, scanner: Scanner):
        self.scanner = scanner
        self.tokens = []
        self.current_token_idx = 0
        self.current_token = None
        self.root = None

    def parse(self):
        self.tokens = self.scanner.tokens
        self.current_token_idx = 0
        self.current_token = self.tokens[self.current_token_idx]
        self.root = self.programa()

        if self.current_token is not None:
            raise SyntaxError(f"Token inesperado '{self.current_token.lexema}' en la línea {self.current_token.linea}")
        
        return self.root
    
    def consume(self, expected_tag):
        if self.current_token is not None and self.current_token.etiqueta == expected_tag:
            self.current_token_idx += 1
            if self.current_token_idx < len(self.tokens):
                self.current_token = self.tokens[self.current_token_idx]
            else:
                self.current_token = None
        else:
            raise SyntaxError(f"Token inesperado '{self.current_token.lexema}' en la línea {self.current_token.linea} esperaba {expected_tag}")
        
    def programa(self):
        node = Node("Programa")
        node_definicion = self.definicion()
        node.children = [node_definicion]
        return node
    
    def definicion(self):
        node = Node("Definicion")
        self.consume(EtiquetasAntachawy.PROGRAMA)
        self.consume(EtiquetasAntachawy.PAREN_IZQ)
        self.consume(EtiquetasAntachawy.PAREN_DER)
        self.consume(EtiquetasAntachawy.SALTO_LINEA)
        self.consume(EtiquetasAntachawy.LLAVE_IZQ)
        self.consume(EtiquetasAntachawy.SALTO_LINEA)
        node_lista_sentencias = self.lista_sentencias()
        node.children = [node_lista_sentencias]
        self.consume(EtiquetasAntachawy.LLAVE_DER)
        return node
    
    def lista_sentencias(self):
        node = Node("ListaSentencias")
        if self.current_token.etiqueta in primeros["ListaSentencias"]:
            node_sentencia = self.sentencias()
            node_lista_sentencias = self.lista_sentencias()
            node.children = [node_sentencia, node_lista_sentencias]
        return node
    
    def sentencias(self):
        node = Node("Sentencias")
        if self.current_token.etiqueta in primeros["Declaraciones"]:
            node_declaraciones = self.declaraciones()
            node.children = [node_declaraciones]
        elif self.current_token.etiqueta in primeros["Asignaciones"]:
            node_asignaciones = self.asignaciones()
            node.children = [node_asignaciones]
        elif self.current_token.etiqueta in primeros["Impresiones"]:
            node_impresion = self.impresion()
            node.children = [node_impresion]
        else:
            raise SyntaxError(f"Token inesperado '{self.current_token.lexema}' en la línea {self.current_token.linea}")
        self.consume(EtiquetasAntachawy.SALTO_LINEA)
        return node
    
    def declaraciones(self):
        node = Node("Declaraciones")
        node_tipo = self.tipo()
        self.consume(EtiquetasAntachawy.ID)
        node_declaraciones_prime = self.declaraciones_prime()
        node.children = [node_tipo, Node(LexemasAntachawy.ID), node_declaraciones_prime]
        return node
    
    def declaraciones_prime(self):
        node = Node("DeclaracionesPrime")
        if self.current_token.etiqueta in primeros["DeclaracionesPrime"]:
            self.consume(EtiquetasAntachawy.ASIGNACION)
            node_expresion = self.expresion()
            node.children = [Node(LexemasAntachawy.ASIGNA), node_expresion]
        return node
    
    def asignaciones(self):
        node = Node("Asignaciones")
        self.consume(EtiquetasAntachawy.ID)
        self.consume(EtiquetasAntachawy.ASIGNACION)
        node_expresion = self.expresion()
        node.children = [Node(LexemasAntachawy.ID), Node(LexemasAntachawy.ASIGNA), node_expresion]
        return node
    
    def impresion(self):
        node = Node("Impresiones")
        self.consume(EtiquetasAntachawy.IMPRESION)
        self.consume(EtiquetasAntachawy.PAREN_IZQ)
        node_expresion_impresion = self.expresion_impresion()
        self.consume(EtiquetasAntachawy.PAREN_DER)
        node.children = [Node(LexemasAntachawy.SIQIY), Node(LexemasAntachawy.PAREN_IZQ), node_expresion_impresion, Node(LexemasAntachawy.PAREN_DER)]
        return node
    
    def tipo(self):
        node = Node("Tipo")
        if self.current_token.etiqueta in primeros["Tipo"]:
            node_tipo = Node(self.current_token.etiqueta)
            self.consume(self.current_token.etiqueta)
            node.children = [node_tipo]
        else:
            raise SyntaxError(f"Token inesperado '{self.current_token.lexema}' en la línea {self.current_token.linea}")
        return node
    
    def expresion(self):
        node = Node("Expresion")
        node_termino = self.termino()
        node_expresion_prime = self.expresion_prime()
        node.children = [node_termino, node_expresion_prime]
        return node
    
    def expresion_prime(self):
        node = Node("ExpresionPrime")
        if self.current_token.etiqueta in primeros["ExpresionPrime"]:
            node_operador = self.operador()
            node_termino = self.termino()
            node_expresion_prime = self.expresion_prime()
            node.children = [node_operador, node_termino, node_expresion_prime]
        return node
    
    def operador(self):
        node = Node("Operador")
        if self.current_token.etiqueta in primeros["Operador"]:
            node_operador = Node(self.current_token.etiqueta)
            self.consume(self.current_token.etiqueta)
            node.children = [node_operador]
        else:
            raise SyntaxError(f"Token inesperado '{self.current_token.lexema}' en la línea {self.current_token.linea}")
        return node
    
    def termino(self):
        node = Node("Termino")
        if self.current_token.etiqueta in primeros["Termino"]:
            if self.current_token.etiqueta == EtiquetasAntachawy.PAREN_IZQ:
                self.consume(EtiquetasAntachawy.PAREN_IZQ)
                node_expresion = self.expresion()
                self.consume(EtiquetasAntachawy.PAREN_DER)
                node.children = [Node(LexemasAntachawy.PAREN_IZQ), node_expresion, Node(LexemasAntachawy.PAREN_DER)]
            else:
                node_termino = Node(self.current_token.etiqueta)
                self.consume(self.current_token.etiqueta)
                node.children = [node_termino]
        else:
            raise SyntaxError(f"Token inesperado '{self.current_token.lexema}' en la línea {self.current_token.linea}")
        return node
    
    def expresion_impresion(self):
        node = Node("ExpresionImpresion")
        node_expresion = self.expresion()
        node_expresion_impresion_prime = self.expresion_impresion_prime()
        node.children = [node_expresion, node_expresion_impresion_prime]
        return node
    
    def expresion_impresion_prime(self):
        node = Node("ExpresionImpresionPrime")
        if self.current_token.etiqueta in primeros["ExpresionImpresionPrime"]:
            self.consume(self.current_token.etiqueta)
            node_expresion_impresion = self.expresion_impresion()
            node.children = [Node(LexemasAntachawy.COMA), node_expresion_impresion]
        return node