from math import sqrt

a = float(input("entrez un premier nombre: "))
b = float(input("entrez un deuxieme nombre: "))
c = float(input("entrez un troisieme nombre: "))
def secondegre(a, b, c):
    d = (b ** 2) - (4 * a * c)
    print("le discriminant de l'equation est", d)
    if(d< 0):
        print("l'equation n'a pas de solution")
    elif(d == 0):
        print("l'equation a une solution et sa valeur est", -b/(2*a))
    else:
        print("l'equation a deux solution et ses valeurs sont")
        print("solution X1: ",(-b-sqrt(d)/(2*a)))
        print("solution X1: ",(-b+sqrt(d)/(2*a)))


secondegre(-4,2,5)
