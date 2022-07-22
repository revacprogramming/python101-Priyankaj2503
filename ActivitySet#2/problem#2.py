def output(a, b, sum):
    print("sum of given two numbers is",sum)
    print("sum of given two numbers ",a,"and" ,b,"is",sum)

def main():
    a = float(input("inputtwo_numbers:"))
    b = float(input("enterthe secomd number:"))
    a = float(input("input first_number:"))
    b = float(input("enter the second number:"))
    sum = add(a, b)
    output(a, b, sum)
if __name__ == '__main__':
    main()