"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    import csv
    with open('data.csv', 'r') as file:
        datos = csv.reader(file,delimiter="\t")
        respuesta1=0
        for fila in datos:
            respuesta1=respuesta1+int(fila[1])
    return respuesta1


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    import csv
    with open('data.csv', 'r') as file:
        datos = csv.reader(file,delimiter="\t")
        valores_unicos=[]
        valores=[]
        for fila in datos:
            valores.append(fila[0])
            if fila[0] not in valores_unicos:
                valores_unicos.append(fila[0])
        valores_unicos.sort()

        conteo=[]
        for i in valores_unicos:
            conteo.append(valores.count(i))

        respuesta2=list(zip(valores_unicos,conteo))
    return respuesta2


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    import csv
    with open('data.csv', 'r') as file:
        datos = csv.reader(file,delimiter="\t")
        datos = list(datos)
        valores_unicos=[]
        for fila in datos:
            if fila[0] not in valores_unicos:
                valores_unicos.append(fila[0])
        valores_unicos.sort()

        conteo=[]
        for i in valores_unicos:
            total=0
            for row in datos:
                if i==row[0]:
                    total=total+int(row[1])
            conteo.append(total)

        respuesta3=list(zip(valores_unicos,conteo))
    return respuesta3


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    import csv
    with open('data.csv', 'r') as file:
        datos = csv.reader(file,delimiter="\t")
        datos = list(datos)
        mes=[]
        for fecha in datos:
            if fecha[2][5:7] not in mes:
                mes.append(fecha[2][5:7])
        mes.sort()
        
        conteo_mes=[]
        for i in mes:
            total=0
            for row in datos:
                if i==row[2][5:7]:
                    total+=1
            conteo_mes.append(total)

        respuesta4=list(zip(mes,conteo_mes))
    return respuesta4


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    import csv
    with open('data.csv', 'r') as file:
        datos = csv.reader(file,delimiter="\t")
        datos = list(datos)
        valores_unicos=[]
        for fila in datos:
            if fila[0] not in valores_unicos:
                valores_unicos.append(fila[0])
        valores_unicos.sort()

        maximos=[]
        minimos=[]
        for i in valores_unicos:
            valores=[]
            for row in datos:
                if i==row[0]:
                    valores.append(row[1])
            maximos.append(int(max(valores)))
            minimos.append(int(min(valores)))

        respuesta5=list(zip(valores_unicos,maximos,minimos))
    return respuesta5


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    import csv
    from collections import defaultdict

    valores = defaultdict(list)

    with open('data.csv', 'r') as file:
        datos = csv.reader(file, delimiter="\t")

        for fila in datos:
            columna_cinco = fila[4]
            letras = columna_cinco.split(',')
            for conjunto in letras:
                clave, valor = conjunto.split(':')
                valores[clave].append(int(valor))

        respuesta6 = []
        for clave, valores_lista in valores.items():
                respuesta6.append((clave, min(valores_lista), max(valores_lista)))
        respuesta6.sort()
        
    return respuesta6 


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    import csv
    with open('data.csv', 'r') as file:
        datos = csv.reader(file,delimiter="\t")
        datos = list(datos)

        grupo_columna2 = {}
        for fila in datos:
            valor_columna1 = fila[0]
            valor_columna2 = int(fila[1])
            
            if valor_columna2 not in grupo_columna2:
                grupo_columna2[valor_columna2] = []
            grupo_columna2[valor_columna2].append(valor_columna1)

        orden =sorted(grupo_columna2)
        respuesta7 = {x: grupo_columna2[x] for x in orden}
        respuesta7 = [(key, value) for key, value in respuesta7.items()]

    return respuesta7


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    import csv
    with open('data.csv', 'r') as file:
        datos = csv.reader(file,delimiter="\t")
        datos = list(datos)

    diccionario = {}

    for fila in datos:
        valor = int(fila[1])
        letras = set(fila[0]) 
        if valor in diccionario:
            diccionario[valor] = diccionario[valor].union(letras)
        else:
            diccionario[valor] = letras

    respuesta8 = [(key, sorted(list(diccionario[key]))) for key in sorted(diccionario.keys())]

    return respuesta8


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    import csv
    with open('data.csv', 'r') as file:
        datos = csv.reader(file,delimiter="\t")
        datos = list(datos)

        frecuencias = {}
        for fila in datos:
            columna_cinco = fila[4] 
            letras = columna_cinco.split(',')
            for conjunto in letras:
                clave, valor = conjunto.split(':')
                if clave in frecuencias:
                    frecuencias[clave] += 1
                else:
                    frecuencias[clave] = 1
            
            orden =sorted(frecuencias)
            respuesta9 = {x: frecuencias[x] for x in orden}
    return respuesta9


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    import csv
    with open('data.csv', 'r') as file:
        datos = csv.reader(file,delimiter="\t")
        datos = list(datos)
    tupla = []
    for fila in datos:
        letras = fila[0]
        elementos_columna_4 = fila[3].split(',')
        elementos_columna_5 = fila[4].split(',')

        conteo_columna_4 = len(elementos_columna_4)
        conteo_columna_5 = len(elementos_columna_5)

        respuesta10 = (letras, conteo_columna_4, conteo_columna_5)

        tupla.append(respuesta10)
    return tupla


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    import csv
    with open('data.csv', 'r') as file:
        datos = csv.reader(file,delimiter="\t")
        datos = list(datos)

    diccionario = {}

    for fila in datos:
        letra = fila[3].split(',')[0]
        for letra in fila[3].split(','):
            numero = int(fila[1])  
            if letra in diccionario:
                diccionario[letra] += numero
            else:
                diccionario[letra] = numero

    respuesta11 = {key: diccionario[key] for key in sorted(diccionario)}

    return respuesta11


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    import csv
    with open('data.csv', 'r') as file:
        datos = csv.reader(file,delimiter="\t")
        datos = list(datos)

    diccionario = {}

    for fila in datos:
            clave = fila[0]  # Obtiene la clave de la columna 1
            valores = fila[4].split(',')  # Divide los valores de la columna 5 por coma
            for valor in valores:
                parte_valor = valor.split(':')
                if clave in diccionario:
                    diccionario[clave] += int(parte_valor[1])  # Suma el valor numérico
                else:
                    diccionario[clave] = int(parte_valor[1])

                orden =sorted(diccionario)
                respuesta12 = {x: diccionario[x] for x in orden}
    return respuesta12
