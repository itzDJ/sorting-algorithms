#!/usr/bin/env python3


def choose_created_list_type():
    """This function allows the user to choose the type of list"""
    list_type = input("What type of of list are you sorting (nums/alpha): ")
    list_type = list_type.lower()
    while list_type != 'nums' or list_type != 'alpha':
        if list_type == 'nums':
            return create_nums_list()
        elif list_type == 'alpha':
            return create_alpha_list()
        else:
            print(f"'{list_type}' was not an option.")
            list_type = input(
                "What type of of list are you sorting (nums/alpha): ")
            list_type = list_type.lower()


def create_nums_list():
    """This function allows the user to create a number list"""
    created_list = []
    print("\nType !quit to end list creation.")
    print("Type !pop to remove the last item you entered from the list.")
    while True:
        items = input("Add an item to the list: ")
        if items == "!quit":
            return created_list
            break
        elif items == "!pop":
            created_list.pop()
        else:
            try:
                pass  # error here
                # number = float(items)
            except ValueError:
                print("That's not a number.")
            else:
                created_list.append(float(items))


def create_alpha_list():
    """This function allows the user to create an alphanumeric list"""
    created_list = []
    print("\nType !quit to end list creation.")
    print("Type !pop to remove the last item you entered from the list.")
    while True:
        items = input("Add an item to the list: ")
        if items == "!quit":
            return created_list
            break
        elif items == "!pop":
            created_list.pop()
        else:
            created_list.append(items)


def choose_premade_list_type():
    """This function allows the user to choose the type of list"""
    list_type = input("What type of of list are you sorting (nums/alpha): ")
    list_type = list_type.lower()
    while list_type != 'nums' or list_type != 'alpha':
        if list_type == 'nums':
            return use_nums_list()
        elif list_type == 'alpha':
            return use_alpha_list()
        else:
            print(f"'{list_type}' was not an option.")
            list_type = input(
                "What type of of list are you sorting (nums/alpha): ")
            list_type = list_type.lower()


def select_list():
    """This functions allows the user to select a list"""
    filename = input("Enter the filename to be sorted: ")
    with open(filename) as f:
        lines = f.readlines()
        return lines


def use_nums_list():
    """"""
    created_list = []
    lines = select_list()
    for line in lines:
        try:
            pass  # some error here
            # number = float(line)
        except ValueError:
            pass
        else:
            created_list.append(float(line))
    return created_list


def use_alpha_list():
    """"""
    created_list = []
    lines = select_list()
    for line in lines:
        created_list.append(line.strip())
    return created_list


def the_list():
    """This function allows the user to choose a list"""
    choose_list = input("Create or select a list (c/s): ")
    choose_list = choose_list.lower()
    if choose_list == 'c':
        return choose_created_list_type()
    elif choose_list == 's':
        return choose_premade_list_type()
    else:
        print(f"'{choose_list}' was not an option.")
        return the_list()


def default_sort(result):
    result.sort()


def reverse_default_sort(result):
    result.sort(reverse=True)


def selection_sort(result):
    for i in range(len(result)):
        cur_min = i
        for j in range(i, len(result)):
            if result[j] < result[cur_min]:
                cur_min = j
        result[i], result[cur_min] = result[cur_min], result[i]


def bubble_sort():
    for j in range(1, len(result)):
        for i in range(0, len(result) - j):
            if result[i] > result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
            else:
                result[i], result[i + 1] = result[i], result[i + 1]
    return result


result = the_list()

# uncomment prefered sorting method here
default_sort(result)
print(result)

# reverse_default_sort(result)
# print(result)

# selection_sort(result)
# print(result)

# bubble_sort()
# print(result)
