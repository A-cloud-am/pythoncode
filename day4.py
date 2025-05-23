#tuple=sequence data type,collection data,data is seperated 
# by comma and data structureand data format,group of data
#immutable(original data is not changeable),allow duplicate values,order
#it doesnot have any methods
a=(12,34.89,"hari",3+4j,"world",12,12,12,34,34,34,34)  #contsant
print(type(a))
print(a)
print(len(a))
print(a[0])
print(a[2][0])
print(a[-5])

# a[0]=67
# print(a)

# a.append(56)
# print(a)

#list=mutable  tuple=immutable
#list=methods   tuple=no methods
#list=low performance tuple=fast performance


#range()=sequence data type,it generates large amount of numbers,order
#syntax: range(start,end,step)
a=range(7,0,-1)   #end=10 default start=0 default step=1   #0 1 2 3 4 5 6 7 8 
print(type(a))  #1 4 7 10   #7 6 5 4 3 2 1
print(a)
print(a[0:4:1])




#set data type=set,collection of data,mutable(original data changeable),
# #doesnot allow duplicate values,unorder
# #no slicing and indexing
# a={12,"hari",67.89,"world",56,90,12,34,34,34,34,34,"world"}
# print(type(a))
# print(a)
# print(len(a))

# #set inbuilt methods 
# #add()=adding single data
# a.add("tina")
# print(a)

# #update()=adding multiple data
# a.update({45,21,23,"rita"})
# print(a)


# #deleting methods
# #pop()=
# # a.pop()
# # print(a)

# #remove()=particular data removes
# # a.remove(100)
# # print(a)

# #discard()
# a.discard(100)
# print(a)

# #clear()
# a.clear()
# print(a)
# a=set({45,"tina","hello"})
# print(a)
# a.clear()
# print(a)

# del a
# print(a)

#union()=it prints all the value that is present in both set
a={1,2,3,4}
b={2,4,6,8}
var=b.union(a)
print(var)
#intersection()=common value in both set
var1=a.intersection(b)
print(var1)

#difference()
var2=a.difference(b) #a-b  (a0)
var3=b.difference(a)  #b-a  (b0)
print(var2)
print(var3)

#symmetric_difference()=it prints value that
#  is present in both set but differnce common 
c=a.symmetric_difference(b)
print(c)

#issuperset() issubset isdisjoint()
a={1,2,3,4,5}
b={6,7,8,9}
c=a.issuperset(b)
print(c)
d=b.issubset(a)

print(d)
f=a.isdisjoint(b)
print(f)



#frozen set(immutable)
a=frozenset({1,2,3,4})
print(type(a))
# a.add(45)
# print(a)
print(a)
b=a.union({4,5,6,7})
print(b)
c=a.intersection({1,2,34,5})
print(c)
