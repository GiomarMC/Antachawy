class IntermediateCodeOptimizer:
    def __init__(self, intermediate_code):
        self.intermediate_code = intermediate_code
        self.optimized_code = []
        self.constants = {}

    def optimize(self):
        self.propagate_constants()
        self.remove_dead_code()
        self.simplify_expressions()
        return self.optimized_code

    def propagate_constants(self):
        new_code = []
        for instruction in self.intermediate_code:
            parts = instruction.split()
            if len(parts) == 3:  # Asignación simple
                dest, _, src = parts
                if src.isdigit():  # Propagar constantes
                    self.constants[dest] = src
                    new_code.append(instruction)
                else:
                    if src in self.constants:
                        new_code.append(f"{dest} = {self.constants[src]}")
                    else:
                        new_code.append(instruction)
            elif len(parts) == 5:  # Operación binaria
                dest, _, left, op, right = parts
                if left in self.constants:
                    left = self.constants[left]
                if right in self.constants:
                    right = self.constants[right]
                new_code.append(f"{dest} = {left} {op} {right}")
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

    def simplify_expressions(self):
        for i, instruction in enumerate(self.optimized_code):
            parts = instruction.split()
            if len(parts) == 5:
                dest, _, left, op, right = parts
                if left.isdigit() and right.isdigit():
                    result = eval(f"{left} {op} {right}")
                    self.optimized_code[i] = f"{dest} = {result}"