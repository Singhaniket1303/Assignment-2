#QUES 1#

x= "Python is a case sensitive language"

# a)using len() to find the length
print(len(x))


# b)using slicing to reverse the order of strings
txt=x[::-1]
print(txt)


# c) Using slicing
s=slice(10,26)
New_string=x[s]
print(New_string)


# d) Using Replace()
a=x.replace("a case sensitive", "object oriented")
print(a)


# e) Using index()
print(x.index("a"))


# f) Using Replace()
print(x.replace(" ",""))


#QUES 2#
x= """
    Hey,{name} Here!\n
    My Sid is {sid}\n
    I am from {dep} Department and my CGPA is {cgpa:.1f}
    """
print

#QUES 3#
a=56
b=10

print(a & b)
print(a | b)
print(a ^ b)
print("a shift left by 2--", a << 2)
print("b shift left by 2--", b << 2)
print("a shift right by 2--", a >> 2)
print("b shift right by 4--", b>>4)

#QUES 4#

a = int(input("First Number: "))
b = int(input("Second Number: "))
c = int(input("Third Number: "))

#comparing numbers
if a>b and a>c:
    print(a,"is the largest number")
if b>a and b>c:
    print(b,"is the largest number")
if c>a and c>b:
    print(c,"is the largest number")

    # QUES 5#

a=input("Enter a sentence: ")
if "name" in a :
    print("Yes")
else :
    print("No")

# QUES 6#

a=int(input("Enter the length of First side of the triangle: "))
b=int(input("Enter the length of the Second side of the triangle: "))
c=int(input("Enter the length of Third side of the triangle: "))

if a>=b+c :
    print("NO")
if b>=a+c :
    print("NO")
if c>=a+b :
    print("NO")
else :
    print("YES")
