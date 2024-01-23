#string slicing
names="alina,atika"
print(names[0:5])
#everything starts from zero in programming
#from zero to hero
fruit="mango"
len1=len(fruit)
print("MANGO IS A",len1,"letter word.")
print(fruit[0:3])#including zero but not 3
print(fruit[:4])# auto index 0
print(fruit[1:4])
print(fruit[0:-3]) #auto len (fruit is put here by python)
print(fruit[0:len(fruit)-3])   #ulta -
#negative slicing subract the index from total length of string
print(fruit[0:-2])    #gives last two letters
print(fruit[-1:len(fruit)-3])
print(fruit[-3:-1])
nm="harry"
print(nm[-4:-2])