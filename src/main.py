from antachawy.scanner import Scanner
from antachawy.token import Token
from antachawy.consolehandler import ConsoleHandler

import typer
from pathlib import Path

def file_exists(path: str):
    file_path = Path(path)
    if not file_path.exists():
        raise typer.BadParameter(f"Archivo de entrada no encontrado: {path}")
    return file_path

def main(file_path: Path = typer.Argument("./inputs/main.awy", help="Archivo de entrada con codigo fuente", callback=file_exists)):
    scanner = Scanner()
    tokens = scanner.tokenize(str(file_path))
    console_handler = ConsoleHandler()
    console_handler.print_title()
    console_handler.scan_debug_table(tokens)

if __name__ == "__main__":
    typer.run(main)