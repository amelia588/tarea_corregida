#Algoritmo para sumar el numero actual y el anterior
número=0
while número < 10:
    número +=1

    suma=número+(número-1)
    print(número-1,"+",número, "=",suma)

