# # #data type
# # # #dynamic type 
# # # a=89
# # # a=67.90
# # # a="hello"
# # # print(a)
# # #1)Numeric data type=integer,float,complex  3+4j
# # #2)Text data type=string
# # #3)Sequence data type=list,tuple,range()
# # #4)Set data type=set ,frozen set
# # #5)Map data type=dictionary
# # #6)Binary data type=bytes and bytearray
# # #7)Boolean data type=True and False
# # #8)None data type
# # # a=None
# # # print(a)

# # #1)Numeric data type
# # #1)Integer=whole numbers can be both positive and negative 
# # a=-45
# # # type()
# # print(type(a))

# # #2)Float=decimal or fraction numbers can be both positive and negative
# # b=-4/5
# # print(type(b))

# # #3)complex=combination of real and imaginary numbers
# # c=5+0j
# # print(type(c))

# # a=34
# # b=67
# # print(type(a+b))

# # # n=67.89
# # # c=56.34
# # # print(type(n+c))
# # # c=97.13+3.87
# # # print(type(c))



# # #text data type=string=collection of one or more character(',",''',""")

# # # a='''i live in butwal
# # # i read in siplaya
# # # i am from ktm
# # # i am a student'''
# # # print(a)
# # # print(type(a))

# # #escape methods in string
# # #\n=line break
# # #\t=tab(4 four space)
# # my_name='my "name"\t is amisha'
# # print(my_name)


# name="my name is amsiha neupane"
# # len()=precoded or predefined length of character
# print(len(name))
# #indexing:position of character
# #syntxa:variable_name[index]
# print(name[-5])

# #slicing = accessing the part of the string
# #syntax:varaible_name[start:end:step]
# print(name[3:7]) #name
# #eman
# print(name[6:2:-1])

# s="python"
# print(len(s))
# #formula for even
# #len(variable)//2-1:len(variable)//2+1
# x=len(s)//2-1
# y=len(s)//2
# v=s[x:y+1]
# print(v)

# #odd
# a="pythons"
# print(len(a))
# #formula : len(varaible)//2
# x=len(a)//2
# print(a[x])







# # name="my name is amisha"
# # print(name[::])
# # print(name[::-1])
# # print(name[2:])
# # print(name[:8])
# # print(name[::3])
# # print(name[:2])
# # print(name[1::-1])

# # a="hello sipalaya"
# # print(a[4::-1])

# #ym


# #mutable and immutable
# #mutable(original data changeable)
# #immutable(original data cannot be cahnged)

# #string=immutable
# #string inbuitl methods(Predefined and precoded)
# #1)upper()=it change all character in capital letter or uppercase

# # b=a.upper()
# # print(b)
# # #2)lower()=it  chnage all character into small letter or lower case
# # c=b.lower()
# # print(c)

# #capitalize
# # d=c.capitalize()
# # # print(d)
# # b=a.capitalize()
# # print(b)

# #swapcase()=it convert lower=upper and upper=lower
# a="tolcome to to to  SIPALAYA"
# # b=a.swapcase()
# # print(b)

# # #startswith()
# # b=a.startswith("nn")
# # print(b)

# # #endswith()
# # b=a.endswith("sipalaya")
# # print(b)

# #count()=it counts numbers of character
# b=a.count("to")
# print(b)

# #find()=it finds index of charcater
# # b=a.find("z")
# # print(b)
# #index()
# # b=a.index("z")
# # print(b)


# #strip()=it removes space of head and tail 
# a="wwwelww comwww"
# # b=a.strip("w")
# #suffix(paxadi) prefix(aagadi)
# # b=a.removesuffix("www")
# b=a.removeprefix("wwwe")
# print(b)


# #split()
# fruits="apple*banana*orange* mango"
# b=fruits.split()
# print(b)


#center()
a="welcome to our company"
print(len(a))
b=a.center(90,"*")
print(b)

#replace()
c=a.replace("company","sipalaya")
print(c)
print(a)



print("helllo ankit ji")





