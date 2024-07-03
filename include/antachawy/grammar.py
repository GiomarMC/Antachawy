grammar = """
<Programa> ::= <ListaDefiniciones> <Definicion>
<Programa> ::=  <Definicion>
<Definicion> ::= "qhapaq" "(" ")" "{" <Bloque> "}"
<Definicion> ::= "qhapaq" "(" ")" "{""}"
<Bloque> ::= <ListaCondiciones>
<Bloque> ::= <Declaraciones>
<Bloque> ::= "Siqiy" "(" <Expresion> ")"
<Bloque> ::= <Operaciones>
<ListaCondiciones> ::= <Condiciones> <ListaCondiciones>
<ListaCondiciones> ::= <Condiciones>
<Condiciones> ::= "ari" "(" <Condicion> ")" "{" <Bloque> "}" <CondicionesElseif> <CondicionElse>
<Condiciones> ::= "ari" "(" <Condicion> ")" "{" <Bloque> "}" <CondicionElse>
<Condiciones> ::= "ari" "(" <Condicion> ")" "{" <Bloque> "}"
<Condiciones> ::= <cicloFor>
<Condiciones> ::= <cicloWhile>
<cicloFor> ::= "for" "(" <Declaracion> ";" <Condicion> ";" <Operacion> ")" "{" <Bloque> "}"
<cicloWhile> ::= "while" "(" <Condicion> ")" "{" <Bloque> "}"
<CondicionesElseif> ::= <CondicionElseif> <CondicionesElseif>
<CondicionesElseif> ::= <CondicionElseif>
<CondicionElseif> ::= "mana_chayqa_ari" "(" <Condicion> ")" "{" <Bloque> "}"
<CondicionElse> ::= "mana_chayqa" "{" <Bloque> "}"
<Declaraciones> ::= <Declaracion> <Declaraciones>
<Declaraciones> ::= <Declaracion>
<Declaracion> ::= <Tipo> <Asignacion>
<Declaracion> ::= <Tipo> <Expresion>
<Operaciones> ::= <Operacion> <Operaciones>
<Operaciones> ::= <Operacion>
<Operacion> ::= ID "=" ID <Operador> ID
<Operacion> ::= ID "=" NUMERO <Operador> ID
<Operacion> ::= ID "=" ID <Operador> NUMERO
<Operacion> ::= ID "=" NUMERO <Operador> NUMERO
<Asignacion> ::= ID "=" <Expresion>
<Condicion> ::= <Expresion> <OperadorRelacional> <Expresion>
<Condicion> ::= <Expresion>
<Operador> ::= "+"
<Operador> ::= "-"
<Operador> ::= "*"
<Operador> ::= "/"
<OperadorRelacional> ::= ">"
<OperadorRelacional> ::= "<"
<OperadorRelacional> ::= "=="
<OperadorRelacional> ::= "!="
<OperadorRelacional> ::= "<="
<OperadorRelacional> ::= ">="
<Tipo> ::= "yupay"
<Tipo> ::= "chunkayuq"
<Tipo> ::= "sananpa"
<Tipo> ::= "qaytu"
<Tipo> ::= "bool"
<Retorno> ::= "cutichiy" "(" <Expresion> ")"
<Expresion> ::= <Expresion> <Operador> <Expresion>
<Expresion> ::= ID <Expresion>
<Expresion> ::= ID
<Expresion> ::= NUMERO <Expresion>
<Expresion> ::= NUMERO
<Expresion> ::= CADENA <Expresion>
<Expresion> ::= CADENA
<Expresion> ::= "yanqa" <Expresion>
<Expresion> ::= "yanqa"  //true
<Expresion> ::= "chiqaq" <Expresion>
<Expresion> ::= "chiqaq"  //false
"""