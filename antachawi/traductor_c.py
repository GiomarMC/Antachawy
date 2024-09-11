from antachawi.shared import symbol_table, print_table

class CodeTranslator:
    def __init__(self, optimized_code):
        self.optimized_code = optimized_code
        self.symbol_table = symbol_table
        self.print_table = print_table
        self.c_code = ""

    def translate_to_c(self):
        c_code = """
#include <stdio.h>

int main() {
"""
        for instruction in self.optimized_code:
            parts = instruction.split()
            if len(parts) == 3 and parts[1] == '=':
                dest, _, src = parts
                var_type = self.symbol_table.get(dest)
                if var_type == "yupay":
                    c_code += f"    int {dest} = {src};\n"
                elif var_type == "chunkayuq":
                    c_code += f"    float {dest} = {src};\n"
                elif var_type == "sananpa":
                    c_code += f"    char {dest} = '{src}';\n"
                elif var_type == "qaytu":
                    c_code += f"    char {dest}[] = \"{src}\";\n"
                elif var_type == "bool":
                    c_code += f"    int {dest} = {1 if src == 'chiqaq' else 0};\n"
                else:
                    c_code += f"    int {dest} = {src};\n"
            elif len(parts) == 5:
                dest, _, left, op, right = parts
                c_code += f"    int {dest} = {left} {op} {right};\n"
            elif parts[0] == "PRINT":
                table_index = int(parts[1])
                entries = self.print_table.get_entries_by_index(table_index)
                if entries:
                    print_statement = "    printf(\""
                    for value, tipo in entries:
                        if tipo == "qaytu":
                            print_statement += f"{value} "
                        elif tipo == "yupay":
                            print_statement += f"%d "
                        elif tipo == "chunkayuq":
                            print_statement += f"%f "
                        elif tipo == "sananpa":
                            print_statement += f"%c "
                        elif tipo == "bool":
                            print_statement += f"%s "
                    print_statement = print_statement.rstrip() + "\\n\", "
                    for value, tipo in entries:
                        if tipo == "yupay" or tipo == "chunkayuq":
                            print_statement += f"{value}, "
                        elif tipo == "sananpa":
                            print_statement += f"'{value}', "
                        elif tipo == "bool":
                            if value == "yanqa":
                                print_statement += "\"true\", "
                            elif value == "chiqaq":
                                print_statement += "\"false\", "
                    print_statement = print_statement.rstrip(', ') + ");\n"
                    c_code += print_statement
            elif parts[0] == "IF" and parts[3] == "GOTO":
                condition = parts[2]
                label = parts[4]
                c_code += f"    if (!{condition}) goto {label};\n"
            
            # Traducción de saltos: GOTO <etiqueta>
            elif parts[0] == "GOTO":
                label = parts[1]
                c_code += f"    goto {label};\n"
            
            # Traducción de etiquetas: <etiqueta>:
            elif parts[0].endswith(":"):
                label = parts[0]
                c_code += f"{label}\n"
        c_code += """
    return 0;
}
"""
        self.c_code = c_code

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            file.write(self.c_code)