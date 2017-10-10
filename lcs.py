import numpy as np
#initialize first string s1

def get_sequence(position_row,position_column):
    if position_row == 1 and position_column == 1:
        return final_sequence
    if table[position_row][position_column] == table[position_row][position_column-1]:
        get_sequence(position_row,position_column-1)

    elif table[position_row][position_column] == table[position_row-1][position_column]:
        get_sequence(position_row-1,position_column)
    else:
        #check diagonal
        #print "Checking diagonal"
        #print position_row-1
        #print position_column -1
        diagonal_element = table[position_row-1][position_column-1]
        if(table[position_row][position_column] == diagonal_element + 1):
            final_sequence.append(table[0][position_column])
            get_sequence(position_row-1,position_column-1)
s1 = "ACCGGTCGAGTGCGCGGAAGCCGGCCGAA"
s2 = " GTCGTTCGGAATGCCGTTGCTCTGTAAA"

convert_string_to_array = []
#Calculate the length of the string
for letter in s1:
    convert_string_to_array.append(letter)
column = len(convert_string_to_array)+2
convert_string_to_array = []

for letter in s2:
    convert_string_to_array.append(letter)
row = len(convert_string_to_array)+2

print row,column
table = [[0 for x in range(column)] for y in range(row)]
table_row = 0
table_column = 0
table[0][0] = "L"
table[0][1] = "P"
table_column = 2

for letter in s1:
    table[0][table_column] = letter
    table[1][table_column] = int(0)
    table_column = table_column + 1

table[1][0] = "P"
table_row = 2
for letter in s2:
    table[table_row][0] = letter
    table[table_row][1] = int(0)
    table_row = table_row + 1

table_row = 2
table_column = 2
for i in range(2,row,1):
    for j in range(2,column,1):
        if(table[table_row][0] == table[0][table_column]):
            element_in_the_preceding_diagonal = table[table_row -1][table_column-1]
            table[table_row][table_column] = element_in_the_preceding_diagonal + 1
        else:
            #print table[table_row][table_column-1]
            #print
            table[table_row][table_column] = max(table[table_row][table_column-1],table[table_row-1][table_column])
        table_column = table_column + 1
        #print j
        #print "Printing the matrix"
        #print np.matrix(table)
    table_row = table_row + 1
    table_column = 2
    #print i

print "Printing the matrix"
print np.matrix(table)
final_sequence = []
print "We are sending row "+str(row)
print "We are sending column "+str(column)
result = get_sequence(row-1,column-1)
print final_sequence












