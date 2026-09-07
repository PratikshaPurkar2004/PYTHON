str='''hi
hello
how are you?'''
print(str)
#''' same as print

#implicit typecasting=automatically changes the datatype
a=10
b=23.1
c=a+b
print(c)
print(type(c))

#explicit typecasting
a="10"
b=12.2
print(float(a)+b)

#slicing=
#thing[start:stop:step]
name="PratikshaRajeshPurkar"
print(name[2:9])
print(len(name))
print(name[5:-3])
print(name[-10:])
print(name[1:20:3])
print(name[::-1])#reverse string

print("Hello",end=" ")
print("pratiksha")

print("Pratiksha","Rajesh","Purkar",sep="-")
