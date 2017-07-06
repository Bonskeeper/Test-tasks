# python 3

print('Hi. I am test case - hourglass.')

sand_test = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, -9, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]

# uncomment this block for user input

##sand = []
##for row in range(6):
##    sand_temp = input("Input six numbers with spaces as separator: ").split()
##    # we are assuming, that we do not need to check for str or len == 6
##    sand.append(sand_temp)


hourglass_sum_numbers = []
i = 0
for row_number, row_item in enumerate(sand_test):
    if i in range(len(sand_test[0])-2):    #This string needed to avoid IndexError: list index out of range
        for place, value in enumerate(row_item):
            if place in range(len(sand_test[0])-2):  #This string needed to avoid IndexError: list index out of range          
                total = sand_test[row_number][place] + sand_test[row_number][place+1] + sand_test[row_number][place+2] + sand_test[row_number+1][place+1] + sand_test[row_number+2][place] + sand_test[row_number+2][place+1] + sand_test[row_number+2][place+2]
                hourglass_sum_numbers.append(total)
            else:
                i += 1
                break
        
print(max(hourglass_sum_numbers))

