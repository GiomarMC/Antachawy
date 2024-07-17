from antachawy.scanner import Scanner
from antachawy.parser import RecursiveDescentParser
from antachawy.consolehandler import ConsoleHandler
from antachawy.semantic import SemanticAnalyzer
from antachawy.intermediate import IntermediateCodeGenerator

class Compiler:
    def __init__(self, source_code: str):
        self.source_code = source_code
        self.scanner = Scanner()
        self.parser = None
        self.console_handler = ConsoleHandler()

    def compile(self):
        tokens = self.scanner.tokenize(self.source_code)
        lex_errors = self.scanner.errors

        self.console_handler.scan_debug_table(tokens)
        if lex_errors:
            print("--> Lexical Analysis Failed")
            self.console_handler.show_errors(lex_errors)
            return False
        
        print("--> Lexical Analysis Passed")

        self.parser = RecursiveDescentParser(self.scanner)
        tree = self.parser.parse()
        parse_errors = self.parser.errors

        if parse_errors:
            self.console_handler.show_errors(parse_errors)
            return False
        
        print("--> Syntax Analysis Passed")

        analyzer = SemanticAnalyzer()
        analyzer.analyze(tree)
        if analyzer.errors:
            for error in analyzer.errors:
                print(error)
            return False
        
        print("--> Semantic Analysis Passed")
        generator = IntermediateCodeGenerator()
        intermediate_code = generator.generate(tree)
        for instruction in intermediate_code:
            print(instruction)

        return True