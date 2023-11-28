a=[ {"Titulo":"Maleducada", "Autor":"Antonio Ortiz", "Año":2016, "ISBN":9789583049705, "Paginas":153, "Precio":28000, "Categoria":"Ficcion"},
    {"Titulo":"El mito del votante irracional", "Autor":"Bryan Caplan", "Año":2007, "ISBN":9780691129426, "Paginas":276, "Precio":0,"Categoria":"Economia"},
    {"Titulo":"Aprendizaje automático y profundo en Python", "Autor":"Carlos Manuel Pineda Pertuz", "Año":2021, "ISBN":9789587923162, "Paginas":341, "Precio":79000, "Categoria":"Ciencia"}
    ]
b=[]
def mayor45(x):
    for i in a:
        if i["Precio"] >= 45000:
            b.append(i)
    return(b)

print(mayor45(a))