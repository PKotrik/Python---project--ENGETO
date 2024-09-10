# """
# projekt_1.py: první projekt do Engeto Online Python Akademie
# author: Patricia Kotrik Iliasova
# email: iliasovap@gmail.com
# discord: iliasovap_54684
# """

TEXTS = [
    """
    Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30N and the Union Pacific Railroad,
    which traverse the valley.""",
    """At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.""",
    """The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.""",
]

existing_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
}

divider = "----------------------------------------"

user = input("Zadejte jmeno: ")
password = input("Zadejte heslo: ")

if user in existing_users and password == existing_users[user]:
    print(f"Ahoj uzivateli {user}! Pokracuj zvolenim textu.")

    chosen_text = input("Cislo textu: ")

    if chosen_text.isdigit():
        if int(chosen_text) >= 1 and int(chosen_text) <= 3:
            print("Text byl zvolen spravne!")

            chosen_index = int(chosen_text) - 1
            wordcount = 0
            wordcount_title = 0
            wordcount_upper = 0
            wordcount_lower = 0
            number_count = 0
            number_sum = 0

            list_of_words = []
            word_length = {}
            length_occurrences = {}

            for word in TEXTS[chosen_index].split():
                list_of_words.append(word.strip(",.:;"))
            for item in list_of_words:
                wordcount += 1
                word_length[item] = len(item)

                if item.istitle():
                    wordcount_title += 1
                elif item.isupper():
                    wordcount_upper += 1
                elif item.islower():
                    wordcount_lower += 1
                elif item.isdigit():
                    number_count += 1
                    number_sum += int(item)
                else:
                    continue
            for i in word_length.values():
                if i not in length_occurrences:
                    length_occurrences[i] = 1
                else:
                    length_occurrences[i] = length_occurrences[i] + 1
            sorted_length_occurrences = dict(sorted(length_occurrences.items()))

            print(
                divider,
                f"Pocet slov v textu je {wordcount}.",
                f"Pocet slov zacinajicich s velkym pismenem je {wordcount_title}.",
                f"Pocet slov psanych velkymi pismeny je {wordcount_upper}.",
                f"Pocet slov psanych malymi pismeny je {wordcount_lower}.",
                f"Pocet cisel v textu je {number_count}.",
                f"Soucet cisel v textu je {number_sum}.",
                divider,
                f"{'LEN|':>{4}}{'OCCURRENCES':^{18}}{'|NR.':<{4}}",
                divider,
                sep="\n",
            )

            for i in sorted_length_occurrences:
                print(
                    f"{(str(i) + '|'):>{4}}{'*' * sorted_length_occurrences[i]:<{18}}{('|' + str(sorted_length_occurrences[i])):<{4}}"
                )
        else:
            print("Lituji, dany text neexistuje.")
    else:
        print("Zadana hodnota musi byt cislo!")
else:
    print(
        "Lituji, byl zadan nespravny uzivatel anebo nespravne heslo. Program se ukoncuje."
    )