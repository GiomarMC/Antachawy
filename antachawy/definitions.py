class LexemasAntachawy:
    QHAPAQ = "qhapaq"                           # main
    YUPAY = "yupay"                             # int
    CHUNKAYUQ = "chunkayuq"                     # float
    SANANPA = "sananpa"                         # char
    QAYTU = "qaytu"                             # string
    BOOL = "bool"                               # bool
    ARI = "ari"                                 # if
    MANA_CHAYQA_ARI = "mana_chayqa_ari"         # else if
    MANA_CHAYQA = "mana_chayqa"                 # else
    SIQIY = "Siqiy"                             # print
    IMAPAQ = "imapaq"                           # for
    CHAYKAMA = "chaykama"                       # while
    YANQA = "yanqa"                             # true
    CHIQAQ = "chiqaq"                           # false
    CUTICHIY = "cutichiy"                       # return
    LLAVE_IZQ = "{"                             # {
    LLAVE_DER = "}"                             # }
    PAREN_IZQ = "("                             # (
    PAREN_DER = ")"                             # )
    COMA = ","                                  # ,
    PUNTOYCOMA = ";"                            # ;
    MAS = "+"                                   # +
    MENOS = "-"                                 # -
    MULTIPLICA = "*"                            # *
    DIVIDE = "/"                                # /
    DIVISIONEXACTA = "//"                       # //
    ASIGNA = "="                                # =
    MAYOR = ">"                                 # >
    MENOR = "<"                                 # <
    IGUAL = "=="                                # ==
    DIFERENTE = "!="                            # !=
    MAYOR_IGUAL = ">="                          # >=
    MENOR_IGUAL = "<="                          # <=
    NUMERO = "NUMERO"                           # numero
    CADENA = "CADENA"                           # cadena
    ID = "ID"                                   # identificador

class EtiquetasAntachawy:
    TIPO_YUPAY = "TIPOENTERO"
    TIPO_CHUNKAYUQ = "TIPOFLOAT"
    TIPO_SANANPA = "TIPOCHAR"
    TIPO_QAYTU = "TIPOSTRING"
    TIPO_BOOL = "TIPOBOOL"
    ASIGNACION = "ASIGNACION"
    CONDICION_ARI = "CONDICION_IF"
    CONDICION_MANA_CHAYQA_ARI = "CONDICION_ELSEIF"
    CONDICION_MANA_CHAYQA = "CONDICION_ELSE"
    OPERADOR_ARITMETICO = "OPERADOR_ARITMETICO"
    OPERADOR_RACIONAL = "OPERADOR_RACIONAL"
    IMPRESION = "IMPRESION"
    BUCLE_FOR = "BUCLE_FOR"
    BUCLE_WHILE = "BUCLE_WHILE"
    BLOQUE = "BLOQUE"
    LLAVE_IZQ = "LLAVE_IZQ"
    LLAVE_DER = "LLAVE_DER"
    PAREN_IZQ = "PAREN_IZQ"
    PAREN_DER = "PAREN_DER"
    COMA = "COMA"
    PUNTOYCOMA = "PUNTOYCOMA"
    PROGRAMA = "PROGRAMA"
    NUMERO = "NUMERO"
    CADENA = "CADENA"
    ID = "ID"

lexema_a_etiqueta = {
    LexemasAntachawy.QHAPAQ:            EtiquetasAntachawy.PROGRAMA,
    LexemasAntachawy.YUPAY:             EtiquetasAntachawy.TIPO_YUPAY,
    LexemasAntachawy.CHUNKAYUQ:         EtiquetasAntachawy.TIPO_CHUNKAYUQ,
    LexemasAntachawy.SANANPA:           EtiquetasAntachawy.TIPO_SANANPA,
    LexemasAntachawy.QAYTU:             EtiquetasAntachawy.TIPO_QAYTU,
    LexemasAntachawy.ASIGNA:            EtiquetasAntachawy.ASIGNACION,
    LexemasAntachawy.ARI:               EtiquetasAntachawy.CONDICION_ARI,
    LexemasAntachawy.MANA_CHAYQA_ARI:   EtiquetasAntachawy.CONDICION_MANA_CHAYQA_ARI,
    LexemasAntachawy.MANA_CHAYQA:       EtiquetasAntachawy.CONDICION_MANA_CHAYQA,
    LexemasAntachawy.SIQIY:             EtiquetasAntachawy.IMPRESION,
    LexemasAntachawy.IMAPAQ:            EtiquetasAntachawy.BUCLE_FOR,
    LexemasAntachawy.CHAYKAMA:          EtiquetasAntachawy.BUCLE_WHILE,
    LexemasAntachawy.LLAVE_IZQ:         EtiquetasAntachawy.LLAVE_IZQ,
    LexemasAntachawy.LLAVE_DER:         EtiquetasAntachawy.LLAVE_DER,
    LexemasAntachawy.PAREN_IZQ:         EtiquetasAntachawy.PAREN_IZQ,
    LexemasAntachawy.PAREN_DER:         EtiquetasAntachawy.PAREN_DER,
    LexemasAntachawy.COMA:              EtiquetasAntachawy.COMA,
    LexemasAntachawy.PUNTOYCOMA:        EtiquetasAntachawy.PUNTOYCOMA,
    LexemasAntachawy.YANQA:             EtiquetasAntachawy.TIPO_BOOL,
    LexemasAntachawy.CHIQAQ:            EtiquetasAntachawy.TIPO_BOOL,
    LexemasAntachawy.MAS:               EtiquetasAntachawy.OPERADOR_ARITMETICO,
    LexemasAntachawy.MENOS:             EtiquetasAntachawy.OPERADOR_ARITMETICO,
    LexemasAntachawy.MULTIPLICA:        EtiquetasAntachawy.OPERADOR_ARITMETICO,
    LexemasAntachawy.DIVIDE:            EtiquetasAntachawy.OPERADOR_ARITMETICO,
    LexemasAntachawy.MAYOR:             EtiquetasAntachawy.OPERADOR_RACIONAL,
    LexemasAntachawy.MENOR:             EtiquetasAntachawy.OPERADOR_RACIONAL,
    LexemasAntachawy.IGUAL:             EtiquetasAntachawy.OPERADOR_RACIONAL,
    LexemasAntachawy.DIFERENTE:         EtiquetasAntachawy.OPERADOR_RACIONAL,
    LexemasAntachawy.MAYOR_IGUAL:       EtiquetasAntachawy.OPERADOR_RACIONAL,
    LexemasAntachawy.MENOR_IGUAL:       EtiquetasAntachawy.OPERADOR_RACIONAL,
    LexemasAntachawy.NUMERO:            EtiquetasAntachawy.NUMERO,
    LexemasAntachawy.CADENA:            EtiquetasAntachawy.CADENA,
    LexemasAntachawy.ID:                EtiquetasAntachawy.ID
}

simbolos_compuestos = {
    "==": EtiquetasAntachawy.OPERADOR_RACIONAL,
    "!=": EtiquetasAntachawy.OPERADOR_RACIONAL,
    "<=": EtiquetasAntachawy.OPERADOR_RACIONAL,
    ">=": EtiquetasAntachawy.OPERADOR_RACIONAL
}

primeros = {
    "Programa": [LexemasAntachawy.QHAPAQ],
    "Definicion": [LexemasAntachawy.QHAPAQ],
    "Bloque": [
        LexemasAntachawy.ARI,
        LexemasAntachawy.IMAPAQ,
        LexemasAntachawy.CHAYKAMA,
        LexemasAntachawy.YUPAY,
        LexemasAntachawy.CHUNKAYUQ,
        LexemasAntachawy.SANANPA,
        LexemasAntachawy.QAYTU,
        LexemasAntachawy.BOOL,
        LexemasAntachawy.SIQIY,
        LexemasAntachawy.ID
    ],
    "ListaCondiciones": [
        LexemasAntachawy.ARI,
        LexemasAntachawy.IMAPAQ,
        LexemasAntachawy.CHAYKAMA
    ],
    "Condiciones": [
        LexemasAntachawy.ARI,
        LexemasAntachawy.IMAPAQ,
        LexemasAntachawy.CHAYKAMA
    ],
    "CondicionesElseif": [LexemasAntachawy.MANA_CHAYQA_ARI],
    "CondicionElseif": [LexemasAntachawy.MANA_CHAYQA_ARI],
    "CondicionElse": [LexemasAntachawy.MANA_CHAYQA],
    "Declaraciones": [
        LexemasAntachawy.YUPAY,
        LexemasAntachawy.CHUNKAYUQ,
        LexemasAntachawy.SANANPA,
        LexemasAntachawy.QAYTU,
        LexemasAntachawy.BOOL
    ],
    "Declaracion": [
        LexemasAntachawy.YUPAY,
        LexemasAntachawy.CHUNKAYUQ,
        LexemasAntachawy.SANANPA,
        LexemasAntachawy.QAYTU,
        LexemasAntachawy.BOOL
    ],
    "Operaciones": [LexemasAntachawy.ID],
    "Operacion": [LexemasAntachawy.ID],
    "Asignacion": [LexemasAntachawy.ID],
    "Condicion": [
        LexemasAntachawy.ID,
        LexemasAntachawy.NUMERO,
        LexemasAntachawy.CADENA,
        LexemasAntachawy.YANQA,
        LexemasAntachawy.CHIQAQ
    ],
    "Operador": [
        LexemasAntachawy.MAS,
        LexemasAntachawy.MENOS,
        LexemasAntachawy.MULTIPLICA,
        LexemasAntachawy.DIVIDE
    ],
    "OperadorRelacional": [
        LexemasAntachawy.MAYOR,
        LexemasAntachawy.MENOR,
        LexemasAntachawy.IGUAL,
        LexemasAntachawy.DIFERENTE,
        LexemasAntachawy.MAYOR_IGUAL,
        LexemasAntachawy.MENOR_IGUAL
    ],
    "Tipo": [
        LexemasAntachawy.YUPAY,
        LexemasAntachawy.CHUNKAYUQ,
        LexemasAntachawy.SANANPA,
        LexemasAntachawy.QAYTU,
        LexemasAntachawy.BOOL
    ],
    "Expresion": [
        LexemasAntachawy.ID,
        LexemasAntachawy.NUMERO,
        LexemasAntachawy.CADENA,
        LexemasAntachawy.YANQA,
        LexemasAntachawy.CHIQAQ
    ],
}

producciones = {
    "Programa": [
        ["Definicion"]
    ],
    "Definicion": [
        [LexemasAntachawy.QHAPAQ, LexemasAntachawy.PAREN_IZQ, LexemasAntachawy.PAREN_DER,
          LexemasAntachawy.LLAVE_IZQ, "Bloque", LexemasAntachawy.LLAVE_DER],
        [LexemasAntachawy.QHAPAQ, LexemasAntachawy.PAREN_IZQ, LexemasAntachawy.PAREN_DER,
          LexemasAntachawy.LLAVE_IZQ, LexemasAntachawy.LLAVE_DER]
    ],
    "Bloque": [
        ["ListaCondiciones"],
        ["Declaraciones"],
        ["Operaciones"],
        [LexemasAntachawy.SIQIY, LexemasAntachawy.PAREN_IZQ, "Expresion", LexemasAntachawy.PAREN_DER]
    ],
    "ListaCondiciones": [
        ["Condiciones", "ListaCondiciones"],
        ["Condiciones"]
    ],
    "Condiciones": [
        [LexemasAntachawy.ARI, LexemasAntachawy.PAREN_IZQ, "Condicion", LexemasAntachawy.PAREN_DER, 
         LexemasAntachawy.LLAVE_IZQ, "Bloque", LexemasAntachawy.LLAVE_DER, "CondicionesElseif", "CondicionElse"], 
        [LexemasAntachawy.ARI, LexemasAntachawy.PAREN_IZQ, "Condicion", LexemasAntachawy.PAREN_DER,
          LexemasAntachawy.LLAVE_IZQ, "Bloque", LexemasAntachawy.LLAVE_DER, "CondicionElse"],
        [LexemasAntachawy.ARI, LexemasAntachawy.PAREN_IZQ, "Condicion", LexemasAntachawy.PAREN_DER,
          LexemasAntachawy.LLAVE_IZQ, "Bloque", LexemasAntachawy.LLAVE_DER],
        ["CicloFor"], 
        ["CicloWhile"]
    ],
    "CicloFor": [
        "For", LexemasAntachawy.PAREN_IZQ,
          "Declaracion", LexemasAntachawy.PUNTOYCOMA, "Condicion", LexemasAntachawy.PUNTOYCOMA, "Operacion", 
          LexemasAntachawy.PAREN_DER, LexemasAntachawy.LLAVE_IZQ, "Bloque", LexemasAntachawy.LLAVE_DER],
    "CicloWhile": [
        "While", LexemasAntachawy.PAREN_IZQ, 
        "Condicion", LexemasAntachawy.PAREN_DER, LexemasAntachawy.LLAVE_IZQ, "Bloque", LexemasAntachawy.LLAVE_DER],
    "CondicionesElseif": [
        ["CondicionElseif", "CondicionesElseif"],
        ["CondicionElseif"]
    ],
    "CondicionElseif": [LexemasAntachawy.MANA_CHAYQA_ARI, LexemasAntachawy.PAREN_IZQ, 
                        "Condicion", LexemasAntachawy.PAREN_DER, LexemasAntachawy.LLAVE_IZQ, "Bloque", LexemasAntachawy.LLAVE_DER],
    "CondicionElse": [LexemasAntachawy.MANA_CHAYQA, LexemasAntachawy.LLAVE_IZQ, "Bloque", LexemasAntachawy.LLAVE_DER],
    "Declaraciones": [
        ["Declaracion", "Declaraciones"],
        ["Declaracion"]
    ],
    "Declaracion": [
        ["Tipo", "Asignacion"],
        ["Tipo", "Expresion"]
    ],
    "Operaciones": [
        ["Operacion", "Operaciones"],
        ["Operacion"]
    ],
    "Operacion": [
        [LexemasAntachawy.ID, "Assign", LexemasAntachawy.ID, "Operador", LexemasAntachawy.ID],
        [LexemasAntachawy.ID, "Assign", "NUMERO", "Operador", LexemasAntachawy.ID],
        [LexemasAntachawy.ID, "Assign", LexemasAntachawy.ID, "Operador", "NUMERO"],
        [LexemasAntachawy.ID, "Assign", "NUMERO", "Operador", "NUMERO"]
    ],
    "Asignacion": [LexemasAntachawy.ID, "Assign", "Expresion"],
    "Condicion": [
        ["Expresion", "OperadorRelacional", "Expresion"],
        ["Expresion"]
    ],
    "Operador": [
        [LexemasAntachawy.MAS],
        [LexemasAntachawy.MENOS],
        [LexemasAntachawy.MULTIPLICA],
        [LexemasAntachawy.DIVIDE]
    ],
    "OperadorRelacional": [
        [LexemasAntachawy.MAYOR],
        [LexemasAntachawy.MENOR],
        [LexemasAntachawy.IGUAL],
        [LexemasAntachawy.DIFERENTE],
        [LexemasAntachawy.MAYOR_IGUAL],
        [LexemasAntachawy.MENOR_IGUAL]
    ],
    "Tipo": [
        [LexemasAntachawy.YUPAY],
        [LexemasAntachawy.CHUNKAYUQ],
        [LexemasAntachawy.SANANPA],
        [LexemasAntachawy.QAYTU],
        [LexemasAntachawy.BOOL]
    ],
    "Expresion": [
        [LexemasAntachawy.ID, "ExpresionPrime"],
        [LexemasAntachawy.NUMERO, "ExpresionPrime"],
        [LexemasAntachawy.CADENA, "ExpresionPrime"], 
        [LexemasAntachawy.YANQA, "ExpresionPrime"],
        [LexemasAntachawy.CHIQAQ, "ExpresionPrime"]
    ],
    "ExpresionPrime": [
        ["Operador", "Expresion", "ExpresionPrime"]
    ],
    "For": [LexemasAntachawy.IMAPAQ],
    "While": [LexemasAntachawy.CHAYKAMA],
    "Assign": [LexemasAntachawy.ASIGNA],
    "NUMERO": [LexemasAntachawy.NUMERO],
}