import re
from antachawi.sourcecode import SourceCode

class AntachawyToCppTranslator:
    def __init__(self, source_code: SourceCode):
        self.code = source_code
        self.c_code = ["#include <iostream>", "#include <string>", "#include <stdbool.h>", "using namespace std;"]  # Incluir las bibliotecas de C++
        self.translations = {
            r'\bqhapaq\b': "int main",
            r'\byupay\b': "int",
            r'\bchunkayuq\b': "float",
            r'\bsananpa\b': "char",
            r'\bqaytu\b': "string",  # Cambiado a std::string para C++
            r'\bbool\b': "bool",
            r'\bari\b': "if",
            r'\bmana_chayqa_ari\b': "else if",  # else if en C++
            r'\bmana_chayqa\b': "else",
            r'\brikuchiy\b': "cout",
            r'\byanqa\b': "true",
            r'\bchiqaq\b': "false"
        }

    def translate_line(self, line):
        # Reemplaza las palabras de Antachawy por las de C++ usando expresiones regulares
        translated_line = line
        for antachawy_word, c_word in self.translations.items():
            translated_line = re.sub(antachawy_word, c_word, translated_line)

        if "cout" in translated_line:
            translated_line = self.translate_cout(translated_line)

        # Asegurar que no se agregue un ; después de estructuras de control
        if (not translated_line.strip().startswith("if") and
            not translated_line.strip().startswith("else if") and
            not translated_line.strip().startswith("else") and
            not translated_line.strip().startswith("int main") and
            not translated_line.strip().endswith('{') and
            not translated_line.strip().endswith('}') and
            not translated_line.strip().endswith(';') and
            len(translated_line.strip()) > 0):  # Ignoramos líneas vacías
            translated_line += ";"

        # Asegurar que no se pongan ; después de "if", "else if", "else" o "int main"
        if (translated_line.strip().endswith(";") and
            (translated_line.strip().startswith("if") or 
             translated_line.strip().startswith("else if") or 
             translated_line.strip().startswith("else") or 
             translated_line.strip().startswith("int main"))):
            translated_line = translated_line[:-1]

        return translated_line

    def translate_cout(self, line):
        # Extrae los argumentos de cout (similar a printf)
        start = line.find('(')
        end = line.find(')')
        if start != -1 and end != -1:
            args_str = line[start + 1:end]
            args = args_str.split(',')

            # Preparar la salida para cout
            cout_args = []
            for arg in args:
                arg = arg.strip()
                if '"' in arg:  # Si es una cadena de texto
                    cout_args.append(arg)
                elif arg in ['true', 'false']:  # Si es booleano
                    cout_args.append(arg)
                elif re.match(r'^[a-zA-Z_]\w*$', arg):  # Si es un identificador (variable)
                    cout_args.append(arg)
                else:  # Por defecto tratamos como número
                    cout_args.append(arg)

            # Crear la sentencia cout en C++
            translated_cout = f"cout << {' << '.join(cout_args)} << endl;"

            return translated_cout
        return line

    def get_variable_type(self, variable_name):
        """
        Obtener el tipo de una variable dada su declaración previa en el código.
        Esto es útil para saber cómo usar 'cout' correctamente para esa variable.
        """
        for line in self.c_code:
            if variable_name in line:
                if "int" in line:
                    return "int"
                elif "float" in line:
                    return "float"
                elif "char " in line:  # Evitar confusión con "string"
                    return "char"
                elif "string" in line:
                    return "string"
                elif "bool" in line:
                    return "bool"
        return "int"  # Si no se encuentra el tipo, asumimos que es un int por defecto
    
    def translate(self):
        in_block_comment = False
        for lineno, line in self.code.get_all_lines().items():
            stripped_line = line.strip()

            # Manejo de comentarios de bloque :* *:
            if ':*' in stripped_line and '*:' in stripped_line:
                continue
            elif ':*' in stripped_line:
                in_block_comment = True
                continue
            elif '*:' in stripped_line:
                in_block_comment = False
                continue

            # Si estamos dentro de un comentario de bloque, ignoramos la línea
            if in_block_comment:
                continue

            # Ignoramos comentarios de línea y líneas vacías
            if stripped_line.startswith('::') or len(stripped_line) == 0:
                continue

            # Traducción línea por línea
            translated_line = self.translate_line(stripped_line)
            if translated_line:
                self.c_code.append(translated_line)

        return "\n".join(self.c_code)

    def save_translated_code(self, filename):
        # Guardar el código traducido en un archivo
        with open(filename, "w") as file:
            for line in self.c_code:
                file.write(line + "\n")