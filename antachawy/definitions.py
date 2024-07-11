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
    OPERADOR_ARITMETICO = "OPERADOR_ARITMETICO"
    OPERADOR_RACIONAL = "OPERADOR_RACIONAL"
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
    NUMEROENTERO = "NUMERO"
    NUMEROFLOTANTE = "FLOTANTE"
    CARACTER = "CARACTER"
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
    LexemasAntachawy.SALTO_LINEA:       EtiquetasAntachawy.SALTO_LINEA,
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
    LexemasAntachawy.NUMEROENTERO:      EtiquetasAntachawy.NUMEROENTERO,
    LexemasAntachawy.NUMEROFLOTANTE:    EtiquetasAntachawy.NUMEROFLOTANTE,
    LexemasAntachawy.CARACTER:          EtiquetasAntachawy.CARACTER,
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
    "ListaSentencias": [
        LexemasAntachawy.YUPAY,
        LexemasAntachawy.CHUNKAYUQ,
        LexemasAntachawy.SANANPA,
        LexemasAntachawy.QAYTU,
        LexemasAntachawy.BOOL,
        LexemasAntachawy.SIQIY,
        LexemasAntachawy.ID
    ],
    "Sentencias": [
        LexemasAntachawy.YUPAY,
        LexemasAntachawy.CHUNKAYUQ,
        LexemasAntachawy.SANANPA,
        LexemasAntachawy.QAYTU,
        LexemasAntachawy.BOOL,
        LexemasAntachawy.SIQIY,
        LexemasAntachawy.ID
    ],
    "Declaraciones": [
        LexemasAntachawy.YUPAY,
        LexemasAntachawy.CHUNKAYUQ,
        LexemasAntachawy.SANANPA,
        LexemasAntachawy.QAYTU,
        LexemasAntachawy.BOOL
    ],
    "Asignaciones": [LexemasAntachawy.ID],
    "Impresiones": [LexemasAntachawy.SIQIY],
    "Tipo": [
        LexemasAntachawy.YUPAY,
        LexemasAntachawy.CHUNKAYUQ,
        LexemasAntachawy.SANANPA,
        LexemasAntachawy.QAYTU,
        LexemasAntachawy.BOOL
    ],
    "Expresion": [
        LexemasAntachawy.PAREN_IZQ,
        LexemasAntachawy.ID,
        LexemasAntachawy.NUMEROENTERO,
        LexemasAntachawy.NUMEROFLOTANTE,
        LexemasAntachawy.CARACTER,
        LexemasAntachawy.CADENA
    ],
    "ExpresionPrime": [
        LexemasAntachawy.MAS,
        LexemasAntachawy.MENOS,
        LexemasAntachawy.MULTIPLICA,
        LexemasAntachawy.DIVIDE
    ],
    "Operador": [
        LexemasAntachawy.MAS,
        LexemasAntachawy.MENOS,
        LexemasAntachawy.MULTIPLICA,
        LexemasAntachawy.DIVIDE
    ],
    "Termino": [
        LexemasAntachawy.PAREN_IZQ,
        LexemasAntachawy.ID,
        LexemasAntachawy.NUMEROENTERO,
        LexemasAntachawy.NUMEROFLOTANTE,
        LexemasAntachawy.CARACTER,
        LexemasAntachawy.CADENA
    ],
    "ExpresionImpresion": [
        LexemasAntachawy.PAREN_IZQ,
        LexemasAntachawy.ID,
        LexemasAntachawy.NUMEROENTERO,
        LexemasAntachawy.NUMEROFLOTANTE,
        LexemasAntachawy.CARACTER,
        LexemasAntachawy.CADENA
    ],
    "ExpresionImpresionPrime": [LexemasAntachawy.COMA]
}

segundos = {
    "Programa": [],
    "Definicion": [],
    "ListaSentencias": [LexemasAntachawy.PAREN_DER],
    "Sentencias": [
        LexemasAntachawy.ID,
        LexemasAntachawy.YUPAY,
        LexemasAntachawy.CHUNKAYUQ,
        LexemasAntachawy.SANANPA,
        LexemasAntachawy.QAYTU,
        LexemasAntachawy.BOOL,
        LexemasAntachawy.SIQIY
    ],
    "Declaraciones": [LexemasAntachawy.SALTO_LINEA],
    "DeclaracionesPrime": [LexemasAntachawy.SALTO_LINEA],
    "Asignaciones": [LexemasAntachawy.SALTO_LINEA],
    "Impresiones": [LexemasAntachawy.SALTO_LINEA],
    "Tipo": [LexemasAntachawy.ID],
    "Expresion": [
        LexemasAntachawy.PAREN_DER,
        LexemasAntachawy.COMA,
        LexemasAntachawy.SALTO_LINEA
    ],
    "ExpresionPrime": [
        LexemasAntachawy.PAREN_DER,
        LexemasAntachawy.COMA,
        LexemasAntachawy.SALTO_LINEA
    ],
    "Operador": [
        LexemasAntachawy.PAREN_IZQ,
        LexemasAntachawy.ID,
        LexemasAntachawy.NUMEROENTERO,
        LexemasAntachawy.NUMEROFLOTANTE,
        LexemasAntachawy.CARACTER,
        LexemasAntachawy.CADENA
    ],
    "Termino": [
        LexemasAntachawy.MAS,
        LexemasAntachawy.MENOS,
        LexemasAntachawy.MULTIPLICA,
        LexemasAntachawy.DIVIDE
    ],
    "ExpresionImpresion": [LexemasAntachawy.PAREN_DER],
    "ExpresionImpresionPrime": [LexemasAntachawy.PAREN_DER]
}