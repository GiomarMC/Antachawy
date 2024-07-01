grammar = """
Programa -> ListaDefiniciones ListaCondiciones
ListaDefiniciones -> Definicion ListaDefiniciones
ListaDefiniciones -> Definicion
Definicion -> "qhapaq" "("")" "{" Bloque "}"
Definicion -> "qhapaq" "("")" "{""}"
Bloque -> ListaCondiciones
Bloque -> Declaraciones
Bloque -> Operaciones
Bloque -> "Siqiy" "(" Expresion ")"
ListaCondiciones -> Condiciones ListaCondiciones
ListaCondiciones -> Condiciones
Condiciones -> "ari" "(" Condicion ")" "{" Bloque "}" CondicionesElseif CondicionElse
Condiciones -> "ari" "(" Condicion ")" "{" Bloque "}" CondicionElse
Condiciones -> "ari" "(" Condicion ")" "{" Bloque "}"
Condiciones -> cicloFor
Condiciones -> cicloWhile
cicloFor -> "for" "(" Declaracion ";" Condicion ";" Operacion ")" "{" Bloque "}"
cicloWhile -> "while" "(" Condicion ")" "{" Bloque "}"
CondicionesElseif -> CondicionElseif CondicionesElseif
CondicionesElseif -> CondicionElseif
CondicionElseif -> "mana chayqa ari" "(" Condicion ")" "{" Bloque "}"
CondicionElse -> "mana chayqa" "{" Bloque "}"
Declaraciones -> Declaracion Declaraciones
Declaraciones -> Declaracion
Declaracion -> Tipo Asignacion
Declaracion -> Tipo Expresion
Operaciones -> Operacion Operaciones
Operaciones -> Operacion
Operacion -> ID "=" ID Operador ID
Asignacion -> ID "=" Expresion
Condicion -> Expresion OperadorRelacional Expresion
Operador -> "+"
Operador -> "-"
Operador -> "*"
Operador -> "/"
OperadorRelacional -> ">"
OperadorRelacional -> "<"
OperadorRelacional -> "=="
OperadorRelacional -> "!="
OperadorRelacional -> "<="
OperadorRelacional -> ">="
Tipo -> "yupay"
Tipo -> "chunkayuq"
Tipo -> "sananpa"
Tipo -> "qaytu"
Retorno -> "cutichiy" "(" Expresion ")"
Expresion -> Expresion Operador Expresion
Expresion -> ID
Expresion -> NUMERO
Expresion -> Cadena
Expresion -> Expresion Cadena ID
Expresion -> Cadena ID
"""