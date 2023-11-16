import math
def area(r):
    return math.pi * r**2

def vol(area,h):
    return area*h

def output(r, h):
    print("Das Volumen beträgt " + str(vol(area(r), h)))

radius = int(input("Geben sie den Radius ein: "))
height = int(input("Geben sie die Höhe ein: "))
output(radius,height)