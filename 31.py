
x = float(input("x = "))
y = float(input("y = "))

if x > 0 and y > 0:
    position = "first quadrant"
elif x < 0 and y > 0:
    position = "second quadrant"
elif x < 0 and y < 0:
    position = "third quadrant"
elif x > 0 and y < 0:
    position = "fourth quadrant"
elif x == 0 and y != 0:
    position = "on the y-axis"
elif x != 0 and y == 0:
    position = "on the x-axis"
else:
    position = "at the origin (0,0) of the coordinate system"

print(f"Point P({x},{y}) is in the {position} of the coordinate system")
