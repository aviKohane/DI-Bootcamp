matrix_string=''' 7ii
    Tsx
    h%?
    i #
    sM 
    $a 
    #t%
    ^r!'''
# matrix 2D list
# [[],[],[]]
COLUMNS = 3
ROWS = 8
# matrix=[]
# for i in range (len(matrix_string)):
#     sublist=list(matrix_string[i:i+COLUMNS])
#     matrix.append(sublist)
    
# print(matrix)

rows=matrix_string.split('\n')
print(rows)
# for row in rows:
#     matrix.append(list(row))
matrix=[list(row) for row in rows]
transposed_matrix=list(zip(*matrix))
print(transposed_matrix)

print(matrix)

transposed_message=[''.join(char) for char in transposed_matrix]
print(transposed_matrix)
dec_message=''
final_str=dec_message.join(transposed_message)
print(final_str)

decrypted_message
