from birthday_dict import birthday
import insert_birthday
import lookup_birthday
import json


# The function receive the user selection from the option - "insert", "lookup", "quit" , check and return the selection
def input_user_chooses() -> str:

    r = "\033[4;1;31m"
    b = "\033[1;0m"

    option = ("insert", "lookup", "quit")
    while True:
        user_chooses = input("Do you want to 'insert' a new birthday, to 'lookup' one or 'quit'? ").strip().lower()
        if user_chooses.isalpha and user_chooses in option:
            return user_chooses
        else:
            print(f"\n{r}please enter one of these names: 'insert', 'lookup', 'quit'{b}\n")


# "insert", "lookup", "quit"
if __name__ == "__main__":

    start_or_quit = True
    name = input("Please enter your name: ")

    # if the count is 1 the welcome explanation will not be printed.
    count_app = 0
    while start_or_quit:

        if count_app == 0:
            print(f"\nWelcome {name}."
                  f"\nyou have reached the birthdays app\n"
                  f"in this app you can 'insert' a new birthday or to 'lookup' on one\n"
                  f"If you want to get out from the program write 'quit'\n")
        else:
            print(f"\nHay {name},")
            # print(f"Welcome {name} to the birthday dictionary")

        selection = input_user_chooses()

        if selection == 'insert':
            insert_birthday.main_insert()
        elif selection == 'lookup':
            lookup_birthday.main_lookup()
            pass
        else:
            start_or_quit = False

        if count_app == 1:
            continue
        else:
            count_app = 1

        # print(birthday)


    print("Bay-bay")




# name = 'yael'
# date = 10_11_1992
# birthday = {}

#birthday[name] = date

# birth = {name: date}
# birthday.update(birth)
# print(birthday)