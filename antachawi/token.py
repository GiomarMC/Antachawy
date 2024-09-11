class Token(object):
    def __init__(self, lexema, etiqueta, linea, idx):
        self.lexema = lexema
        self.etiqueta = etiqueta
        self.linea = linea
        self.idx = idx

    def found_at(self) -> str:
        # Devuelve una cadena que representa la posición del token en el formato (línea, índice)
        return "({}, {})".format(self.linea, self.idx - 1)

    def __str__(self) -> str:
        # Devuelve una representación en cadena del token en el formato (lexema, etiqueta, línea)
        return "({}, {}, {})".format(self.lexema, self.etiqueta, self.linea)