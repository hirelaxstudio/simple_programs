from random import randint
from os import system
from random import choice
#################################################################################################################
def language_select (p1):
    if p1 != "eng to tr" and p1 != "tr to eng":
        return "You made the wrong language choice\n"
    else:
        return p1
#################################################################################################################
def word_training (p1, p2):
    words_keys, words_values = list(), list() 
    random_number, number_check = 0, 0
    key_to_value, value_to_key = " ", " "
    current_file_path = "\\".join(__file__.split("\\")[:-1]) + "\\word_lists\\" + f"{p1}.txt"

    try:
        with open(r"{}" .format(current_file_path), "r", encoding="utf-8") as language_file:
            raw_str_all = language_file.readlines()

            for i in range(len(raw_str_all)):
                raw_str = raw_str_all[i]
                raw_str = raw_str.split(": ")

                words_keys.append(raw_str[0])

                raw_str[1] = raw_str[1].split(", ")
                raw_str[1][-1] = raw_str[1][-1].strip("\n")
                words_values.append(raw_str[1])
    except:
        print("The list you entered is not defined or you entered an incorrect word.\n")
        return 0

    if p2 == "eng to tr" or p2 == "tr to eng":
        print("To exit the list, type 'exit the list'.\n")
        while True:
            if number_check == random_number:
                random_number = randint(0,len(words_keys)-1)
                continue 

            if p2 == "eng to tr":
                key_to_value = input("{} : ".format(words_keys[random_number]))

            elif p2 == "tr to eng":
                value_to_key = input("{} : ".format(choice(words_values[random_number])))

            if words_values[random_number].__contains__(key_to_value) or value_to_key == words_keys[random_number]:
                print("\nCorrect answer!\n")
                number_check = random_number

            elif not words_values[random_number].__contains__(key_to_value) or value_to_key != words_keys[random_number]:
                if key_to_value=="exit the list" or value_to_key=="exit the list":
                    system("cls")
                    break
                else:
                    if p2 == "eng to tr":
                        if words_values[random_number] == 1:
                            print("\nWrong answer! Correct answer is: {}\n".format(words_values[random_number]))
                        else:
                            print("\nWrong answer! Correct answers is: ", end="")
                            for i in words_values[random_number]:
                                print(f"| {i} |", end=" ")
                            print("\n")
                    elif p2 == "tr to eng":
                        print("\nWrong answer! Correct answer is: {}\n".format(words_keys[random_number]))
                    number_check = random_number
    else:
        print(p2)