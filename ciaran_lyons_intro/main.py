import random


def get_num_names():
    #  Using a try loop here because we weant ot do a conversion to int and a
    #  check in one step[
    try:
        return int(
            input("Enter Number of names: ")
        )
    except Exception as e:
        print("Input is not an interger value")
        # we don't want to exit the program we want the user to give a valid
        # input int
        return get_num_names()


def get_user_input_name(name_index):
    input_name = input(f"Enter name number {name_index+1}: ")
    # becasue inpuit should be first, last take advantage of sp[lit to get a
    # list hopefully of 2 if not return
    if len(input_name.split()) == 2:
        print("input format is incorrect should contain two names seperated "
              "by one whitespace")
        return
    return input_name.split()


def make_random_name():
    #  Get a library that gives random names
    names = [
        "Bruno",
        "mars",
        "indigo"
    ]
    list_length = len(names)
    # random intergher is used to select form the list a ranokm name so nopt
    # same everytiume
    return names[random.randint(0, list_length-1)]


def capitalise_first_letter(first_name):
    # Upper case string
    return first_name[0].upper()


def capitalise(last_name):
    return last_name.upper()


def lower_case(first_name):
    return first_name.lower()


if __name__ == '__main__':
    num_names = get_num_names()
    result = []
    for index in range(0, num_names):
        names = get_user_input_name(index)
        result.append(" ".join([
            capitalise_first_letter(names[0]),
            make_random_name(),
            capitalise(names[1]),
            make_random_name(),
            lower_case(names[0])
        ]))
        print(f"\tInput: {' '.join(names)}")
        print(f"\tOutput: {result[index]}")
    print(result)
