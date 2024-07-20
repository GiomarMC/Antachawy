from tabulate import tabulate

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

    def get_all_by_type(self, var_type):
        return {name: info for name, info in self.symbols.items() if info["type"] == var_type}

    def __repr__(self):
        return str(self.symbols)

    def print_table(self):
        if not self.symbols:
            print("La tabla de símbolos está vacía.")
            return

        headers = ["Nombre", "Tipo", "Ámbito", "Valor"]
        rows = [[name, info["type"], info["scope"], info["value"]] for name, info in self.symbols.items()]
        print("\nTabla de Símbolos:")
        print(tabulate(rows, headers, tablefmt="grid"))
        print("\n")

class PrintTable:
    def __init__(self):
        self.tables = []

    def add_table(self):
        self.tables.append([])

    def add_entry(self, table_index, value, tipo):
        self.tables[table_index].append((value, tipo))

    def get_entries_by_index(self, index):
        if 0 <= index < len(self.tables):
            return self.tables[index]
        else:
            return None

    def print_entries(self):
        for i, table in enumerate(self.tables):
            print(f"\nSentencia de Impresión {i + 1}:")
            headers = ["siqiy", "Tipo"]
            rows = [(entry_value, entry_type) for entry_value, entry_type in table]
            print(tabulate(rows, headers, tablefmt="grid"))
            print("\n")