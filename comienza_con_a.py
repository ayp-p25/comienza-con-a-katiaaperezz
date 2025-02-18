"""
Comienza con A
"""

# Entradas
palabra = input("Escribe una palabra: ")

# Proceso
if palabra.startswith("A"):
    resultado = "'" + palabra + "'" + " comienza con " + "'" + "A" + "'"
elif palabra.startswith("a"):
    resultado = "'" + palabra + "'" + " comienza con " + "'" + "A" + "'"
elif palabra.startswith("á"):
    resultado = "'" + palabra + "'" + " comienza con " + "'" + "A" + "'"
elif palabra.startswith("Á"):
    resultado = "'" + palabra + "'" + " comienza con " + "'" + "A" + "'"
else: 
    resultado= "'" + palabra + "'" + " no comienza con " + "'" + "A" + "'"
# Salidas
print(resultado)
