from antachawy.compiler import Compiler

import typer
from pathlib import Path

def file_exists(path: str):
    file_path = Path(path)
    if not file_path.exists():
        raise typer.BadParameter(f"Archivo de entrada no encontrado: {path}")
    return file_path

def main(file_path: Path = typer.Argument("./inputs/main.awy", help="Archivo de entrada con codigo fuente", callback=file_exists)):
    compiler = Compiler(file_path)
    resutl = compiler.compile()
    if resutl:
        print("Compilación exitosa")
    else:
        print("Compilación fallida")

if __name__ == "__main__":
    typer.run(main)