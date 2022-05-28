def computepay(h, r):
    if h <= 40:
        p = h * r 
    else:
        p = 40*r + (h-40)*1.5*r
    return p

hrs = int(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
p = computepay(hrs,rate)
print("Pay",p)
 #code is reviewed