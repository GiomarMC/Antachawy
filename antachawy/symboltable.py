class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add(self, name, var_type):
        if name in self.symbols:
            raise ValueError(f"Variable '{name}' ya definida.")
        self.symbols[name] = var_type

    def get(self, name):
        return self.symbols.get(name)

    def __repr__(self):
        return str(self.symbols)
    
    def print_table(self):
        if not self.symbols:
            print("La tabla de símbolos está vacía.")
            return
        
        print("Tabla de Símbolos:")
        print(f"{'Nombre':<15} {'Tipo':<10}")
        print("="*25)
        for name, var_type in self.symbols.items():
            print(f"{name:<15} {var_type:<10}")