my_list=["evan","navarro","lopez"]
for x in my_list:
    if x == "navarro":
        print(my_list)

my_list=["evan","navarro","lopez"]
result=[name for name in my_list]
print(result)

my_dict={"name":"evan","apellido":"navarro","edad":33,"profesion":"empleado"}
result2=[x for x in my_dict.values()]
print(result2)

