import source
from os import listdir
from os import system
while True:
    word_list_path = "\\".join(__file__.split("\\")[:-1]) + "\\word_lists\\"

    print("Choose one of the word lists below:")
    for i in listdir(word_list_path):
        i = i.rstrip(".txt")
        print(i, sep="\n")
    print("\nTo exit the program, type 'exit the program'.")
    dict_selection = input("\nYour choice: ")
    
    if dict_selection == "exit the program":
        break

    system("cls")

    language = input("\nLanguage (eng to tr / tr to eng)\n\nTo exit the program, type 'exit the program'.\n\nYour choice: ")
    if language == "exit the program":
        break

    system("cls")

    r = source.word_training(dict_selection, source.language_select(language))