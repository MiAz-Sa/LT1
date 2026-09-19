import math
#input stage
radius = float(input("Please enter your radius..."))

                                         #calculation and answer or something idk...
area = math.pi * math.pow(radius, 2)
print("Your area is", area)

circ = 2 * math.pi * radius
print("Your circumference is", circ)

SOA = math.sqrt(area)                    # SOA being square root of area
print("The square root of the area is", SOA)

ARU = math.ceil(area)                    #ARU being area rounded up
print("The area rounded down is", ARU)

ARD = math.floor(area)                   #ARD being area rounded down
print("The area rounded down is", ARD)