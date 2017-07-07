# python3
import sys, os.path

print('Hi. I am test case 2.')

# Path to file with data
if len(sys.argv) == 1:
    file = ""
else:
    if not os.path.exists(sys.argv[1]):
        print("File not found")
        sys.exit()
    else:
        file = sys.argv[1]

# If no file - enter the data from the keyboard
def get_data():
    bd_list = []
    search_list = []
    all_data_from_file = []
    if file != "":
        with open(file) as f:
            for line in f:
                sand_temp = line.rstrip().split()
                all_data_from_file.append(sand_temp)
        bd_list = all_data_from_file[1:int(all_data_from_file[0][0])+1]
        search_list = all_data_from_file[(int(all_data_from_file[0][0])+2):]
    else:
        print('Input some strings, then input several strings to search.')
        number_of_strings = ""
        while type(number_of_strings) != int:
            try:
                number_of_strings = int(input('How much strings do you want to input? (you will be searching in these) '))
            except:
                print("It's not a number. Input number please.")
                continue

        for number in range(number_of_strings):
            data_checking = 0
            while data_checking != 1:
                bd_string = input("Please input a string: ")
                if bd_string.isalpha():
                    bd_list.append(bd_string)
                    data_checking += 1
                else:
                    print("Enter string please")
                    continue


        number_of_search_strings = ""
        while type(number_of_search_strings) != int:
            try:
                number_of_search_strings = int(input('Ok. Now, how much search strings do you want to input? '))
            except:
                print("It's not a number. Input number please.")
                continue

        for number in range(number_of_search_strings):
            data_checking = 0
            while data_checking != 1:
                search_string = input("Please input a string: ")
                if search_string.isalpha():
                    search_list.append(search_string)
                    data_checking += 1
                else:
                    print("Enter string please")
                    continue

    return search_list, bd_list

def search_in_data():
    search_list, bd_list = get_data()
    for search in search_list:
        print(search, bd_list.count(search))

if __name__ == "__main__":
    search_in_data()