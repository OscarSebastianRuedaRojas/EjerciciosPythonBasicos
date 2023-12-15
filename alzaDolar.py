n = int(input(f"Cuantos dias? \n"))
Dias= []
for i in range(n):
    precio=int(input(f"Dia {i+1}: \n"))
    Dias.append(precio)
Alzamayor=int(0)
for i in range(1, n-1):
    Alza= Dias[i]-Dias[i-1]
    if Alza>Alzamayor:
        Alzamayor=Alza
if Alzamayor==0:
    print("No hubo alza")
else:
    print(f"La mayor alza fue: {Alzamayor}")