def add(x,y):
    z=  x+y
    return z

a = float(input("Enter the first number: "))
b = float(input("Enter the second number:"))
c = add(a,b)

print ("sum of two given number is",c)
def main():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number:"))
    c = add(a,b)
    return c
s=main()
print("sum of two given number is",s)