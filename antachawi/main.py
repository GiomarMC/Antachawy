import argparse
import platform
from antachawi.compiler import Compiler
from pathlib import Path

from antachawi import __version__

def main():
    parser = argparse.ArgumentParser(
        description="Antachawi compiler CLI",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
        )
    parser.add_argument(
        "file_path",
        type=Path,
        help="Archivo de entrada con código fuente"
        )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="Nombre del archivo de salida"
        )
    parser.add_argument(
        "-d",
        "--debug",
        action="store_true",
        help="Genera archivos de depuración en la carpeta outputs"
        )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"Antachawi compiler version {__version__}",
        help="Muestra la versión del compilador"
        )

    args = parser.parse_args()
    
    file_path = args.file_path
    output_file = args.output if args.output else None
    debug = args.debug
    
    if not file_path.exists():
        parser.error(f"El archivo {file_path} no existe")
    
    compiler = Compiler(str(file_path), output_file, debug)
    result = compiler.compile()
    
    if result:
        print("Successful compilation")
    else:
        print("Failed compilation")

if __name__ == "__main__":
    main()