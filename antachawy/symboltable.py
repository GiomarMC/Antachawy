class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add(self, name, var_type, scope="global", value=None):
        if name in self.symbols:
            raise ValueError(f"Variable '{name}' ya definida.")
        self.symbols[name] = {"type": var_type, "scope": scope, "value": value}

    def get(self, name):
        if name in self.symbols:
            return self.symbols[name]["type"]
        return None
    
    def get_value(self, name):
        if name in self.symbols:
            return self.symbols[name]["value"]
        return None
    
    def set_value(self, name, value):
        if name in self.symbols:
            self.symbols[name]["value"] = value
        else:
            raise ValueError(f"Variable '{name}' no definida.")
    
    def get_scope(self, name):
        if name in self.symbols:
            return self.symbols[name]["scope"]
        return None
    
    def __repr__(self):
        return str(self.symbols)
    
    def print_table(self):
        if not self.symbols:
            print("La tabla de símbolos está vacía.")
            return
        
        print("\nTabla de Símbolos:")
        print(f"{'Nombre':<15} {'Tipo':<10} {'Ambito':<10} {'Valor':<10}")
        print("="*45)
        for name, info in self.symbols.items():
            print(f"{name:<15} {info['type']:<10} {info['scope']:<10} {str(info['value']):<10}")
        print("\n")