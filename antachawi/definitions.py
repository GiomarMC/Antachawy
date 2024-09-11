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
    RIKUCHIY = "rikuchiy"                       # print
    IMAPAQ = "imapaq"                           # for
    CHAYKAMA = "chaykama"                       # while
    YANQA = "yanqa"                             # true
    CHIQAQ = "chiqaq"                           # false
    CUTICHIY = "cutichiy"                       # return
    SALTO_LINEA = "\n"                          # salto de linea
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
    Y = "&&"                                    # &&
    O = "||"                                    # ||
    NUMEROENTERO = "entero"                     # numero
    NUMEROFLOTANTE = "flotante"                 # flotante
    CARACTER = "caracter"                       # caracter
    CADENA = "cadena"                           # cadena
    ID = "id"                                   # identificador

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
    MAS = "MAS"
    MENOS = "MENOS"
    MULTIPLICA = "MULTIPLICA"
    DIVIDE = "DIVIDE"
    IMPRESION = "IMPRESION"
    BUCLE_FOR = "BUCLE_FOR"
    BUCLE_WHILE = "BUCLE_WHILE"
    BLOQUE = "BLOQUE"
    SALTO_LINEA = "SALTO_LINEA"
    LLAVE_IZQ = "LLAVE_IZQ"
    LLAVE_DER = "LLAVE_DER"
    PAREN_IZQ = "PAREN_IZQ"
    PAREN_DER = "PAREN_DER"
    COMA = "COMA"
    PUNTOYCOMA = "PUNTOYCOMA"
    PROGRAMA = "PROGRAMA"
    NUMEROENTERO = "ENTERO"
    NUMEROFLOTANTE = "FLOTANTE"
    CARACTER = "CARACTER"
    CADENA = "CADENA"
    TRUE = "TRUE"
    FALSE = "FALSE"
    ID = "ID"
    MAYOR = "MAYOR"
    MENOR = "MENOR"
    IGUAL = "IGUAL"
    DIFERENTE = "DIFERENTE"
    MAYOR_IGUAL = "MAYOR_IGUAL"
    MENOR_IGUAL = "MENOR_IGUAL"
    Y = "OPERADOR_Y"
    O = "OPERADOR_O"

lexema_a_etiqueta = {
    LexemasAntachawy.QHAPAQ:            EtiquetasAntachawy.PROGRAMA,
    LexemasAntachawy.YUPAY:             EtiquetasAntachawy.TIPO_YUPAY,
    LexemasAntachawy.CHUNKAYUQ:         EtiquetasAntachawy.TIPO_CHUNKAYUQ,
    LexemasAntachawy.SANANPA:           EtiquetasAntachawy.TIPO_SANANPA,
    LexemasAntachawy.QAYTU:             EtiquetasAntachawy.TIPO_QAYTU,
    LexemasAntachawy.BOOL:              EtiquetasAntachawy.TIPO_BOOL,
    LexemasAntachawy.ASIGNA:            EtiquetasAntachawy.ASIGNACION,
    LexemasAntachawy.ARI:               EtiquetasAntachawy.CONDICION_ARI,
    LexemasAntachawy.MANA_CHAYQA_ARI:   EtiquetasAntachawy.CONDICION_MANA_CHAYQA_ARI,
    LexemasAntachawy.MANA_CHAYQA:       EtiquetasAntachawy.CONDICION_MANA_CHAYQA,
    LexemasAntachawy.RIKUCHIY:          EtiquetasAntachawy.IMPRESION,
    LexemasAntachawy.IMAPAQ:            EtiquetasAntachawy.BUCLE_FOR,
    LexemasAntachawy.CHAYKAMA:          EtiquetasAntachawy.BUCLE_WHILE,
    LexemasAntachawy.SALTO_LINEA:       EtiquetasAntachawy.SALTO_LINEA,
    LexemasAntachawy.LLAVE_IZQ:         EtiquetasAntachawy.LLAVE_IZQ,
    LexemasAntachawy.LLAVE_DER:         EtiquetasAntachawy.LLAVE_DER,
    LexemasAntachawy.PAREN_IZQ:         EtiquetasAntachawy.PAREN_IZQ,
    LexemasAntachawy.PAREN_DER:         EtiquetasAntachawy.PAREN_DER,
    LexemasAntachawy.COMA:              EtiquetasAntachawy.COMA,
    LexemasAntachawy.PUNTOYCOMA:        EtiquetasAntachawy.PUNTOYCOMA,
    LexemasAntachawy.YANQA:             EtiquetasAntachawy.TRUE,
    LexemasAntachawy.CHIQAQ:            EtiquetasAntachawy.FALSE,
    LexemasAntachawy.MAS:               EtiquetasAntachawy.MAS,
    LexemasAntachawy.MENOS:             EtiquetasAntachawy.MENOS,
    LexemasAntachawy.MULTIPLICA:        EtiquetasAntachawy.MULTIPLICA,
    LexemasAntachawy.DIVIDE:            EtiquetasAntachawy.DIVIDE,
    LexemasAntachawy.MAYOR:             EtiquetasAntachawy.MAYOR,
    LexemasAntachawy.MENOR:             EtiquetasAntachawy.MENOR,
    LexemasAntachawy.IGUAL:             EtiquetasAntachawy.IGUAL,
    LexemasAntachawy.DIFERENTE:         EtiquetasAntachawy.DIFERENTE,
    LexemasAntachawy.MAYOR_IGUAL:       EtiquetasAntachawy.MAYOR_IGUAL,
    LexemasAntachawy.MENOR_IGUAL:       EtiquetasAntachawy.MENOR_IGUAL,
    LexemasAntachawy.Y:                 EtiquetasAntachawy.Y,
    LexemasAntachawy.O:                 EtiquetasAntachawy.O,
    LexemasAntachawy.NUMEROENTERO:      EtiquetasAntachawy.NUMEROENTERO,
    LexemasAntachawy.NUMEROFLOTANTE:    EtiquetasAntachawy.NUMEROFLOTANTE,
    LexemasAntachawy.CARACTER:          EtiquetasAntachawy.CARACTER,
    LexemasAntachawy.CADENA:            EtiquetasAntachawy.CADENA,
    LexemasAntachawy.ID:                EtiquetasAntachawy.ID,
}

simbolos_compuestos = {
    "==": EtiquetasAntachawy.IGUAL,
    "!=": EtiquetasAntachawy.DIFERENTE,
    "<=": EtiquetasAntachawy.MENOR_IGUAL,
    ">=": EtiquetasAntachawy.MAYOR_IGUAL,
    "&&": EtiquetasAntachawy.Y,
    "||": EtiquetasAntachawy.O
}

primeros = {
    "Programa": [EtiquetasAntachawy.PROGRAMA],
    "Definicion": [EtiquetasAntachawy.PROGRAMA],
    "ListaSentencias": [
        "$",
        EtiquetasAntachawy.TIPO_YUPAY,
        EtiquetasAntachawy.TIPO_CHUNKAYUQ,
        EtiquetasAntachawy.TIPO_SANANPA,
        EtiquetasAntachawy.TIPO_QAYTU,
        EtiquetasAntachawy.TIPO_BOOL,
        EtiquetasAntachawy.IMPRESION,
        EtiquetasAntachawy.ID,
        EtiquetasAntachawy.CONDICION_ARI,
    ],
    "Sentencias": [
        EtiquetasAntachawy.TIPO_YUPAY,
        EtiquetasAntachawy.TIPO_CHUNKAYUQ,
        EtiquetasAntachawy.TIPO_SANANPA,
        EtiquetasAntachawy.TIPO_QAYTU,
        EtiquetasAntachawy.TIPO_BOOL,
        EtiquetasAntachawy.IMPRESION,
        EtiquetasAntachawy.ID,
        EtiquetasAntachawy.CONDICION_ARI,
    ],
    "Declaraciones": [
        EtiquetasAntachawy.TIPO_YUPAY,
        EtiquetasAntachawy.TIPO_CHUNKAYUQ,
        EtiquetasAntachawy.TIPO_SANANPA,
        EtiquetasAntachawy.TIPO_QAYTU,
        EtiquetasAntachawy.TIPO_BOOL
    ],
    "DeclaracionesPrime": [
        EtiquetasAntachawy.ASIGNACION,
        "$",
    ],
    "Asignaciones": [EtiquetasAntachawy.ID],
    "Condicional": [EtiquetasAntachawy.CONDICION_ARI],
    "CondicionalPrime": [
        EtiquetasAntachawy.CONDICION_MANA_CHAYQA_ARI,
        EtiquetasAntachawy.CONDICION_MANA_CHAYQA],
    "Impresiones": [EtiquetasAntachawy.IMPRESION],
    "Tipo": [
        EtiquetasAntachawy.TIPO_YUPAY,
        EtiquetasAntachawy.TIPO_CHUNKAYUQ,
        EtiquetasAntachawy.TIPO_SANANPA,
        EtiquetasAntachawy.TIPO_QAYTU,
        EtiquetasAntachawy.TIPO_BOOL
    ],
    "Expresion": [
        EtiquetasAntachawy.PAREN_IZQ,
        EtiquetasAntachawy.ID,
        EtiquetasAntachawy.NUMEROENTERO,
        EtiquetasAntachawy.NUMEROFLOTANTE,
        EtiquetasAntachawy.CARACTER,
        EtiquetasAntachawy.CADENA,
        EtiquetasAntachawy.TRUE,
        EtiquetasAntachawy.FALSE
    ],
    "ExpresionAditiva": [
        EtiquetasAntachawy.PAREN_IZQ,
        EtiquetasAntachawy.ID,
        EtiquetasAntachawy.NUMEROENTERO,
        EtiquetasAntachawy.NUMEROFLOTANTE,
        EtiquetasAntachawy.CARACTER,
        EtiquetasAntachawy.CADENA,
        EtiquetasAntachawy.TRUE,
        EtiquetasAntachawy.FALSE
    ],
    "ExpresionMultiplicativa": [
        EtiquetasAntachawy.PAREN_IZQ,
        EtiquetasAntachawy.ID,
        EtiquetasAntachawy.NUMEROENTERO,
        EtiquetasAntachawy.NUMEROFLOTANTE,
        EtiquetasAntachawy.CARACTER,
        EtiquetasAntachawy.CADENA,
        EtiquetasAntachawy.TRUE,
        EtiquetasAntachawy.FALSE
    ],
    "ExpresionCondicion": [
        EtiquetasAntachawy.PAREN_IZQ,
        EtiquetasAntachawy.ID,
        EtiquetasAntachawy.NUMEROENTERO,
        EtiquetasAntachawy.NUMEROFLOTANTE,
        EtiquetasAntachawy.CARACTER,
        EtiquetasAntachawy.CADENA,
        EtiquetasAntachawy.TRUE,
        EtiquetasAntachawy.FALSE
    ],
    "ExpresionCondicionPrime": [
        EtiquetasAntachawy.Y,
        EtiquetasAntachawy.O,
    ],
    "ExpresionOperadorRelacional": [
        EtiquetasAntachawy.PAREN_IZQ,
        EtiquetasAntachawy.ID,
        EtiquetasAntachawy.NUMEROENTERO,
        EtiquetasAntachawy.NUMEROFLOTANTE,
        EtiquetasAntachawy.CARACTER,
        EtiquetasAntachawy.CADENA,
        EtiquetasAntachawy.TRUE,
        EtiquetasAntachawy.FALSE
    ],
    "OperadorAditivo": [
        EtiquetasAntachawy.MAS,
        EtiquetasAntachawy.MENOS
    ],
    "OperadorMultiplicativo": [
        EtiquetasAntachawy.MULTIPLICA,
        EtiquetasAntachawy.DIVIDE
    ],
    "OperadorRelacional": [
        EtiquetasAntachawy.MAYOR,
        EtiquetasAntachawy.MENOR,
        EtiquetasAntachawy.IGUAL,
        EtiquetasAntachawy.DIFERENTE,
        EtiquetasAntachawy.MAYOR_IGUAL,
        EtiquetasAntachawy.MENOR_IGUAL
    ],
    "OperadorLogico": [
        EtiquetasAntachawy.Y,
        EtiquetasAntachawy.O
    ],
    "Termino": [
        EtiquetasAntachawy.PAREN_IZQ,
        EtiquetasAntachawy.ID,
        EtiquetasAntachawy.NUMEROENTERO,
        EtiquetasAntachawy.NUMEROFLOTANTE,
        EtiquetasAntachawy.CARACTER,
        EtiquetasAntachawy.CADENA,
        EtiquetasAntachawy.TRUE,
        EtiquetasAntachawy.FALSE
    ],
    "ExpresionImpresion": [
        EtiquetasAntachawy.PAREN_IZQ,
        EtiquetasAntachawy.ID,
        EtiquetasAntachawy.NUMEROENTERO,
        EtiquetasAntachawy.NUMEROFLOTANTE,
        EtiquetasAntachawy.CARACTER,
        EtiquetasAntachawy.CADENA,
        EtiquetasAntachawy.TRUE,
        EtiquetasAntachawy.FALSE
    ],
    "ExpresionImpresionPrime": [EtiquetasAntachawy.COMA, "$"]
}