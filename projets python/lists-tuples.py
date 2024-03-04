# user_name="john"
# user_email='john@gmail.com'
# user_age='25'

# user_info=[user_name,user_email,user_age]
# print(user_info)
# print(user_info[1])

# user_name_list=[user_name]
# print(user_name_list)

# #separate each caracter of the list
# user_name_list2=list(user_name)
# print(user_name_list2)

# user_name_list3=user_name.split(',')
# print(user_name_list3)

# #comma separator : ,
# user_info2=input('give me your name, email and age separated by , :').split(',')
# print(user_info2)

# user_info2.append('betzalel')

# changing an element
color_list=['blue','red','green','green']
# color_list[1]='red'

#sort() and sorted()
new_list=sorted(color_list)
print(color_list.sort())
print(new_list)

#removing element
new_list.remove('red')
print(new_list)

#Tuples-> round brackets ()
#Tuple is a sequence that can
my_tuple=(1,2,3,4,5)
color_tuple=tuple(color_list)
print(color_tuple)

a,b,c,d=(10,20,30,40)
print(a)
print(my_tuple[2])

#Sets-> curly brackets {}
#sets is a collection 
#les Sets ne sont pas ordonnés mais ne contiennent pas de duplicate
clean_set=set(color_list)
clean_set.add('purple')
print(clean_set)

words={'hello','there','python'}
joined_sets=clean_set.union(words)
print(joined_sets)
joined_sets.remove('blue')
print(joined_sets)

joined_sets.pop()
print(joined_sets)