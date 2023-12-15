
#Una máquina de alimentos tiene productos de tres tipos, A, B y C, 
# que valen respectivamente $270, $340 y $390. La máquina acepta 
# y da de vuelto monedas de $10, $50 y $100.
#Escriba un programa que pida al usuario elegir el producto
# y luego le pida ingresar las monedas hasta alcanzar el monto a pagar. 
# Si el monto ingresado es mayor que el precio del producto, 
# el programa debe entregar las monedas de vuelto, una por una.


from os import system
import math

def devuelta(mon, num):
    if mon==1:
        print(num)
    elif mon==0:
        print("")
    else:
        for i in range(mon):
            print(num)

bebida = str(input(f"Ingresa el alimento que deseas \n a. $270 \n b. $340 \n c. $370 \n"))

if bebida=="a":
    total = 270
elif bebida=="b":
    total = 340
elif bebida=="c":
    total = 370

monedas10= 0
monedas50= 0
monedas100= 0
moneda = 1
system("cls")
print(f"Ingresa tus monedas de 10$, 50$, 100$ (Ingrese 0 si desea acabar)")
while moneda!=0:
    moneda = int(input("\n"))
    if moneda==10:
        monedas10 += 1
    elif moneda==50:
        monedas50 += 1
    elif moneda==100:
        monedas100 += 1
    elif moneda==0:
        system("cls")
    else:
        print(f"Ingrese la cantidad de la moneda correcta")
monedas10to=monedas10*10
monedas50to=monedas50*50
monedas100to=monedas100*100
tomonedas=monedas10to+monedas50to+monedas100to
vuelta=tomonedas-total
vuelta100=(math.trunc(vuelta/100))
resta=vuelta100*100
vuelta -=resta
vuelta50=(math.trunc(vuelta/50))
resta=vuelta50*50
vuelta -=resta
vuelta10=math.trunc(vuelta/10)

print (f"Tus vueltas son: ")
devuelta(vuelta100, 100)
devuelta(vuelta50, 50)
devuelta(vuelta10, 10)





        

    