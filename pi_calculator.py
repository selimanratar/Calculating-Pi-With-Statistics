import random
import math

print("How many darts would you like to throw?\n")
iterations = int(input())
print("Would you like to determine the radius of the circle yourself, or use the default 10? (y/n)\n")
boolean = input()

if (boolean == 'y'):
    print("What would you like the radius to be?")
    radius = float(input())
    
else: 
    radius = 10
    
inside_circle = 0
inside_square = 0

while (0 < iterations):
    
    iterations -= 1
    a = random.uniform(0,radius*2)
    b = random.uniform(0, radius*2)

    if (math.sqrt(abs(a-(radius))**2+abs(b-radius)**2) < radius):
        inside_circle += 1
        
    inside_square += 1
        
divident = float(inside_circle/inside_square)

print(f"PI is calculated as {divident*4}, after {inside_square} amount of darts.\nDo not forget, more darts you choose to throw, PI should get closer to it's actual value, which 3.1415926535897932...")
