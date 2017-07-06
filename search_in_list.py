# python3

print('Hi. I am test case 2.')

# Path to file with data
file = ""

bd_list = []
search_list = []
sand = []
# If no file - enter the data from the keyboard
if file != "":
    with open(file) as f:
        for line in f:
            sand_temp = line.rstrip().split()
            sand.append(sand_temp)
    bd_list = sand[1:int(sand[0][0])+1]
    search_list = sand[(int(sand[0][0])+2):]
else:
    print('Input some strings, then input several strings to search.')
    number_of_strings = int(input('How much strings do you want to input? (you will be searching in these) '))
    while number_of_strings > 0:
        bd_string = input("Please input a string: ")
        bd_list.append(bd_string)
        number_of_strings -= 1

    number_of_search_strings = int(input('Ok. Now, how much search strings do you want to input? '))
    while number_of_search_strings > 0:
        search_string = input("Please input a string: ")
        search_list.append(search_string)
        number_of_search_strings -= 1

for search in search_list:
    print(search, bd_list.count(search))

