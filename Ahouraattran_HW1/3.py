my_list= []

for i in range(1, 5):
    x = int(input(f"Enter {i} value: "))
    my_list.append(x)
    
y = int (input("Enter a valur: "))

print(my_list.count(y))