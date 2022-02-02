print(" -----------------  CALCULADORA DE PYTHON ------------")
print("1. operacion suma.")
print("2. operacion resta")
print("3. operacion multiplicacion.")
print("4. operacion division.")
o = int(input("Seleccione una operacion."))

if o == 1:
    num1 = int(input("Escriba su primer número"))
    num2 = int(input("Escriba su segundo número"))
    suma = num1+num2
    print("El resultado de la suma es: " ,suma)
elif o == 2:
    num1 = int(input("Escriba su primer número"))
    num2 = int(input("Escriba su segundo número"))
    resta = num1-num2
    print("El resultado de la suma es: " ,resta)

elif o == 3:
    num1 = int(input("Escriba su primer numero."))
    num2 = int(input("Escriba su segundo numero."))
    mult = num1 * num2
    print("el resultado de la Multiplicacion es: ",mult)

elif o == 4:
    num1 = int(input("Escriba su primer numero."))
    num2 = int(input("Escriba su segundo numero."))
    div = num1 / num2
    print("el resultado de la division es: ",div)
    
else:
    print("OPCIÓN FUERA DE RANGO ")
