#zad1
A=[1-x for x in range(1,11,1)]
print(A)
B=[4**x for x in range(0,8,1)]
print(B)
C=[x for x in B if x%2==0]
print(C)

#zad2
import random
lista1=[int(random.random()*100) for x in range(10)]
print(lista1)
lista2=[x for x in lista1 if x%2==0]
print(lista2)

#zad5
def pole_trapezu(a,b,h):
    pole=((a+b)*h)/2
    if pole<=0:
        print('Error')
        return -1
    else:
        print('pole trapezu = ')
        return pole
print(pole_trapezu(3,8,2))
print(pole_trapezu(6,10,4))
print(pole_trapezu(3,7,5))

#zad4
def prostokatny(a,b,c):
    if a**2+b**2==c**2:
        return True
    elif c**2-a**2==b**2:
        return True
    elif c**2-b**2==a**2:
        return True
    else:
        return False
print(prostokatny(3,4,5))
print(prostokatny(3,6,7))