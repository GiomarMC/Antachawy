from antachawy.definitions import LexemasAntachawy, EtiquetasAntachawy, lexema_a_etiqueta, simbolos_compuestos
from antachawy.token import Token

class Scanner:
    def __init__(self):
        self.code = ""
        self.lineno = 1
        self.current_char = ""
        self.idx = 0
        self.tokens = []

    def __open_file(self, filename: str):
        with open(filename, "r", encoding= 'utf-8') as file:
            self.code = file.read()

    def __get_next_char(self):
        if self.idx < len(self.code):
            self.current_char = self.code[self.idx]
            self.idx += 1
            return self.current_char
        else:
            self.current_char = None
            return None

    def __get_tokens(self):
        while self.__get_next_char() is not None:
            if self.current_char.isspace():
                if self.current_char == '\n':
                    self.lineno += 1
                continue
            elif self.current_char == '/' and self.__peek_next_char() == '/':
                self.__skip_line_comment()
            elif self.current_char == '/' and self.__peek_next_char() == '*':
                self.__skip_block_comment()
            elif self.current_char == '"':
                self.tokens.append(self.__get_string())
            elif self.current_char == "'":
                self.tokens.append(self.__get_character())
            elif self.current_char.isdigit():
                self.tokens.append(self.__get_number())
            elif self.current_char.isalpha():
                self.tokens.append(self.__get_id())
            else:
                self.tokens.append(self.__get_special_character())

        return self.tokens
    
    def __peek_next_char(self):
        if self.idx < len(self.code):
            return self.code[self.idx]
        else:
            return None
        
    def __skip_line_comment(self):
        while self.__get_next_char() is not None and self.current_char != '\n':
            continue
        self.lineno += 1

    def __skip_block_comment(self):
        while True:
            if self.__get_next_char() is None:
                raise SyntaxError("Comentario de bloque no terminado en la línea {}".format(self.lineno))
            if self.current_char == '*' and self.__peek_next_char() == '/':
                self.__get_next_char()
                break
            if self.current_char == '\n':
                self.lineno += 1

    def __get_string(self):
        startidx = self.idx - 1
        lexema = '"'

        while self.__get_next_char() and self.current_char != '"':
            lexema += self.current_char
        
        #if self.current_char != '"':
        #    raise SyntaxError("literal de cadena no terminada en la línea {}".format(self.lineno)) #Traducir la expresion a quechua (literal de cadena no terminada en la línea {})

        lexema += '"'
        self.idx += 1

        return Token(lexema, EtiquetasAntachawy.CADENA, linea = self.lineno, idx = startidx)
    
    def __get_character(self):
        startidx = self.idx - 1
        lexema = "'"

        while self.__get_next_char() and self.current_char != "'":
            lexema += self.current_char

        if self.current_char != "'":
            raise SyntaxError("literal de caracter no terminada en la línea {}".format(self.lineno)) #Traducir la expresion a quechua (literal de caracter no terminada en la línea {})
        
        lexema += "'"
        self.idx += 1

    def __get_number(self):
        startidx = self.idx - 1
        lexema = self.current_char

        while self.__get_next_char() and (self.current_char.isdigit() or self.current_char == "."):
            lexema += self.current_char

        if self.current_char:
            self.idx -= 1

        return Token(lexema, EtiquetasAntachawy.NUMERO, self.lineno, startidx)
    
    def __get_id(self):
        startidx = self.idx - 1
        lexema = self.current_char

        while self.__get_next_char() and (self.current_char.isalnum() or self.current_char == "_"):
            lexema += self.current_char

        if self.current_char:
            self.idx -= 1

        etiqueta = lexema_a_etiqueta.get(lexema, EtiquetasAntachawy.ID)

        return Token(lexema, etiqueta, self.lineno, startidx)
    
    def __get_special_character(self):
        startidx = self.idx - 1
        lexema = self.current_char

        if self.idx < len(self.code) and self.code[startidx:startidx+2] in simbolos_compuestos:
            lexema += self.code[self.idx]
            self.idx += 1
        elif self.idx < len(self.code) and self.code[startidx] in simbolos_compuestos:
            lexema = self.code[startidx]
        
        if lexema in lexema_a_etiqueta:
            self.tokens.append((lexema, lexema_a_etiqueta[lexema]))
            self.idx += 1
            if self.idx < len(self.code):
                self.current_char = self.code[self.idx]
            return
        
        if lexema == ";":
            self.tokens.append((lexema, lexema_a_etiqueta[LexemasAntachawy.PUNTOYCOMA]))
            self.idx += 1
            if self.idx < len(self.code):
                self.current_char = self.code[self.idx]
            return
        
        self.tokens.append((lexema, EtiquetasAntachawy.ID))
        self.idx += 1
        if self.idx < len(self.code):
            self.current_char = self.code[self.idx]


    def tokenize(self, filename: str):
        self.__open_file(filename)
        return self.__get_tokens()