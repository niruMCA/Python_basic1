a=int(input("Enter any No.:"))
i=a
rev=0
while i>0 :
d=i%10
rev=((rev*10)+d)
i=i//10
if a==rev :
print("The number is palindrom.")
else :
print("Not palindrom.")
