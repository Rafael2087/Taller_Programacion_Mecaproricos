letra = input("Ingrese una letra: ")
vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
if letra in vocales:
    print (f"La letra {letra} es una vocal")
else:
    print ("La letra {} es una consonate".format(letra))
