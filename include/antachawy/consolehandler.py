from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table, box
from rich.panel import Panel

from os import path

class ConsoleHandler:
    console = Console()
    
    def print_title(self):
        title = """ #Antachawy Compiler """
        self.console.print(Markdown(title))

    def scan_debug_table(self, tokens):
        debug_table = Table(title="Tabla de Tokens")

        debug_table.add_column("Lexema", style="cyan", justify="center")
        debug_table.add_column("Etiqueta", style="magenta", justify="center")
        debug_table.add_column("Linea", style="green", justify="center")

        for token in tokens:
            debug_table.add_row(token.lexema, token.etiqueta, str(token.linea))

        self.console.print(debug_table, justify="center")