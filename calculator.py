print("==================")
print("Area Calculator 📐")
print("==================")

print ("1) Triangle")
print ("2) Rectangle")
print ("3) Square")
print ("4) Circle")
print ("5) Quit")

which = int (input("Which shape calculate? "))
if which == 1:
  h = float (input("height: "))
  b = float(input("base: "))
  area_triangle = float ((h * b)/2)
  print("The area is",area_triangle)
elif which == 2:
  l = float (input("lenght: "))
  w = float (input("width: "))
  area_rectangle = l*w
  print("The area is ",area_rectangle)
elif which == 3:
  s = float (input("side: "))
  area_square = s**2
  print ("The area is ",area_square)
elif which == 4:
  pi = 3.14
  r = float (input("radius:"))
  area_circle = pi*(r**2)
  print ("The area is", area_circle)
elif which == 5:
  print ("Exiting the program...")
else:
  print ("Error: Unknown")
