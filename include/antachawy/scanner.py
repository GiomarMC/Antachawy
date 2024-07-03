from antachawy.definitions import LexemasAntachawy, EtiquetasAntachawy, lexema_a_etiqueta, simbolos_compuestos
from antachawy.token import Token

class Scanner:
    def __init__(self):
        # Inicializa el scanner con valores predeterminados
        self.code = ""                          # Contenido del archivo fuente
        self.lineno = 1                         # Línea actual del archivo fuente
        self.current_char = ""                  # Caracter actual que se está procesando
        self.idx = 0                            # Índice actual en el archivo fuente
        self.tokens = []                        # Lista de tokens generados

    def __open_file(self, filename: str):
        # Abre un archivo y guarda su contenido en self.code
        with open(filename, "r", encoding='utf-8') as file:
            self.code = file.read()

    def __get_next_char(self):
        # Obtiene el siguiente caracter del archivo
        if self.idx < len(self.code):
            self.current_char = self.code[self.idx]
            self.idx += 1
            return self.current_char
        else:
            self.current_char = None
            return None

    def __get_tokens(self):
        # Principal función de análisis que recorre el archivo y genera tokens
        while self.__get_next_char() is not None:
            if self.current_char.isspace():
                # Ignora los espacios en blanco
                if self.current_char == '\n':
                    self.lineno += 1
                continue
            elif self.current_char == '/' and self.__peek_next_char() == '/':
                # Ignora los comentarios de línea
                self.__skip_line_comment()
            elif self.current_char == '/' and self.__peek_next_char() == '*':
                # Ignora los comentarios de bloque
                self.__skip_block_comment()
            elif self.current_char == '"':
                # Maneja las cadenas
                self.tokens.append(self.__get_string())
            elif self.current_char == "'":
                # Maneja los caracteres
                self.tokens.append(self.__get_character())
            elif self.current_char.isdigit():
                # Maneja los números
                self.tokens.append(self.__get_number())
            elif self.current_char.isalpha():
                # Maneja los identificadores y palabras clave
                self.tokens.append(self.__get_id())
            else:
                # Maneja caracteres especiales
                self.tokens.append(self.__get_special_character())

        return self.tokens

    def __peek_next_char(self):
        # Devuelve el siguiente carácter sin avanzar el índice
        if self.idx < len(self.code):
            return self.code[self.idx]
        else:
            return None

    def __skip_line_comment(self):
        # Ignora los comentarios de línea
        while self.__get_next_char() is not None and self.current_char != '\n':
            continue
        self.lineno += 1

    def __skip_block_comment(self):
        # Ignora los comentarios de bloque
        while True:
            if self.__get_next_char() is None:
                raise SyntaxError("Comentario de bloque no terminado en la línea {}".format(self.lineno))  # Traducir la expresion a quechua (Comentario de bloque no terminado en la línea {})
            if self.current_char == '*' and self.__peek_next_char() == '/':
                self.__get_next_char()
                break
            if self.current_char == '\n':
                self.lineno += 1

    def __get_string(self):
        # Procesa y devuelve un token de cadena
        startidx = self.idx - 1
        lexema = '"'

        while self.__get_next_char() and self.current_char != '"':
            lexema += self.current_char

        if self.current_char != '"':
            raise SyntaxError("literal de cadena no terminada en la línea {}".format(self.lineno)) # Traducir la expresion a quechua (literal de cadena no terminada en la línea {})

        lexema += '"'
        return Token(lexema, EtiquetasAntachawy.CADENA, linea=self.lineno, idx=startidx)

    def __get_character(self):
        # Procesa y devuelve un token de caracter
        startidx = self.idx - 1
        lexema = "'"

        while self.__get_next_char() and self.current_char != "'":
            lexema += self.current_char

        if self.current_char != "'":
            raise SyntaxError("literal de caracter no terminada en la línea {}".format(self.lineno)) # Traducir la expresion a quechua (literal de caracter no terminada en la línea {})

        lexema += "'"
        return Token(lexema, EtiquetasAntachawy.TIPO_SANANPA, self.lineno, startidx)

    def __get_number(self):
        # Procesa y devuelve un token de número
        startidx = self.idx - 1
        lexema = self.current_char

        while self.__get_next_char() and (self.current_char.isdigit() or self.current_char == "."):
            lexema += self.current_char

        if self.current_char:
            self.idx -= 1

        return Token(lexema, EtiquetasAntachawy.NUMERO, self.lineno, startidx)

    def __get_id(self):
        # Procesa y devuelve un token de identificador o palabra clave
        startidx = self.idx - 1
        lexema = self.current_char

        while self.__get_next_char() and (self.current_char.isalnum() or self.current_char == "_"):
            lexema += self.current_char

        if self.current_char:
            self.idx -= 1

        etiqueta = lexema_a_etiqueta.get(lexema, EtiquetasAntachawy.ID)

        return Token(lexema, etiqueta, self.lineno, startidx)

    def __get_special_character(self):
        # Procesa y devuelve un token de carácter especial
        startidx = self.idx - 1
        lexema = self.current_char

        if self.idx < len(self.code) and self.code[startidx: startidx + 2] in simbolos_compuestos:
            lexema += self.code[self.idx]
            self.idx += 1
        elif lexema in lexema_a_etiqueta:
            return Token(lexema, lexema_a_etiqueta[lexema], self.lineno, startidx)
        
        if lexema in lexema_a_etiqueta:
            return Token(lexema, lexema_a_etiqueta[lexema], self.lineno, startidx)
        else:
            raise SyntaxError("Carácter no reconocido '{}' en la línea {}".format(lexema, self.lineno))

    def tokenize(self, filename: str):
        # Tokeniza el contenido del archivo dado
        self.__open_file(filename)
        return self.__get_tokens()