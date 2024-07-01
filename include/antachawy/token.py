class Token(object):
    def __init__(self, lexema, etiqueta, linea, idx):
        self.lexema = lexema
        self.etiqueta = etiqueta
        self.linea = linea
        self.idx = idx

    def found_at(self) -> str:
        return "({}, {})".format(self.linea, self.idx - 1)
    
    def __str__(self) -> str:
        return "({}, {}, {})".format(self.lexema, self.etiqueta, self.linea)