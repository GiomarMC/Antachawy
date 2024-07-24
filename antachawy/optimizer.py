import os

class IntermediateCodeOptimizer:
    def __init__(self, intermediate_code, combine_prints=False):
        self.intermediate_code = intermediate_code
        self.optimized_code = []
        self.constants = {}
        self.copies = {}
        self.combine_prints = combine_prints

    def optimize(self):
        self.propagate_constants_and_copies()
        self.remove_dead_code()
        self.simplify_expressions()
        if self.combine_prints:
            self.combine_prints_instructions()
        return self.optimized_code

    def propagate_constants_and_copies(self):
        new_code = []
        print_index = 0
        for instruction in self.intermediate_code:
            parts = instruction.split()
            if len(parts) == 3:
                dest, _, src = parts
                if src.isdigit() or (src.startswith("'") and src.endswith("'")):
                    self.constants[dest] = src
                    new_code.append(instruction)
                elif src in self.constants:
                    new_code.append(f"{dest} = {self.constants[src]}")
                else:
                    self.copies[dest] = src
                    new_code.append(instruction)
            elif len(parts) == 5:
                dest, _, left, op, right = parts
                if left in self.constants:
                    left = self.constants[left]
                if right in self.constants:
                    right = self.constants[right]
                new_code.append(f"{dest} = {left} {op} {right}")
            elif parts[0] == "PRINT":
                new_code.append(f"PRINT {print_index}")
                print_index += 1
        self.intermediate_code = new_code

    def remove_dead_code(self):
        used_vars = set()
        for instruction in reversed(self.intermediate_code):
            parts = instruction.split()
            if len(parts) == 3:
                dest, _, src = parts
                if dest in used_vars or src in used_vars:
                    self.optimized_code.insert(0, instruction)
                used_vars.add(dest)
                used_vars.add(src)
            elif len(parts) == 5:
                dest, _, left, op, right = parts
                if dest in used_vars or left in used_vars or right in used_vars:
                    self.optimized_code.insert(0, instruction)
                used_vars.add(dest)
                used_vars.add(left)
                used_vars.add(right)
            elif parts[0] == "PRINT":
                var_to_print = parts[1]
                if var_to_print in self.constants:
                    self.optimized_code.insert(0, f"PRINT {self.constants[var_to_print]}")
                else:
                    self.optimized_code.insert(0, instruction)
                used_vars.add(var_to_print)

    def simplify_expressions(self):
        for i, instruction in enumerate(self.optimized_code):
            parts = instruction.split()
            if len(parts) == 5:
                dest, _, left, op, right = parts
                if left.isdigit() and right.isdigit():
                    result = eval(f"{left} {op} {right}")
                    self.optimized_code[i] = f"{dest} = {result}"

    def combine_prints_instructions(self):
        combined_print = ""
        new_code = []
        for instruction in self.optimized_code:
            if instruction.startswith("PRINT"):
                parts = instruction.split(" ", 1)
                if len(parts) > 1:
                    if combined_print:
                        combined_print += " " + parts[1]
                    else:
                        combined_print = parts[1]
            else:
                if combined_print:
                    new_code.append(f'PRINT "{combined_print.strip()}"')
                    combined_print = ""
                new_code.append(instruction)
        if combined_print:
            new_code.append(f'PRINT "{combined_print.strip()}"')
        self.optimized_code = new_code

    def save_optimized_code(self, filename="optimized_code.txt"):
        os.makedirs("outputs/optimizer", exist_ok=True)
        filepath = os.path.join("outputs/optimizer", filename)
        with open(filepath, "w") as file:
            for line in self.optimized_code:
                file.write(line + "\n")