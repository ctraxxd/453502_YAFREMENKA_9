import os
import square
import circle

shape = os.getenv("SHAPE", "circle")
a = float(os.getenv("A", "3"))

if shape == "circle":
    print(circle.area(a))
    print(circle.perimeter(a))
elif shape == "square":
    print(square.area(a))
    print(square.perimeter(a))
else:
    raise ValueError("Unknown SHAPE")
