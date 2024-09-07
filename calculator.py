import math
# The command "import math" is used to enable the use of math.pi and other functions and constants provided by the math module.
# f = F-strings allow you to embed variables and expressions inside curly braces {} within a string and format them.
#:.2f = It ensures that the result is rounded to two decimal places.

print("Area Calculator\n")
print("Please choose a shape to calculate its area:\n")
print("1) Square")
print("2) Rectangle")
print("3) Triangle")
print("4) Circle")
print("5) Quit")

q1 = int(input("Enter the number corresponding to your choice: "))

if q1 == 1:
    print("Square Area Calculator!")
    side = float(input("What is the side length? "))
    square_area = side * side
    print(f"The area of the square is {square_area:.2f}")

elif q1 == 2:
    print("Rectangle Area Calculator!")
    length = float(input("What is the length? "))
    width = float(input("What is the width? "))
    rectangle_area = length * width
    print(f"The area of the rectangle is {rectangle_area:.2f}")

elif q1 == 3:
    print("Triangle Area Calculator!")
    height = float(input("What is the height? "))
    base = float(input("What is the base? "))
    triangle_area = (base * height) / 2
    print(f"The area of the triangle is {triangle_area:.2f}")

elif q1 == 4:
    print("Circle Area Calculator!")
    radius = float(input("What is the radius? "))
    circle_area = math.pi * (radius ** 2)
    print(f"The area of the circle is {circle_area:.2f}")

elif q1 == 5:
    print("Goodbye!")

else:
    print("Invalid choice. Please choose a valid option.")

    
