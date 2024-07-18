from antachawy.scanner import Scanner
from antachawy.parser import RecursiveDescentParser
from antachawy.consolehandler import ConsoleHandler
from antachawy.semantic import SemanticAnalyzer
from antachawy.intermediate import IntermediateCodeGenerator
from antachawy.optimizer import IntermediateCodeOptimizer

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

        tree = self.perform_syntax_analysis(tokens)
        if not tree:
            return False

        if not self.perform_semantic_analysis(tree):
            return False

        code = self.generate_intermediate_code(tree)
        self.optimize_intermediate_code(code)
        return True

    def perform_lexical_analysis(self):
        tokens = self.scanner.tokenize(self.source_code)
        lex_errors = self.scanner.errors

        self.console_handler.scan_debug_table(tokens)
        if lex_errors:
            print("--> Lexical Analysis Failed")
            self.console_handler.show_errors(lex_errors)
            return None

        print("--> Lexical Analysis Passed")
        return tokens

    def perform_syntax_analysis(self, tokens):
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
        if code:
            for cod in code:
                print(cod)
        print("--> Generated Intermediate Code")
        return code
    
    def optimize_intermediate_code(self, code):
        optimizer = IntermediateCodeOptimizer(code)
        codigo = optimizer.optimize()
        for cod in codigo:
            print(cod)
        return True