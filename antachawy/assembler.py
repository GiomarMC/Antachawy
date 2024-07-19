class AssemblyCodeGenerator:
    def __init__(self, optimized_code):
        self.optimized_code = optimized_code
        self.assembly_code = []
        self.data_section = ["section .data"]
        self.bss_section = ["section .bss"]
        self.string_counter = 0
        self.variables = set()

    def generate(self):
        self.declare_bss_section()
        self.assembly_code.append("section .text")
        self.assembly_code.append("global _start")
        self.assembly_code.append("_start:")

        for instruction in self.optimized_code:
            parts = instruction.split()
            if len(parts) == 3:
                dest, _, src = parts
                self.variables.add(dest)
                if src.isdigit():
                    self.assembly_code.append(f"    mov qword [{dest}], {src}")
                elif src.isalpha():
                    self.assembly_code.append(f"    mov rax, qword [{src}]")
                    self.assembly_code.append(f"    mov qword [{dest}], rax")
            elif len(parts) == 5:
                dest, _, left, op, right = parts
                self.variables.add(dest)
                self.handle_arithmetic_operation(dest, left, op, right)
            elif "PRINT" in instruction:
                self.handle_print_instruction(instruction)

        self.append_exit_code()
        self.append_print_functions()

        return "\n".join(self.data_section + self.bss_section + self.assembly_code)

    def declare_bss_section(self):
        for var in self.variables:
            self.bss_section.append(f"{var} resq 1")

    def handle_arithmetic_operation(self, dest, left, op, right):
        if left.isdigit():
            self.assembly_code.append(f"    mov rax, {left}")
        else:
            self.assembly_code.append(f"    mov rax, qword [{left}]")

        if right.isdigit():
            self.assembly_code.append(f"    mov rbx, {right}")
        else:
            self.assembly_code.append(f"    mov rbx, qword [{right}]")

        if op == '*':
            self.assembly_code.append("    imul rax, rbx")
        elif op == '+':
            self.assembly_code.append("    add rax, rbx")
        elif op == '-':
            self.assembly_code.append("    sub rax, rbx")
        elif op == '/':
            self.assembly_code.append("    cqo")
            self.assembly_code.append("    idiv rbx")

        self.assembly_code.append(f"    mov qword [{dest}], rax")

    def handle_print_instruction(self, instruction):
        parts = instruction.split(' ', 1)
        if len(parts) > 1:
            text = parts[1].strip()
            if text.isdigit():
                self.assembly_code.append(f"    mov rax, {text}")
                self.assembly_code.append("    call print_int")
            elif text.isalpha():
                self.assembly_code.append(f"    mov rax, qword [{text}]")
                self.assembly_code.append("    call print_int")
            else:
                label = f"str_{self.string_counter}"
                self.string_counter += 1
                self.data_section.append(f"{label} db '{text}', 0")
                self.assembly_code.append(f"    mov rdi, {label}")
                self.assembly_code.append("    call print_string")

    def append_exit_code(self):
        self.assembly_code.append("    mov rax, 60")  # syscall: exit
        self.assembly_code.append("    xor rdi, rdi")  # exit code 0
        self.assembly_code.append("    syscall")

    def append_print_functions(self):
        self.assembly_code.append("print_int:")
        self.assembly_code.append("    ; Save registers")
        self.assembly_code.append("    push rbx")
        self.assembly_code.append("    push rcx")
        self.assembly_code.append("    push rdx")
        self.assembly_code.append("    mov rbx, 10")
        self.assembly_code.append("    xor rcx, rcx")
        self.assembly_code.append("print_int_loop:")
        self.assembly_code.append("    xor rdx, rdx")
        self.assembly_code.append("    div rbx")
        self.assembly_code.append("    add dl, '0'")
        self.assembly_code.append("    push rdx")
        self.assembly_code.append("    inc rcx")
        self.assembly_code.append("    test rax, rax")
        self.assembly_code.append("    jnz print_int_loop")
        self.assembly_code.append("print_int_print:")
        self.assembly_code.append("    pop rax")
        self.assembly_code.append("    mov [rsp-1], al")
        self.assembly_code.append("    sub rsp, 1")
        self.assembly_code.append("    mov rdi, rsp")
        self.assembly_code.append("    mov rsi, rcx")
        self.assembly_code.append("    call print_string")
        self.assembly_code.append("    add rsp, rcx")
        self.assembly_code.append("    ; Restore registers")
        self.assembly_code.append("    pop rdx")
        self.assembly_code.append("    pop rcx")
        self.assembly_code.append("    pop rbx")
        self.assembly_code.append("    ret")

        self.assembly_code.append("print_string:")
        self.assembly_code.append("    ; Assume RDI points to the string")
        self.assembly_code.append("    mov rax, 1")  # syscall: write
        self.assembly_code.append("    mov rdi, 1")  # file descriptor: stdout
        self.assembly_code.append("    mov rsi, rdi")  # message to write
        self.assembly_code.append("    mov rdx, rsi")  # message length
        self.assembly_code.append("    syscall")
        self.assembly_code.append("    ret")

    def save_to_file(self, filename):
        assembly_code = self.generate()
        with open(filename, 'w') as file:
            file.write(assembly_code)
        print(f"Assembly code saved to {filename}")