from Hendese import circle
from Hendese import rectangle
from Hendese import Square
from Hendese import triangle
from Hendese import save_results


circle_r = 5.6
Square_r = 4

req_w = 6
req_l = 8

tri_a = 7
tri_b = 5
tri_c = 8
print("Testing functions:")
print(f"circle test", "=" * 60)
print(circle.circle_area(circle_r))
print(circle.circle_perimeter(circle_r))
print("=" * 70)

print(f"Square test", "=" * 60)
print(Square.area(Square_r))
print(Square.perimeter(Square_r))
print("=" * 70)

print(f"Rectangle test", "=" * 60)
print(rectangle.area(req_l, req_w))
print(rectangle.perimeter(req_w, req_l))
print("=" * 70)


print(f"Triangle test", "=" * 60)
print(triangle.area(tri_a, tri_b, tri_c))
print(triangle.perimeter(tri_a, tri_b, tri_c))
print("=" * 70)
print("Test finished. Functions work fine.")
step = 0

result = []
    
while True:
    print("Please choose a shape:")
    print("1.circle", "2.square", "3.Rectangle", "4.triangle", "5.Save")
    choice = int(input())
    step += 1
    
    try:

        if choice == 1:
            try:
                radius = float(input("Please enter radius"))
                
            except:
                raise ValueError("Please enter a numeric variable")
            
            else:
                area = circle.circle_area(radius)
                perimeter = circle.circle_perimeter(radius)
                
                print(f"area = {area:.2f}")
                print(f"perimeter = {perimeter:.2f}")
                
                to_app = {f"{step} area": area, f"{step} perimeter": perimeter, f"{step} shape": "circle"}
                result.append(to_app)

        elif choice == 2:
            
            try:
                side = float(input("Please enter sqare length:"))

            except:
                raise ValueError("Please enter a numeric variable")
            
            else:
                area = Square.area(side)
                perimeter = Square.perimeter(side)

                print(f"area = {area:.2f}")
                print(f"perimeter = {perimeter:.2f}")
                
                to_app = {f"{step} area": area, f"{step} perimeter": perimeter, f"{step} shape": "Square"}
                result.append(to_app)

        elif choice == 3:
            
            try:
                length = float(input("Please enter length: "))
                width = float(input("Please enter width"))
            except:
                raise ValueError("Please enter a numeric variable")
            
            else:
                area = rectangle.area(length, width) 
                perimeter = rectangle.perimeter(length, width)

                print(f"area = {area:.2f}")
                print(f"perimeter = {perimeter:.2f}")
                
                
                to_app = {f"{step} area": area, f"{step} perimeter": perimeter, f"{step} shape": "Rectangle"}
                result.append(to_app)

        elif choice == 4:
            try:
                a = float(input("Enter a"))
                b = float(input("Enter b"))
                c = float(input("Enter c"))

            except:
                raise ValueError("Please enter a numeric variable")
            
            else:
                area = triangle.area(a, b, c)
                perimeter = triangle.perimeter(a, b, c)

                print(f"area = {area:.2f}")
                print(f"perimeter = {perimeter:.2f}")
                
                
                to_app = {f"{step} area": area, f"{step} perimeter": perimeter, f"{step} shape": "triangle"}
                result.append(to_app)

        elif choice == 5:

            print(result)
            save_results.save_results("results.txt", result)
            print("End.")
            break

        else:
            print("Not a valid choice")

    except ValueError as error:
        print("Error", error)