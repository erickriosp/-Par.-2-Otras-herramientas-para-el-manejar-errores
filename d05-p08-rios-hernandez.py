#practica 07
#rios peres jose heriberto
#hernandez del toro moises
print ("practica 08")
print ("rios perez jose heriberto")
print ("hernandez del toro moises")
def e1():#Ejemplo de primer ejemplo
    r=float(input("introduce el radio: "))
    pi = 3.1416
    while (r > 0):
        a = 4 * pi * r
        print("El area de una esfera de radio es:",a);
        return 
    print("Error el radio debe ser mayor que cero");

def e2():#Ejemplo de segundo ejemplo
    a=float(input("introduce la arista del cubo: "))
    while (a > 0):
        v = a * a * a
        print("El volumen del cubo de arista es:",v);
        a=float(input("introduce la arista del cubo: ")) 
    print("Error la arista debe ser mayor que cero");
    
def e3():#Ejemplo de tercer ejemplo
       a=int(input("introduce la tabla de multiplicar que desea: "))
       if( a < 0 ):
           print("Dato invalido");
           return e3()
       t=int(input("introduce el tope: "))
       if( t < 0 ):
           print("Dato invalido");
           return e3()
       i = 1
       while i <= t:
               print(a, "x", i,"=",a * i)
               i += 1
               
def e4(): # Ejemplo de cuarto ejemplo
    respuesta = "si"
    num_n1 = int(input("Ingrese el primer numero negativo: "))
    if num_n1 >= 0:
        print("Ingrese un numero negativo")
        return e4()
    num_n2 = int(input("Ingrese el segundo numero negativo: "))
    if num_n2 >= 0:
        print("Ingrese un numero negativo")
        return e4()
    num_n3 = int(input("Ingrese el tercer numero negativo: "))
    if num_n3 >= 0:
        print("Ingrese un numero negativo")
        return e4()
    num_n4 = int(input("Ingrese el cuarto numero negativo: "))
    if num_n4 >= 0:
        print("Ingrese un numero negativo")
        return e4()
    num_n5 = int(input("Ingrese el quinto numero negativo: "))
    if num_n5 >= 0:
        print("Ingrese un numero negativo")
        return e4()
    while respuesta == "si":
        num_n1 = num_n1 * -1
        print(num_n1)
        num_n2 = num_n2 * -1
        print(num_n2)
        num_n3 = num_n3 * -1
        print(num_n3)
        num_n4 = num_n4 * -1
        print(num_n4)
        num_n5 = num_n5 * -1 
        print(num_n5)
        respuesta = str(input("Desea ingresar mas numeros <si ó no> "))
        if respuesta == "si":
            return e4()
def e5(): # Ejemplo del quinto ejemplo
    cal_1 = float(input("Calificacion del primer alumno: "))
    if cal_1 < 0 or cal_1 >= 101:
        print("Ingrese un dato valido")
        return e5()
    cal_2 = float(input("Calificacion del segundo alumno: "))
    if cal_2 < 0 or cal_2 >= 101:
        print("Ingrese un dato valido")
        return e5()
    cal_3 = float(input("Calificacion del tercer alumno: "))
    if cal_3 < 0 or cal_3 >= 101:
        print("Ingrese un dato valido")
        return e5()
    cal_4 = float(input("Calificacion del cuarto alumno: "))
    if cal_4 < 0 or cal_4 >= 101:
        print("Ingrese un dato valido")
        return e5()
    cal_5 = float(input("Calificacion del quinto alumno: "))
    if cal_5 < 0 or cal_5 >= 101:
        print("Ingrese un dato valido")
        return e5()
    orden = [cal_1, cal_2, cal_3, cal_4, cal_5] # Arreglo
    cal_t = cal_1 + cal_2 + cal_3 + cal_4 + cal_5 # Calificaciones sumadas
    while cal_t <= 500:
        med = cal_t / 5 # Media
        print("La media es: ", med)
        orden.sort()
        print("La calificacion mas baja es: ", orden[0])
        cal_t = cal_t + 500

def e6(): # Ejemplo del sexto ejemplo
    cant_aut2 = 0
    amarilla = 0
    rosa = 0
    roja = 0
    verde = 0
    azul = 0
    respuesta = "si"
    while( respuesta == "si"):
        placa = str(input("Digite la placa: "))
        ult_placa = placa[-1]
        if ult_placa == "1" or ult_placa == "2":
            print("Calcomania amarilla")
            amarilla += 1
        elif ult_placa == "3" or ult_placa == "4":
            print("Calcomania rosa")
            rosa += 1
        elif ult_placa == "5" or ult_placa == "6":
            print("Calcomania roja")
            roja += 1
        elif ult_placa == "7" or ult_placa == "8":
            print("Calcomania verde")
            verde += 1
        elif ult_placa == "9" or ult_placa == "0":
            print("Calcomania azul")
            azul += 1
        else:
            pass
        respuesta=str(input("Desea agregar otra placa: "))
    print("Automoviles con calcomania amarilla: ", amarilla)
    print("Automoviles con calcomania rosa: ", rosa)
    print("Automoviles con calcomania roja: ", roja)
    print("Automoviles con calcomania verde: ", verde)
    print("Automoviles con calcomania azul: ", azul)

def menu(): # Ejemplo del septimo ejemplo
    elec = int(input("1.- e1()\n2.- e2()\n3.- e3()\n4.- e4()\n5.- e5()\n6.- e6()\nQue ejercicio desea: "))
    respuesta = "continuar"
    while respuesta == "continuar":
        if elec == 1:
            e1()
            respuesta = (input("Desea otro ejercicio <continuar ó salir> "))
            if respuesta == "continuar":
                return menu()
            else:
                print("Gracias")
        if elec == 2:
            e2()
            respuesta = input("Desea otro ejercicio <continuar ó salir> ")
            if respuesta == "continuar":
                menu()
            else:
                print("Gracias")
        if elec == 3:
            e3()
            respuesta = input("Desea otro ejercicio <continuar ó salir> ")
            if respuesta == "continuar":
                menu()
            else:
                print("Gracias")
        if elec == 4:
            e4()
            respuesta = input("Desea otro ejercicio <continuar ó salir> ")
            if respuesta == "continuar":
                menu()
            else:
                print("Gracias")
        if elec == 5:
            e5()
            respuesta = input("Desea otro ejercicio <continuar ó salir> ")
            if respuesta == "continuar":
                menu()
            else:
                print("Gracias")
        if elec == 6:
            e6()
            respuesta = input("Desea otro ejercicio <continuar ó salir> ")
            if respuesta == "continuar":
                menu()
            else:
                print("Gracias")
        break

