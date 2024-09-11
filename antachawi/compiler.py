from antachawi.scanner import Scanner
from antachawi.parser import RecursiveDescentParser
from antachawi.consolehandler import ConsoleHandler
from antachawi.semantic import SemanticAnalyzer
from antachawi.intermediate import IntermediateCodeGenerator
from antachawi.optimizer import IntermediateCodeOptimizer
from antachawi.traductor_c import CodeTranslator
from antachawi.sourcecode import SourceCode
from antachawi.antachawy_translator import AntachawyToCppTranslator
import subprocess
import os
import platform

class Compiler:
    def __init__(self, source_code: str, output_file: str, debug: bool = False):
        self.source_code = source_code
        self.code = SourceCode(source_code)
        self.output_file = output_file if output_file else self.default_output_file()
        self.debug = debug
        self.scanner = Scanner(self.code)
        self.parser = None
        self.console_handler = ConsoleHandler()

    def default_output_file(self):
        system = platform.system()
        if system == "Windows":
            return "run.exe"
        else:
            return "run"

    def compile(self):
        tokens = self.perform_lexical_analysis()
        if not tokens:
            return False

        tree = self.perform_syntax_analysis()
        if not tree:
            return False
        
        if not self.perform_semantic_analysis(tree):
            return False
        self.translate_antachawy_to_c()
        self.compile_c_code("programa.cpp", self.output_file)
        return True

    def perform_lexical_analysis(self):
        tokens = self.scanner.tokenize(self.source_code)
        lex_errors = self.scanner.errors
        if lex_errors:
            print("--> Lexical Analysis Failed")
            self.console_handler.show_errors(lex_errors)
            return None
        print("--> Lexical Analysis Passed")
        if self.debug:
            self.scanner.save_tokens()
        return tokens

    def perform_syntax_analysis(self):
        self.parser = RecursiveDescentParser(self.scanner, self.code)
        tree = self.parser.parse()
        parse_errors = self.parser.errors
        if parse_errors:
            self.console_handler.show_errors(parse_errors)
            return None
        print("--> Syntax Analysis Passed")
        if self.debug:
            self.parser.save_syntax_outputs(tree, "outputs/sintactic/AbstractSyntaxTree")
        return tree

    def perform_semantic_analysis(self, tree):
        analyzer = SemanticAnalyzer(self.code)
        analyzer.analyze(tree)
        if analyzer.errors:
            self.console_handler.show_errors(analyzer.errors)
            return False
        print("--> Semantic Analysis Passed")
        if self.debug:
            analyzer.save_symbol_table()
            analyzer.save_print_table()
        return True

    def generate_intermediate_code(self, tree):
        generator = IntermediateCodeGenerator()
        code = generator.analyze(tree)
        print("--> Generated Intermediate Code")
        if self.debug:
            generator.save_intermediate_code()
            generator.save_symbol_table()
        return code
    
    def optimize_intermediate_code(self, code):
        optimizer = IntermediateCodeOptimizer(code)
        codigo = optimizer.optimize()
        print("--> Optimized Intermediate Code")
        if self.debug:
            optimizer.save_optimized_code()
        return codigo

    def translate_to_c(self, optimized_code):
        translator = CodeTranslator(optimized_code)
        translator.translate_to_c()
        translator.save_to_file("programa.c")
        print("--> Translated to C")
        return True
    
    def translate_antachawy_to_c(self):
        translator = AntachawyToCppTranslator(self.code)
        translated_code = translator.translate()
        translator.save_translated_code("programa.cpp")
        print("--> Translated to C++")
        return True
    
    def compile_c_code(self, source_file, output_file):
        try:
            compile_command = ["g++", source_file, "-o", output_file]
            result = subprocess.run(compile_command, check=True, capture_output=True, text=True)
            print(f"--> Compilation successful. Executable created: {output_file}")
            print(result.stdout)
            if not self.debug:
                os.remove(source_file)
        except subprocess.CalledProcessError as e:
            print(f"--> Error during compilation: {e.stderr}")