# python3
# -*- coding: utf-8 -*-
import sys, os.path

print('Hi. I am test case 1.')

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
human_data = []
if file != "":
    with open(file) as f:
        for line in f:
            sand_temp = line.rstrip().split(" ")
            human_data.append(sand_temp)
else:
    number_of_str = ""
    while type(number_of_str) != int:
        try:
            number_of_str = int(input('How much strings do you want to input? ' ))
        except:
            print("It's not a number. Input number please.")
            continue
    for number in range(number_of_str):
        data_checking = 0
        while data_checking != 1:
            sand_temp = []
            sand_name, sand_surname, sand_sex, sand_age = input("Please input a string with spaces as separator Name, Surname, Sex, Age: ").split(" ")
            if sand_name.isalpha and sand_surname.isalpha and sand_sex in ["Ж","ж","м","М"] and int(sand_age) in range(5,120):
                data_checking += 1
                sand_temp.append(sand_name)
                sand_temp.append(sand_surname)
                sand_temp.append(sand_sex)
                sand_temp.append(sand_age)
                human_data.append(sand_temp)
            else:
                print("Enter all the data correctly")
                continue

def sort_col(i):
    return i[4]

def my_decorator_for_add_Mr_and_Mrs(function_to_decorate):
    # Декоратор для добавления приставки Г-н и Г-жа
    def the_wrapper_around_the_original_function(arg1):
        for line in arg1:
            if line[2] in ["Ж","ж"]:
                line.insert(0, "Г-жа")
            else:
                line.insert(0, "Г-н")
        function_to_decorate(arg1)
    return the_wrapper_around_the_original_function

@my_decorator_for_add_Mr_and_Mrs
def sort_by_age(list_for_sort):
    list_for_sort.sort(key=sort_col)
    for line in list_for_sort:
        print (" ".join(line[0:3]))


if __name__ == "__main__":
    sort_by_age(human_data)

