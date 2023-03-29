def get_name():
    #
    # students should write the code for this function
    #

    # get the names
    name_list = []
    n = 3
    for i in range(n):
        name = input("Please enter name %d of %d: " % (i+1, n))
        first_last = name.split(" ")
        name_list.append(first_last)

    # sort the names (this is an advanced way to sort by last name, sort() also works)
    name_list.sort(key=lambda x: x[1])

    return name_list


def create_greeting(name): 
    greeting_list = ["Hello", "Welcome", "Dear", "Hi", "Yoroshiku", "Konnichiwa"]

    # import the random module, and use choice to make random choices
    import random
    greeting = random.choice(greeting_list)
    first = name[0]

    result = greeting + " " + first

    return result


def get_age(name_list):
    #
    # students should write the code for this function
    #
    n = len(name_list)
    age_list = []
    for i in range(n):
        name = name_list[i]
        greeting = create_greeting(name)
        age_input = input("%s, how old are you?: " % greeting)
        age = int(age_input)
        age_list.append(age)

    return age_list


def print_first_report(name_list):
    """
    prints first report
    """

    print()
    print("The sorted names are:")
    n = len(name_list)
    for i in range(n):
        name = name_list[i]
        # this is an advanced way to "unpack" a list. name[0], name[1] also works.
        first, last = name
        print("%d. %s, %s" % (i+1, last, first))


def print_final_report(name_list, age_list):
    """
    prints the final report
    """
    print()
    print("The names and ages sorted by last name are:")
    n = len(name_list)
    for i in range(n):
        name = name_list[i]
        # this is an advanced way to "unpack" a list. name[0], name[1] also works.
        first, last = name
        age = age_list[i]
        print("%d. %s, %s is %d years old" % (i+1, last, first, age))


def main():
    """
    main prints each person and their age.
    """
    #
    # students should write the code for this function
    #

    # get and print names
    name_list = get_name()
    print_first_report(name_list)

    # for each person get their age, and greet them
    age_list = get_age(name_list)

    # print final report information
    print_final_report(name_list, age_list)


main()