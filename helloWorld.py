#print statements
print("Hello world")
print("How are you doing today")
#arithmetic satements 
x = 1
y= 2
print(x+y)
print (y-x)
print(y*x)
print(y/x)
#input
name = input("what is your name? ")
print(name)
age = int(input("what is your age? "))

#if condition
if(age < 14 and age > 0 ):
    print(name + " is in elementary school")
elif(age > 15 and age < 18):
    print(name + " is in highschool")
elif(age < 0):
    print("age invalid")
else: 
    print(name + " is an adult")

