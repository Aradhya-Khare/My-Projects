alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def coding_and_decoding(the_word, shift_amount, the_value):
    text = ""
    if the_value == "decode":
        shift_amount *= -1
    elif the_value == "decode":
         shift_amount *= 1
    for char in the_word:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = shift_amount + position
            new_char = alphabet[new_position]
            text += new_char
        else:
           text += char
    print(f"the {the_value}d text is {text}")

    

to_continue = True
while to_continue:
    value = input("Select you want to decode or encode: ").lower()
    word = input("Enter a word: ")
    shift = int(input("Enter a shift amount by which you want to shift the text: "))

    shift = shift % 26

    coding_and_decoding(the_word=word, shift_amount=shift, the_value= value)
    a = input("Do you want to code and decode again if yes type 'y' if no type 'n': ").lower()
    if a == "n":
        to_continue = False
    elif a == "y":
        to_continue = True
    else:
        print("Invalid input")
        to_continue = False
