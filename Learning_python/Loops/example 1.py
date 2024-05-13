"""x=""
for y in range(5):
    x = x + "*"
    print(x)

a = [1,2,3]
b = [0,20,4]

d = a + b

a.extend(b)
#a.sort()

print(a)

my_dict = {
    "name":"evan", "last name":"Navarro", "phone":"5580368040"
}
print(my_dict["name"])

for x in my_dict.values():
    print(x)

for x in my_dict.values():
    if x == "evann":
        print(True)
    else: 
        print(False)

print("evan" in my_dict.values())
print(my_dict.keys())

my_list=[1,2,3,4,5,6,7,8,9,0]
my_list.sort()
if 2 not in my_list:
    print("el 2 no esta en la lista")
else :
    print ("el dos si esta en la lista")

for num in my_list:
    
    print(num)

    
i = 0
while i < 5:
    print(i)
    i = i + 1
    
i = 0

while i < 10:
    if i == 3:
        i += 1
        continue

    print(i)

    if i == 5:
        break
    i += 1

try:
    x = [i for i in range(5)]
    print(x)

except:
    print("no se encontro")

#print( {i: str(i) for i in range(5)} )

my_dict = {
    "name":"evan", "last name":"Navarro", "phone":"5580368040"
}
print({key:str(value) for key, value in my_dict.items()})


"""




doc = open(r"C:\Users\SYGNO\Desktop\notas.txt", "r")
data = doc.readlines()
for x in data:
    if x.find() == "Titular" :
        print(x)

