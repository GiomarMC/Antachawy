import argparse
from antachawy.compiler import Compiler
from pathlib import Path

def file_exists(path: str):
    file_path = Path(path)
    if not file_path.exists():
        raise argparse.ArgumentTypeError(f"Archivo de entrada no encontrado: {path}")
    return file_path

def main():
    parser = argparse.ArgumentParser(description="Antachawy compiler")
    parser.add_argument("file_path", type=file_exists, help="Archivo de entrada con código fuente")
    parser.add_argument("-o", "--output", type=str, help="Nombre del archivo de salida")
    parser.add_argument("-d", "--debug", action="store_true", help="Genera archivos de depuración en la carpeta outputs")

    args = parser.parse_args()
    
    output_file = args.output if args.output else None
    debug = args.debug
    file_path = str(args.file_path)
    
    compiler = Compiler(file_path, output_file, debug)
    result = compiler.compile()
    
    if result:
        print("Successful compilation")
    else:
        print("Failed compilation")

if __name__ == "__main__":
    main()