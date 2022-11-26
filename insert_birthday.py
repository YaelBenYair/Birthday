from birthday_dict import birthday


# this function receive a name from the user, check end return the name
def check_name():
    while True:
        name_user = input("\nPlease insert a full name: ").strip().lower()
        if name_user.isalpha():
            return name_user
        elif " " in name_user or "-" in name_user:
            name = name_user.split(" ")
            name = "".join(name)
            name = name.split("-")
            name = "".join(name)

            if name.isalpha():
                return name_user
            else:
                print("\n\033[4;1;31mPlease enter only letters\033[1;0m")

        else:
            print("\n\033[4;1;31mPlease enter only letters\n\033[1;0m")

# this function receive a date from the user in format dd.mm.yyyy, check end return the date
def check_date():
    while True:
        date_user = input("\nPlease insert a birthday date in format DD.MM.YYYY: ").strip()
        d_user = date_user.split(".")
        d_user_j = "".join(d_user)

        # check if we have 2 - "." in tha date
        if len(d_user) == 3:

            # check if ta date is a number
            if d_user_j.isdigit():
                return date_user
            else:
                print("\n\033[4;1;31mPlease enter only numbers\n\033[1;0m")
        else:
            print("\n\033[4;1;31mPlease enter in the requested format\n\033[1;0m")







def main_insert():

    name = check_name()
    date = check_date()

    if name in birthday:
        print("This name already exists")
    else:
        birthday[name] = date
        print("\nDone!")
    # print(birthday)






# main_insert()
