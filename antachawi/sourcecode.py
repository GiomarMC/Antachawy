# Autor: Giomar Muñoz
# Fecha: 2023-09-26
# Descripción: Clase que representa un archivo de código fuente

class SourceCode:
    def __init__(self, filename: str):
        self.filename = filename
        self.lines = {}         # Diccionario que almacena las líneas de código
        self.__load_file()

    def __load_file(self):
        #Carga el archivo de código fuente en un diccionario
        with open(self.filename, "r", encoding='utf-8') as file:
            for lineno, line in enumerate(file, start=1):
                self.lines[lineno] = line.strip()

    def get_line(self, lineno: int) -> str:
        #Devuelve la línea de código en la posición indicada
        return self.lines.get(lineno, None)
    
    def get_all_lines(self) -> dict:
        #Devuelve todo el contenido del archivo en un diccionario
        return self.lines
    
    def print_all_lines(self):
        #Imprime todas las líneas de código
        for lineno, line in self.lines.items():
            print(f"{lineno}: {line}")