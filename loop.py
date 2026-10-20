n=int(input("Enter a number:"))

# number from  1 to n using for loop

print("Number from 1 to n :")
for i in range(1,n+1):
    print(i)


# number from n to 1 using while loop

print(" Number from ",n,"to 1")
i=n
while i>=1:
    print(i)
    i -=1

#Multiplication table

print("Multiplication table of",n)
for i in range(1,11):
   print(n,"x",i,"=",n*i)