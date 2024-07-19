from antachawy.scanner import Scanner
from antachawy.parser import RecursiveDescentParser
from antachawy.consolehandler import ConsoleHandler
from antachawy.semantic import SemanticAnalyzer
from antachawy.intermediate import IntermediateCodeGenerator
from antachawy.optimizer import IntermediateCodeOptimizer
from antachawy.assembler import AssemblyCodeGenerator
from antachawy.traductor_c import CodeTranslator
import subprocess
import os

class Compiler:
    def __init__(self, source_code: str):
        self.source_code = source_code
        self.scanner = Scanner()
        self.parser = None
        self.console_handler = ConsoleHandler()

    def compile(self):
        tokens = self.perform_lexical_analysis()
        if not tokens:
            return False

        tree = self.perform_syntax_analysis()
        if not tree:
            return False
        
        if not self.perform_semantic_analysis(tree):
            return False

        code = self.generate_intermediate_code(tree)
        codigo = self.optimize_intermediate_code(code)
        #self.generate_assembly_code(codigo)
        self.translate_to_c(codigo)
        self.compile_c_code("programa.c", "programa")
        return True

    def perform_lexical_analysis(self):
        tokens = self.scanner.tokenize(self.source_code)
        lex_errors = self.scanner.errors
        if lex_errors:
            print("--> Lexical Analysis Failed")
            self.console_handler.show_errors(lex_errors)
            return None
        print("--> Lexical Analysis Passed")
        return tokens

    def perform_syntax_analysis(self):
        self.parser = RecursiveDescentParser(self.scanner)
        tree = self.parser.parse()
        parse_errors = self.parser.errors
        if parse_errors:
            self.console_handler.show_errors(parse_errors)
            return None
        print("--> Syntax Analysis Passed")
        return tree

    def perform_semantic_analysis(self, tree):
        analyzer = SemanticAnalyzer()
        analyzer.analyze(tree)
        if analyzer.errors:
            for error in analyzer.errors:
                print(error)
            return False
        print("--> Semantic Analysis Passed")
        return True

    def generate_intermediate_code(self, tree):
        generator = IntermediateCodeGenerator()
        code = generator.analyze(tree)
        print("--> Generated Intermediate Code")
        return code
    
    def optimize_intermediate_code(self, code):
        optimizer = IntermediateCodeOptimizer(code)
        codigo = optimizer.optimize()
        print("--> Optimized Intermediate Code")
        return codigo
    
    """
    def generate_assembly_code(self, code):
        generator = AssemblyCodeGenerator(code)
        generator.save_to_file("programa.asm")
        print("--> Generated Assembly Code")
        return True
    """

    def translate_to_c(self, optimized_code):
        translator = CodeTranslator(optimized_code)
        translator.translate_to_c()
        translator.save_to_file("programa.c")
        print("--> Translated to C")
        return True
    
    def compile_c_code(self, source_file, output_file):
        try:
            compile_command = ["gcc", source_file, "-o", output_file]
            result = subprocess.run(compile_command, check=True, capture_output=True, text=True)
            print(f"--> Compilation successful. Executable created: {output_file}")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"--> Error during compilation: {e.stderr}")