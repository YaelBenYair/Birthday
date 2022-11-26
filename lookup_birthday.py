from birthday_dict import birthday






def y_n_check(y_n):
    while True:
        if y_n.isdigit() and int(y_n) == 1:
            return True
        elif y_n.isdigit() and int(y_n) == 2:
            return False
        else:
            print("\n\033[4;1;31mPlease enter a number: 1 - for yes, 2 - for no\033[1;0m")




def match(n_list, l_n_list, name1, last_name_1):
    n = False
    l_n = False
    if len(n_list) > 0:
        n = True
    if len(l_n_list) > 0:
        l_n = True
    if n or l_n:
        yes_no = input(f"\nWe couldn't find exact value matching '{name1} {last_name_1}'. Do you want to see "
                       f"suggestions?\nEnter 1 for yes, 2 for no: ").strip()
        if y_n_check(yes_no):
            print()
            if n:
                print(f"We have in name {name1}: {n_list}")
            if l_n:
                print(f"We have in last name {last_name_1}: {l_n_list}")
            choice = input("\nInsert a name from the list above or '$$$' to return to the main menu: ")
            if choice in birthday:
                print(f"\n{choice.title()}'s birthday is in {birthday.get(choice)}")
                return '$$$'
            else:
                return '$$$'
        else:
            return '$$$'

    else:
        return '$$$'







def match_search(name):
    name = name.split(" ")
    last_name = name[1]
    name = name[0]
    name_li = []
    last_name_li = []
    for key in birthday:
        if name in key:
            name_li.append(key)
        elif last_name in key:
            last_name_li.append(key)
    return match(name_li, last_name_li, name, last_name)







def main_lookup():

    match_s = True

    while match_s:
        name_look = input("\nwho's birthday do you want to look up? ").strip().lower()

        if name_look in birthday:
            print(f"\n{name_look.title()}'s birthday is in {birthday.get(name_look)}")
            match_s = False
        else:
            rename = match_search(name_look)
            if rename == '$$$':
                print(f"\nWe dont have record for {name_look.title()}")
                match_s = False
