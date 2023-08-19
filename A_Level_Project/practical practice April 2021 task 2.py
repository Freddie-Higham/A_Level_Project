n = int(input("How many nunbers do you want to input: "))
numbers = input(f"Enter the {n} numbers: ")
numbers = numbers.split(", ")

dictionary = {}

for number in numbers:
    dictionary[number] = 0

print(dictionary)

for number in numbers:
    dictionary[number] += 1

highest_number = -1
multimodal = False
for number in dictionary:
    print(f"{int(dictionary[number])} > {highest_number}")
    if int(dictionary[number]) > highest_number:
        multimodal = False
        highest_number = dictionary[number]
    elif int(dictionary[number]) == highest_number:
        multimodal = True

if multimodal:
    print("Data was multimodal")
else:
    print(f"{highest_number} was the highest with a frequency of {dictionary[highest_number]}")
