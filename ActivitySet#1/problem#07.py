largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "quit":
        break
    try:
        x = int(num)
        if largest is None or largest < x:
            largest = x
        elif smallest is None or smallest > x:
            smallest = x
    except:
        print("Invalid input")
        continue
      
print("Maximum is", largest)
print("Minimum is", smallest)