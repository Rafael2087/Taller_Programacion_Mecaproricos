if __name__ == "__main__" :
 num_uno : float = float(input("DIjite un número: "))
 num_dos : float = float(input("DIjite un número: "))
 if num_uno % num_dos == 0 :
  print("El "+str(num_uno)+" es multiplo de "+str(num_dos))
 else:
  print("El "+str(num_uno)+" no es multiplo de "+str(num_dos))