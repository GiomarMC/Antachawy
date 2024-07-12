epsilon = "ε"
grammar = """
Programa -> Definicion
Definicion -> qhapaq ( ) newline lbrace newline ListaSentencias rbrace
ListaSentencias -> Sentencias ListaSentencias | ε
Sentencias -> Declaraciones newline
		| Asignaciones newline
		| Impresiones newline
Declaraciones -> Tipo id DeclaracionesPrime
DeclaracionesPrime -> asignacion Expresion | ε
Asignaciones -> id asignacion Expresion
Impresiones -> siqiy ( ExpresionImpresion )
Tipo -> yupay
	| chunkayuq
	| sananpa
	| qaytu 
    | bool
Expresion -> Termino ExpresionPrime
ExpresionPrime -> Operador Termino ExpresionPrime
        | ε
Operador -> + | menos | * | /
Termino -> ( Expresion ) 
	| id
	| numero
	| flotante
	| caracter
	| cadena
    | chinqaq
    | yanqa
ExpresionImpresion -> Expresion ExpresionImpresionPrime
ExpresionImpresionPrime -> coma ExpresionImpresion
			| ε
"""