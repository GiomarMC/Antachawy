from antachawy.definitions import LexemasAntachawy, EtiquetasAntachawy, primeros
from antachawy.scanner import Scanner
from anytree import Node, RenderTree
from anytree.exporter import UniqueDotExporter
from tabulate import tabulate
import os

def render_tree(root: object, filename: str):
    tree_str = ""
    for pre, fill, node in RenderTree(root):
        tree_str += "%s%s\n" % (pre, node.name)
    with open(filename, "w") as file:
        file.write(tree_str)

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
            self.errors.append({
                "mensaje": f"Token inesperado '{self.current_token.lexema}'",
                "linea": self.current_token.linea,
                "contenido": self.current_token.lexema
            })
        
        return self.root
    
    def next_token(self):
        self.current_token_idx += 1
        if self.current_token_idx < len(self.tokens):
            self.current_token = self.tokens[self.current_token_idx]
        else:
            self.current_token = None

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
            self.next_token()
            if self.current_token is None:
                return
        else:
            if self.current_token is not None:
                mensaje = f"Token inesperado '{self.current_token.etiqueta}' se esperaba '{expected_tag}'"
                self.panic_mode(mensaje,EtiquetasAntachawy.SALTO_LINEA, parent=parent)
            else:
                mensaje = f"Se esperaba '{expected_tag}' al final del archivo"
                self.panic_mode(mensaje, None, parent=parent)
        
    def panic_mode(self, mensaje, *expected_tags, parent: Node):
        Node('ERROR', parent=parent)

        if mensaje and self.current_token is not None:
            self.errors.append({
                "mensaje": mensaje,
                "linea": self.current_token.linea,
                "contenido": self.current_token.lexema
            })

        if not expected_tags:
            self.errors.append({
                "mensaje": mensaje,
                "linea": self.tokens[-1].linea,
                "contenido": self.tokens[-1].lexema
            })
            return
        
        while self.current_token is not None and self.current_token.etiqueta not in expected_tags:
            self.next_token()
    
    def programa(self):
        node = Node("Programa")
        node_definicion = self.definicion()
        node.children = [node_definicion]
        return node
    
    def definicion(self):
        node = Node("Definicion")
        self.consume(EtiquetasAntachawy.PROGRAMA,node)
        self.consume(EtiquetasAntachawy.PAREN_IZQ,node)
        self.consume(EtiquetasAntachawy.PAREN_DER,node)
        self.consume(EtiquetasAntachawy.SALTO_LINEA,node)
        self.consume(EtiquetasAntachawy.LLAVE_IZQ,node)
        self.consume(EtiquetasAntachawy.SALTO_LINEA,node)
        node_lista_sentencias = self.lista_sentencias()
        node_lista_sentencias.parent = node
        self.consume(EtiquetasAntachawy.LLAVE_DER,node)
        return node
    
    def lista_sentencias(self):
        node = Node("ListaSentencias")
        if self.current_token is None:
            return node
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
        node_tipo = Node(self.current_token.etiqueta)
        Node(self.current_token.lexema, parent=node_tipo)
        self.consume(self.current_token.etiqueta, node)
        return node
    
    def expresion(self):
        node = Node("Expresion")
        node_expresion_multiplicativa = self.expresion_multiplicativa()
        node_expresion_multiplicativa.parent = node
        node_expresion_aditiva_prime = self.expresion_aditiva_prime()
        node_expresion_aditiva_prime.parent = node
        return node
    
    def expresion_aditiva_prime(self):
        node = Node("ExpresionAditivaPrime")
        if self.current_token.etiqueta in primeros["OperadorAditivo"]:
            node_operador_aditivo = self.operador_aditivo()
            node_operador_aditivo.parent = node
            node_expresion_multiplicativa = self.expresion_multiplicativa()
            node_expresion_multiplicativa.parent = node
            node_expresion_aditiva_prime = self.expresion_aditiva_prime()
            node_expresion_aditiva_prime.parent = node
        return node
    
    def expresion_multiplicativa(self):
        node = Node("ExpresionMultiplicativa")
        node_termino = self.termino()
        node_termino.parent = node
        node_expresion_multiplicativa_prime = self.expresion_multiplicativa_prime()
        node_expresion_multiplicativa_prime.parent = node
        return node
    
    def expresion_multiplicativa_prime(self):
        node = Node("ExpresionMultiplicativaPrime")
        if self.current_token.etiqueta in primeros["OperadorMultiplicativo"]:
            node_operador_multiplicativo = self.operador_multiplicativo()
            node_operador_multiplicativo.parent = node
            node_termino = self.termino()
            node_termino.parent = node
            node_expresion_multiplicativa_prime = self.expresion_multiplicativa_prime()
            node_expresion_multiplicativa_prime.parent = node
        return node
    
    def operador_aditivo(self):
        node = Node("OperadorAditivo")
        node_aditivo = Node(self.current_token.etiqueta)
        Node(self.current_token.lexema, parent=node_aditivo)
        self.consume(self.current_token.etiqueta, node)
        return node
    
    def operador_multiplicativo(self):
        node = Node("OperadorMultiplicativo")
        node_multiplicativo = Node(self.current_token.etiqueta)
        Node(self.current_token.lexema, parent=node_multiplicativo)
        self.consume(self.current_token.etiqueta, node)
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
            mensaje = f"Token inesperado '{self.current_token.etiqueta}'"
            self.panic_mode(mensaje, EtiquetasAntachawy.SALTO_LINEA, parent=node)
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
        if self.current_token is None:
            return node
        if self.current_token.etiqueta in primeros["ExpresionImpresionPrime"]:
            self.consume(EtiquetasAntachawy.COMA, node)
            node_expresion_impresion = self.expresion_impresion()
            node_expresion_impresion.parent = node
        return node
    
    def save_syntax_outputs(self, root: object, base_filename: str):
        os.makedirs("outputs/sintactic", exist_ok=True)
        render_tree(root, base_filename + ".txt")
        export_tree(root, base_filename)