#loops in python: for loops and while loops
#range use 2 
for i in range(10):
    print('python')


for i in range(5,10):
    print('avi')

for i in range(len('juliana')):
    print('ju')   

students=['john','bob','anna','lise']
for each_student in students:
    if each_student is 'anna':
        print('hello anna')
    else:
        print(each_student)

cities=('tel aviv','jerusalem','amsterdam','paris')
for city in cities:
    print(f'I have been in {city}')

#finding the max and the min and the sum
list1=[5,25,4,85,12,1]
print(max(list1))
print(min(list1))
print(sum(list1))