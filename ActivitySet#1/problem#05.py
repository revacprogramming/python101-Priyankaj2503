# Functions
score = input("Enter Score: ")
s = float(score)
if s>1.0:
    print("entered value is greater than the range")
elif s<0.0:
    print("entered value is less than the range")    
elif s>=0.9:
    print("A")
elif s>=0.8:
    print("B")
elif s>=0.7:
    print("C")
elif s>=0.6:
    print("D")
else :
    print("F")
  #code is reviewed