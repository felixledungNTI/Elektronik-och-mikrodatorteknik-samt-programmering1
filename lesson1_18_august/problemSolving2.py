from math import sqrt

a = 3
b = 4
c = 5

#omkretsen av triangeln
circumference = a+b+c

print(f"Omkretsen av triangeln är {circumference}")

#area of triangle

s = (a+b+c)/2

area = sqrt(s*(s-a)*(s-b)*(s-c))

print(f"Arean av triangeln är: {area}")