# program that ask the user phone number and print the the number in alphabets 
# create a dictionary that maps digits to their corresponding words
digit_to_word = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',   
    '9': 'nine'
}
# ask the user for their phone number
phone_number = input("Please enter your phone number: ")
# convert the phone number to words using the dictionary
phone_number_in_words = ""
for digit in phone_number:
    phone_number_in_words += digit_to_word[digit] + " "
print(phone_number_in_words)
# program that ask the user for a word and print the number of times each letter appears in the word
# create a dictionary to store the count of each letter
letter_count = {}
# ask the user for a word
word = input("Please enter a word: ")
# count the occurrences of each letter
for letter in word:
    letter_count[letter] = letter_count.get(letter, 0) + 1
# print the count of each letter
for letter, count in letter_count.items():
    print(f"{letter}: {count}")
    
message = input("Enter a message: ")    

words = message.split(" ")  

emojis = {
    ":)": "😊",
    ":(": "😢",
    "3>": "❤️",
    "(:": "😠",
}
for word in words:
    if word in emojis:
        print(emojis[word], end=" ")
    else:
        print(word, end=" ")