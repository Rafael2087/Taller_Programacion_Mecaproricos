#Segundo Punto
num_uno : float; num_dos : float; num_tres : float
num_uno = float (input("Ingrese el primer numero: "))
num_dos = float (input("Ingrese el segundo numero: "))
num_tres = float (input("Ingrese el tercer numero: "))
if (num_uno > num_dos and num_uno > num_tres):
    print ("El numero {} es mayor que los numeros {} y {}".format(num_uno, num_dos, num_tres))
elif (num_dos > num_uno and num_dos > num_tres):
    print ("El numero {} es mayor que los numeros {} y {}".format(num_dos, num_uno, num_tres))
elif (num_tres > num_dos and num_tres > num_uno):
    print ("El numero {} es mayor que los numeros {} y {}".format(num_tres, num_uno, num_dos))