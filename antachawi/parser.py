from antachawi.definitions import LexemasAntachawy, EtiquetasAntachawy, primeros
from antachawi.scanner import Scanner
from antachawi.sourcecode import SourceCode
from anytree import Node, RenderTree
from anytree.exporter import UniqueDotExporter
from tabulate import tabulate
import os

SALTO_DE_LINEA = 'salto de línea'

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
    def __init__(self, scanner: Scanner, source_code: SourceCode):
        self.scanner = scanner
        self.tokens = []
        self.current_token_idx = 0
        self.current_token = None
        self.root = None
        self.errors = []
        self.source_code = source_code

    def get_current_line_content(self, line):
        return self.source_code.get_line(line)
    
    def parse(self):
        self.tokens = self.scanner.tokens
        self.current_token_idx = 0
        self.current_token = self.tokens[self.current_token_idx]
        self.root = self.programa()

        if self.current_token is not None:
            self.errors.append({
                "mensaje": f"Error: '{self.current_token.lexema}'",
                "linea": self.current_token.linea,
                "contenido": self.get_current_line_content(self.current_token.linea)
            })
        
        return self.root

    def next_token(self):
        self.current_token_idx += 1
        if self.current_token_idx < len(self.tokens):
            self.current_token = self.tokens[self.current_token_idx]
        else:
            self.current_token = None

    def consume(self, expected_tag, lexema, parent: Node):
        if self.current_token is not None and self.current_token.etiqueta == expected_tag:
            if self.current_token.etiqueta == EtiquetasAntachawy.SALTO_LINEA:
                token_node = Node('\\n', parent=parent)
            elif self.current_token.etiqueta == EtiquetasAntachawy.CARACTER:
                token_node = Node(self.current_token.lexema[1:-1], parent=parent)
            elif self.current_token.etiqueta == EtiquetasAntachawy.CADENA:
                token_node = Node(self.current_token.lexema[1:-1], parent=parent)
            else:
                token_node = Node(self.current_token.lexema, parent=parent)

            Node(self.current_token.linea, parent=token_node)
            self.next_token()
            if self.current_token is None:
                return
        else:
            if self.current_token is not None:
                token = SALTO_DE_LINEA if self.current_token.lexema == '\n' else self.current_token.lexema
                lexema = SALTO_DE_LINEA if lexema == '\n' else lexema
                mensaje = f"Error inesperado '{token}' se esperaba '{lexema}'"
                self.panic_mode(mensaje,EtiquetasAntachawy.SALTO_LINEA, parent=parent)
            else:
                mensaje = f"Se esperaba '{lexema}' al final del archivo"
                self.panic_mode(mensaje, None, parent=parent)
        
    def panic_mode(self, mensaje, *expected_tags, parent: Node):
        Node('ERROR', parent=parent)

        if mensaje and self.current_token is not None:
            self.errors.append({
                "mensaje": mensaje,
                "linea": self.current_token.linea,
                "contenido": self.get_current_line_content(self.current_token.linea)
            })

        if not expected_tags:
            self.errors.append({
                "mensaje": mensaje,
                "linea": self.tokens[-1].linea,
                "contenido": self.get_current_line_content(self.tokens[-1].linea)
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
        self.consume(EtiquetasAntachawy.PROGRAMA,LexemasAntachawy.QHAPAQ,node)
        self.consume(EtiquetasAntachawy.PAREN_IZQ,LexemasAntachawy.PAREN_IZQ,node)
        self.consume(EtiquetasAntachawy.PAREN_DER,LexemasAntachawy.PAREN_DER,node)
        self.consume(EtiquetasAntachawy.SALTO_LINEA,LexemasAntachawy.SALTO_LINEA,node)
        self.consume(EtiquetasAntachawy.LLAVE_IZQ,LexemasAntachawy.LLAVE_IZQ,node)
        self.consume(EtiquetasAntachawy.SALTO_LINEA,LexemasAntachawy.SALTO_LINEA,node)
        node_lista_sentencias = self.lista_sentencias()
        node_lista_sentencias.parent = node
        self.consume(EtiquetasAntachawy.LLAVE_DER,LexemasAntachawy.LLAVE_DER,node)
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
        elif self.current_token.etiqueta in primeros["Condicional"]:
            node_condicional = self.condicional()
            node_condicional.parent = node
        self.consume(EtiquetasAntachawy.SALTO_LINEA,LexemasAntachawy.SALTO_LINEA,node)
        return node
    
    def condicional(self):
        node = Node("Condicional")
        self.consume(EtiquetasAntachawy.CONDICION_ARI, LexemasAntachawy.ARI, node)
        self.consume(EtiquetasAntachawy.PAREN_IZQ, LexemasAntachawy.PAREN_IZQ, node)
        node_expresion = self.expresion_condicion()
        node_expresion.parent = node
        self.consume(EtiquetasAntachawy.PAREN_DER, LexemasAntachawy.PAREN_DER, node)
        self.consume(EtiquetasAntachawy.SALTO_LINEA, LexemasAntachawy.SALTO_LINEA, node)
        self.consume(EtiquetasAntachawy.LLAVE_IZQ, LexemasAntachawy.LLAVE_IZQ, node)
        self.consume(EtiquetasAntachawy.SALTO_LINEA, LexemasAntachawy.SALTO_LINEA, node)
        node_lista_sentencias = self.lista_sentencias()
        node_lista_sentencias.parent = node
        self.consume(EtiquetasAntachawy.LLAVE_DER, LexemasAntachawy.LLAVE_DER, node)
        self.consume(EtiquetasAntachawy.SALTO_LINEA, LexemasAntachawy.SALTO_LINEA, node)
        node_condicional_prime = self.condicional_prime()
        node_condicional_prime.parent = node
        return node

    def condicional_prime(self):
        node = Node("CondicionalPrime")
        if self.current_token.etiqueta == EtiquetasAntachawy.CONDICION_MANA_CHAYQA_ARI:
            self.consume(EtiquetasAntachawy.CONDICION_MANA_CHAYQA_ARI, LexemasAntachawy.MANA_CHAYQA_ARI, node)
            self.consume(EtiquetasAntachawy.PAREN_IZQ, LexemasAntachawy.PAREN_IZQ, node)
            node_expresion = self.expresion_condicion()
            node_expresion.parent = node
            self.consume(EtiquetasAntachawy.PAREN_DER, LexemasAntachawy.PAREN_DER, node)
            self.consume(EtiquetasAntachawy.SALTO_LINEA, LexemasAntachawy.SALTO_LINEA, node)
            self.consume(EtiquetasAntachawy.LLAVE_IZQ, LexemasAntachawy.LLAVE_IZQ, node)
            self.consume(EtiquetasAntachawy.SALTO_LINEA, LexemasAntachawy.SALTO_LINEA, node)
            node_lista_sentencias = self.lista_sentencias()
            node_lista_sentencias.parent = node
            self.consume(EtiquetasAntachawy.LLAVE_DER, LexemasAntachawy.LLAVE_DER, node)
            self.consume(EtiquetasAntachawy.SALTO_LINEA, LexemasAntachawy.SALTO_LINEA, node)
            node_condicional_prime = self.condicional_prime()
            node_condicional_prime.parent = node

        elif self.current_token.etiqueta == EtiquetasAntachawy.CONDICION_MANA_CHAYQA:
            self.consume(EtiquetasAntachawy.CONDICION_MANA_CHAYQA, LexemasAntachawy.MANA_CHAYQA, node)
            self.consume(EtiquetasAntachawy.SALTO_LINEA, LexemasAntachawy.SALTO_LINEA, node)
            self.consume(EtiquetasAntachawy.LLAVE_IZQ, LexemasAntachawy.LLAVE_IZQ, node)
            self.consume(EtiquetasAntachawy.SALTO_LINEA, LexemasAntachawy.SALTO_LINEA, node)
            node_lista_sentencias = self.lista_sentencias()
            node_lista_sentencias.parent = node
            self.consume(EtiquetasAntachawy.LLAVE_DER, LexemasAntachawy.LLAVE_DER, node)
            self.consume(EtiquetasAntachawy.SALTO_LINEA, LexemasAntachawy.SALTO_LINEA, node)
        return node

    def expresion_condicion(self):
        node = Node("ExpresionCondicion")
        if self.current_token.etiqueta in primeros["ExpresionCondicion"]:
            node_expresion = self.expresion_relacional()
            node_expresion.parent = node
            node_expresion_condicion_prime = self.expresion_condicion_prime()
            node_expresion_condicion_prime.parent = node
        else:
            lexema = SALTO_DE_LINEA if self.current_token.lexema == '\n' else self.current_token.lexema
            mensaje = f"Error: '{lexema}' no es una expresión condicional"
            self.panic_mode(mensaje, EtiquetasAntachawy.SALTO_LINEA, parent=node)
        return node

    def expresion_condicion_prime(self):
        node = Node("ExpresionCondicionPrime")
        if self.current_token.etiqueta in primeros["ExpresionCondicionPrime"]:
            node_operador_logico = self.operador_logico()
            node_operador_logico.parent = node
            node_expresion_condicion = self.expresion_condicion()
            node_expresion_condicion.parent = node
        return node

    def expresion_relacional(self):
        node = Node("ExpresionRelacional")
        node_expresion = self.termino()
        node_expresion.parent = node
        node_operador_relacional = self.operador_relacional()
        node_operador_relacional.parent = node
        node_expresion_relacional = self.termino()
        node_expresion_relacional.parent = node
        return node

    def operador_logico(self):
        node = Node("OperadorLogico")
        if self.current_token.etiqueta in primeros["OperadorLogico"]:
            node_logico = Node(self.current_token.etiqueta)
            Node(self.current_token.lexema, parent=node_logico)
            self.consume(self.current_token.etiqueta,self.current_token.lexema,node)
        return node

    def operador_relacional(self):
        node = Node("OperadorRelacional")
        if self.current_token.etiqueta in primeros["OperadorRelacional"]:
            node_relacional = Node(self.current_token.etiqueta)
            Node(self.current_token.lexema, parent=node_relacional)
            self.consume(self.current_token.etiqueta,self.current_token.lexema,node)
        else:
            lexema = SALTO_DE_LINEA if self.current_token.lexema == '\n' else self.current_token.lexema
            mensaje = f"Error: '{lexema}' no es un operador relacional"
            self.panic_mode(mensaje, EtiquetasAntachawy.SALTO_LINEA, parent=node)
        return node

    def declaraciones(self):
        node = Node("Declaraciones")
        node_tipo = self.tipo()
        node_tipo.parent = node
        node_id = Node(self.current_token.etiqueta)
        node_id.parent = node
        self.consume(EtiquetasAntachawy.ID,LexemasAntachawy.ID,node_id)
        node_declaraciones_prime = self.declaraciones_prime()
        node_declaraciones_prime.parent = node
        return node
    
    def declaraciones_prime(self):
        node = Node("DeclaracionesPrime")
        if self.current_token.etiqueta in primeros["DeclaracionesPrime"]:
            node_asignacion = Node(self.current_token.etiqueta)
            node_asignacion.parent = node
            self.consume(EtiquetasAntachawy.ASIGNACION,LexemasAntachawy.ASIGNA,node_asignacion)
            node_expresion = self.expresion()
            node_expresion.parent = node
        return node
    
    def asignaciones(self):
        node = Node("Asignaciones")
        node_id = Node(self.current_token.etiqueta, parent=node)
        self.consume(EtiquetasAntachawy.ID,LexemasAntachawy.ID,node_id)
        node_asignacion = Node(self.current_token.etiqueta, parent=node)
        self.consume(EtiquetasAntachawy.ASIGNACION,LexemasAntachawy.ASIGNA,node_asignacion)
        node_expresion = self.expresion()
        node_expresion.parent = node
        return node
    
    def impresion(self):
        node = Node("Impresiones")
        self.consume(EtiquetasAntachawy.IMPRESION,LexemasAntachawy.RIKUCHIY,node)
        self.consume(EtiquetasAntachawy.PAREN_IZQ,LexemasAntachawy.PAREN_IZQ,node)
        node_expresion_impresion = self.expresion_impresion()
        node_expresion_impresion.parent = node
        self.consume(EtiquetasAntachawy.PAREN_DER,LexemasAntachawy.PAREN_DER,node)
        return node
    
    def tipo(self):
        node = Node("Tipo")
        node_tipo = Node(self.current_token.etiqueta)
        Node(self.current_token.lexema, parent=node_tipo)
        self.consume(self.current_token.etiqueta,self.current_token.lexema,node)
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
        self.consume(self.current_token.etiqueta,self.current_token.lexema,node)
        return node
    
    def operador_multiplicativo(self):
        node = Node("OperadorMultiplicativo")
        node_multiplicativo = Node(self.current_token.etiqueta)
        Node(self.current_token.lexema, parent=node_multiplicativo)
        self.consume(self.current_token.etiqueta,self.current_token.lexema,node)
        return node
    
    def termino(self):
        node = Node("Termino")
        if self.current_token.etiqueta in primeros["Termino"]:
            if self.current_token.etiqueta == EtiquetasAntachawy.PAREN_IZQ:
                self.consume(EtiquetasAntachawy.PAREN_IZQ,LexemasAntachawy.PAREN_IZQ,node)
                node_expresion = self.expresion()
                node_expresion.parent = node
                self.consume(EtiquetasAntachawy.PAREN_DER,LexemasAntachawy.PAREN_DER,node)
            else:
                node_termino = Node(self.current_token.etiqueta)
                node_termino.parent = node
                self.consume(self.current_token.etiqueta,self.current_token.lexema,node_termino)

        else:
            lexema = SALTO_DE_LINEA if self.current_token.lexema == '\n' else self.current_token.lexema
            mensaje = f"Error: '{lexema}'"
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
            self.consume(EtiquetasAntachawy.COMA,LexemasAntachawy.COMA,node)
            node_expresion_impresion = self.expresion_impresion()
            node_expresion_impresion.parent = node
        return node
    
    def save_syntax_outputs(self, root: object, base_filename: str):
        os.makedirs("outputs/sintactic", exist_ok=True)
        render_tree(root, base_filename + ".txt")
        export_tree(root, base_filename)