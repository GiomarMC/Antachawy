class Token(object):
    def __init__(self, lexema, etiqueta, linea, idx):
        # Inicializa un token con su lexema, etiqueta, línea y índice
        self.lexema = lexema  # El lexema asociado al token
        self.etiqueta = etiqueta  # La etiqueta o tipo del token
        self.linea = linea  # La línea del archivo donde se encontró el token
        self.idx = idx  # El índice dentro de la línea donde se encontró el token

    def found_at(self) -> str:
        # Devuelve una cadena que representa la posición del token en el formato (línea, índice)
        return "({}, {})".format(self.linea, self.idx - 1)

    def __str__(self) -> str:
        # Devuelve una representación en cadena del token en el formato (lexema, etiqueta, línea)
        return "({}, {}, {})".format(self.lexema, self.etiqueta, self.linea)