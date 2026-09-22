# فرض می کنیم برای مثلث سه ضلع رو بهمون میدن
import math

def perimeter(a, b , c):
    return (a + b + c)

def area(a, b, c):
    p = perimeter(a, b, c)
    s = p / 2
    
    return math.sqrt(s * (s - a) * (s - b) * (s - c))