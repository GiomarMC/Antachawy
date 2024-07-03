from antachawy.scanner import Scanner
from antachawy.token import Token

import typer
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich import box

def file_exists(path: str):
    file_path = Path(path)
    if not file_path.exists():
        raise typer.BadParameter(f"Archivo de entrada no encontrado: {path}")
    return file_path

def main(file_path: Path = typer.Argument("./inputs/main.awy", help="Archivo de entrada con codigo fuente", callback=file_exists)):
    scanner = Scanner()
    tokens = scanner.tokenize(str(file_path))

    console = Console()
    table = Table(title="Tokens Generados")
    table.add_column("Lexema", style="cyan", justify="center")
    table.add_column("Etiqueta", style="magenta", justify="center")
    table.add_column("Linea", style="green", justify="center")

    for token in tokens:
        table.add_row(token.lexema, token.etiqueta, str(token.linea))
    
    console.print(table)

if __name__ == "__main__":
    typer.run(main)