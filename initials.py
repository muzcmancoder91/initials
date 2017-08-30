def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    # TODO your code here
    xs = (fullname)
    name_list = xs.split()

    initials = ""

    for name in name_list:
      initials += name[0].upper()

    return initials

    first = name_list[0][0]

    second = name_list[1][0]

    third = name_list[2][0]

    return(first.upper())

    return(first.upper() + second.upper())

    return(first.upper() + second.upper() + third.upper())

answer = get_initials("Matthew Lee Rey")
print("The initials of 'Matthew Lee Rey' are", answer)

def main():
    name = input("What is your name?")
    print(name)
    person = get_initials(name)
    print(person)
    

if __name__ == '__main__':
    main()