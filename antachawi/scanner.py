from antachawi.definitions import LexemasAntachawy, EtiquetasAntachawy, lexema_a_etiqueta, simbolos_compuestos
from antachawi.token import Token
from antachawi.sourcecode import SourceCode
from tabulate import tabulate
import re
import os

class Scanner:
    def __init__(self, source_code: SourceCode):
        # Inicializa el scanner con valores predeterminados
        self.code = ""                          # Contenido del archivo fuente
        self.lineno = 1                         # Línea actual del archivo fuente
        self.current_char = ""                  # Caracter actual que se está procesando
        self.idx = 0                            # Índice actual en el archivo fuente
        self.tokens = []                        # Lista de tokens generados
        self.errors = []                        # Lista de errores encontrados
        self.source_code = source_code          # Objeto SourceCode

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
    
    def __remove_coments(self, line: str):
        # Remueve los comentarios de una línea
        line = re.sub(r'::.*', '', line)
        line = re.sub(r'/:*.*\*:', '', line)
        return line

    def __get_current_line_content(self):
        # Devuelve el contenido de la línea actual donde se encuentra el índice(self.idx)
        return self.source_code.get_line(self.lineno)

    def __get_tokens(self):
        # Principal función de análisis que recorre el archivo y genera tokens
        while self.__get_next_char() is not None:
            if self.current_char.isspace():
                # Ignora los espacios en blanco
                if self.current_char == '\n':
                    self.tokens.append(Token("\n", EtiquetasAntachawy.SALTO_LINEA, self.lineno, self.idx - 1))
                    self.lineno += 1
                continue
            elif self.current_char == ':' and self.__peek_next_char() == ':':
                # Ignora los comentarios de línea
                self.__skip_line_comment()
            elif self.current_char == ':' and self.__peek_next_char() == '*':
                # Ignora los comentarios de bloque
                self.__skip_block_comment()
            elif self.current_char == '"':
                # Maneja las cadenas
                token = self.__get_string()
                if token:
                    self.tokens.append(token)
            elif self.current_char == "'":
                # Maneja los caracteres
                token = self.__get_character()
                if token:
                    self.tokens.append(token)
            elif self.current_char.isdigit():
                # Maneja los números
                token = self.__get_number()
                if token:
                    self.tokens.append(token)
            elif self.current_char.isalpha():
                # Maneja los identificadores y palabras clave
                token = self.__get_id()
                if token:
                    self.tokens.append(token)
            else:
                # Maneja caracteres especiales
                token = self.__get_special_character()
                if token:
                    self.tokens.append(token)
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
        if self.current_char == '\n':
            self.tokens.append(Token("\n", EtiquetasAntachawy.SALTO_LINEA, self.lineno, self.idx - 1))
        self.lineno += 1

    def __skip_block_comment(self):
        # Ignora los comentarios de bloque
        while True:
            if self.__get_next_char() is None:
                self.errors.append({
                    "mensaje": "Comentario de bloque no terminado",
                    "linea": self.lineno,
                    "contenido": self.__get_current_line_content()
                })
                return
            if self.current_char == '*' and self.__peek_next_char() == ':':
                self.__get_next_char()
                break
            if self.current_char == '\n':
                self.lineno += 1

    def __get_string(self):
        # Procesa y devuelve un token de cadena
        startidx = self.idx - 1
        lexema = '"'

        while self.__get_next_char() and self.current_char != '"' and self.current_char != '\n':
            lexema += self.current_char

        if self.current_char != '"':
            self.errors.append({
                "mensaje": "Literal de cadena no terminada en la línea",
                "linea": self.lineno,
                "contenido": self.__get_current_line_content()
            })
            return
        lexema += '"'
        return Token(lexema, EtiquetasAntachawy.CADENA, linea=self.lineno, idx=startidx)

    def __get_character(self):
        # Procesa y devuelve un token de caracter
        startidx = self.idx - 1
        lexema = "'"
        character_content = ""

        while self.__get_next_char() and self.current_char != "'" and self.current_char != '\n':
            character_content += self.current_char
            lexema += self.current_char

        if len(character_content) > 1 and self.current_char != "\n":
            self.errors.append({
                "mensaje": "Caracteres multiples en un literal de caracter",
                "linea": self.lineno,
                "contenido": self.__get_current_line_content()
            })
            return
        
        if self.current_char != "'":
            self.errors.append({
                "mensaje": "Literal de caracter no terminado en la línea",
                "linea": self.lineno,
                "contenido": self.__get_current_line_content()
            })
            self.lineno += 1
            return
        lexema += "'"
        return Token(lexema, EtiquetasAntachawy.CARACTER, self.lineno, startidx)

    def __get_number(self):
        # Procesa y devuelve un token de número
        startidx = self.idx - 1
        lexema = self.current_char
        decimal_point_count = 0

        if self.current_char == ".":
            decimal_point_count += 1

        while self.__get_next_char() and (self.current_char.isdigit() or self.current_char == "."):
            if self.current_char == ".":
                decimal_point_count += 1
                if decimal_point_count > 1:
                    self.errors.append({
                        "mensaje": "Número con más de un punto decimal",
                        "linea": self.lineno,
                        "contenido": self.__get_current_line_content()
                    })
                    return
            lexema += self.current_char

        if self.current_char.isalpha():
            while self.current_char and self.current_char.isalpha():
                lexema += self.current_char
                self.__get_next_char()
            
            self.errors.append({
                "mensaje": "Numero seguido por caracteres no permitidos",
                "linea": self.lineno,
                "contenido": self.__get_current_line_content()
            })
            return

        if self.current_char:
            self.idx -= 1
        
        if "." in lexema:
            return Token(lexema, EtiquetasAntachawy.NUMEROFLOTANTE, self.lineno, startidx)
        else:
            return Token(lexema, EtiquetasAntachawy.NUMEROENTERO, self.lineno, startidx)

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
            self.errors.append({
                "mensaje": "Caracter no reconocido",
                "linea": self.lineno,
                "contenido": self.__get_current_line_content()
            })
            return

    def tokenize(self, filename: str):
        # Tokeniza el contenido del archivo dado
        self.__open_file(filename)
        return self.__get_tokens()
    
    def save_tokens(self, filename="tokens.txt"):
        os.makedirs("outputs/lexicon", exist_ok=True)
        filepath = os.path.join("outputs/lexicon", filename)
        headers = ["Lexema", "Etiqueta", "Linea", "Indice"]
        rows = [[token.lexema, token.etiqueta, token.linea, token.idx] for token in self.tokens]
        with open(filepath, "w") as file:
            file.write(tabulate(rows, headers, tablefmt="grid"))