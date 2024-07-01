from antachawy.definitions import LexemasAntachawy, EtiquetasAntachawy, lexema_a_etiqueta, simbolos_compuestos
from antachawy.token import Token

class Scanner:
    def __init__(self):
        self.lineno = 1
        self.linecontent = ""
        self.current_atom = ""
        self.text = ""
        self.idx = 0