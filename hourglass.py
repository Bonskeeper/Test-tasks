# python 3

print('Hi. I am test case - hourglass.')



def get_data():
    sand = []
    for row in range(6):
        sand_temp = input("Input six numbers with spaces as separator in range -9 to 9: ").split()
        # we are assuming, that we do not need to check for str or len == 6
        for i, elem in enumerate(sand_temp):
            sand_temp[i] = int(elem)
        sand.append(sand_temp)
    return sand

def calculating_the_largest_hourglass():
    sand = get_data()
    hourglass_sum_numbers = []
    i = 0
    for row_number, row_item in enumerate(sand):
        if i in range(len(sand[0])-2):    #This string needed to avoid IndexError: list index out of range
            for place, value in enumerate(row_item):
                if place in range(len(sand[0])-2):  #This string needed to avoid IndexError: list index out of range
                    total = sand[row_number][place] + sand[row_number][place+1] + sand[row_number][place+2] + \
                            sand[row_number+1][place+1] + sand[row_number+2][place] + sand[row_number+2][place+1] + \
                            sand[row_number+2][place+2]
                    hourglass_sum_numbers.append(total)
                else:
                    i += 1
                    break

    return print(max(hourglass_sum_numbers))


if __name__ == "__main__":
    calculating_the_largest_hourglass()