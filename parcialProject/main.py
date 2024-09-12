#conversion de tipos de datos
#Enteros a decimal
valor_Enteros = 10
ent_a_decimal=(float(valor_Enteros))

print(ent_a_decimal)


#convertir decimal a entero

valor_decimal=14.87
decimal_a_entero=(int(valor_decimal))
print(decimal_a_entero)

#convertir cadena a entero
cadena="987"
cadena_a_entero=(int(cadena))
print(cadena_a_entero)

#Multilineas de cadenas
cadena_ejemplo="Este es un ejemplo es para probar las multilineas de cadenas \n chanchito feliz  \n chanchito triste "
print("cadena multilinea:")
print(cadena_ejemplo)
print("\n")

#función len()longitud de una cadena, con esta función se cuenta cuantos caracteres tiene la cadena "Hola planeta Tierra"
cadena_a_contar = "Hola PLaneta Tierra"
print(f"longitud de la cadena'{cadena_a_contar}': {len(cadena_a_contar)}")
print("\n")

#sub cadenas
n = 8
#Cuenta los primeros n caracteres de una cadena
primeros_n = cadena_a_contar[:n]

#Cuenta los caracteres de el medio (si la longitud es impar)
medio = cadena_a_contar[len(cadena_a_contar)//2 - 1 : len(cadena_a_contar)//2 + 1]

#Cuenta los últimos n caracteres
ultimos_n = cadena_a_contar[-n:]

print("subcadenas:")
print(f"primeros {n} caracteres: {primeros_n}")
print(f"caracteres de en medio: {medio} ")
print(f"ultimos {n} caracteres: {ultimos_n} ")
print("\n")


#Funcion Upper()
print(f"'{cadena_a_contar}' en mayúsculas: {cadena_a_contar.upper()}")

#Funcion Lower()
print(f"'{cadena_a_contar}' en minúsculas: {cadena_a_contar.lower()}")
print("\n")

# Función strip() - Elimina espacios al inicio y al final
ejemplo_cadena = "   Fundacion universitaria de Popayan   "
print(f"Cadena original: '{ejemplo_cadena}'")
print(f"Cadena con strip: '{ejemplo_cadena.strip()}'")
print("\n")

# Función replace() - Reemplaza un  texto
print(f"Reemplazar 'Fundacion', 'FUP': {ejemplo_cadena.replace('Fundacion', 'FUP')}")
print("\n")

# Función split() - Dividide una cadena en partes
print(f"Dividir la cadena en palabras: {ejemplo_cadena.split()}")
print("\n")

# Formato de cadenas F-String Inserta valores de variables en la cadena de texto
nombre = "Rossby"
universidad = "FUP"
print(f"Hola, soy {nombre} y estudio en la {universidad} ")
