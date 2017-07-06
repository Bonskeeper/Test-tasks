# python3

print('Hi. I am test case 1.')

# Path to file with data
file = ""

# If no file - enter the data from the keyboard
sand = []
if file != "":
    with open(file) as f:
        for line in f:
            sand_temp = line.rstrip().split(" ")
            sand.append(sand_temp)
else:
    number_of_str = int(input('How much strings do you want to input? ' ))
    while number_of_str > 0:
        sand_temp = input("Please input a string with spaces as separator Name, Surname, Sex, Age: ").split(" ")
        sand.append(sand_temp)
        number_of_str -= 1


def sort_col(i):
    return i[4]

def my_decorator_for_add_Mr_and_Mrs(function_to_decorate):
    # Декоратор для добавления приставки Г-н и Г-жа
    def the_wrapper_around_the_original_function(arg1):
        for line in arg1:
            if "Ж" in line[2]:
                line.insert(0, "Г-жа")
            else:
                line.insert(0, "Г-н")
        function_to_decorate(arg1)
    return the_wrapper_around_the_original_function

@my_decorator_for_add_Mr_and_Mrs
def sort_by_age(list_for_sort):
    list_for_sort.sort(key=sort_col)
    for line in list_for_sort:
        print (" ".join(line))    


sort_by_age(sand)
