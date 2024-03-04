list1=[5,10,15,20,25,50,20]
num_found=list1.index(20)
#square brackets []
list1[num_found]=200
print(list1)

#le int est important car sinon il considere le input comme un string
user_num=int(input('Give me a number '))
for i in range(10):
    print(i*user_num)

#while loop
counter=0
while counter <=8 :
    counter+=1
    print("hello")
    
password=''
while password!="123456":
    password=input('password?')
    if password=='juliana':
        break

print('you got the right password')
