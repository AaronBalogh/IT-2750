import math


def archimedes(numsides):
    innerangleB = 360.0 / numsides
    halfangleA = innerangleB / 2

    onehalfsideS = math.sin(math.radians(halfangleA))
    sideS = onehalfsideS * 2

    polygonCircumference = numsides * sideS
    pi = polygonCircumference/2

    polygonRadius = polygonCircumference/2 * pi
    print(polygonRadius)

    return polygonRadius

