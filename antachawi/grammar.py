epsilon = "ε"
grammar = """
Programa -> Definicion
Definicion -> qhapaq ( ) newline lbrace newline ListaSentencias rbrace
ListaSentencias -> Sentencias ListaSentenciasPrime
ListaSentenciasPrime -> ListaSentencias | ε
Sentencias -> Declaraciones newline
            | Asignaciones newline
		| Condicional newline
            | Impresiones newline
Declaraciones -> Tipo id DeclaracionesPrime
DeclaracionesPrime -> asignacion Expresion | ε
Asignaciones -> id asignacion Expresion
Condicional -> ari (ExpresionCondicion) newline lbrace newline ListaSentencias rbrace newline CondicionalPrime
CondicionalPrime -> mana_chayqa_ari (ExpresionCondicion) newline lbrace newline ListaSentencias rbrace newline CondicionalPrime
					| mana_chayqa newline lbrace newline ListaSentencias rbrace newline
					| ε
Impresiones -> rikuchiy ( ExpresionImpresion )
Tipo -> yupay
      | chunkayuq
      | sananpa
      | qaytu 
      | bool
Expresion -> ExpresionMultiplicativa ExpresionAditivaPrime
ExpresionAditivaPrime -> OperadorAditivo ExpresionMultiplicativa ExpresionAditivaPrime | ε
ExpresionMultiplicativa -> Termino ExpresionMultiplicativaPrime
ExpresionMultiplicativaPrime -> OperadorMultiplicativo Termino ExpresionMultiplicativaPrime | ε
ExpresionCondicion -> ExpresionRelacional ExpresionCondicionPrime
ExpresionCondicionPrime -> OperadorLogico ExpresionCondicion | ε
ExpresionRelacional -> Termino OperadorRelacional Termino
OperadorAditivo -> + | menos
OperadorMultiplicativo -> * | /
OperadorRelacional -> mayor | menor | menorigual | mayorigual | igual | diferente
OperadorLogico -> y | o
Termino -> ( Expresion ) 
         | id
         | numero
         | flotante
         | caracter
         | cadena
         | chinqaq
         | yanqa
ExpresionImpresion -> Expresion ExpresionImpresionPrime
ExpresionImpresionPrime -> coma ExpresionImpresion | ε
"""