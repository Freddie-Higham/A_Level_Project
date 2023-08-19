word_1 = list(input("Enter the first word: "))
word_2 = list(input("Enter the second word: "))

works = True

for letter_1 in word_1:
    letter_found = False
    for letter_2 in word_2:
        if letter_1 == letter_2 and not letter_found:
            letter_found = True
            word_2.remove(letter_2)
        
    if not letter_found:
        works = False

print(works)
