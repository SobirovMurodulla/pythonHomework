#1-question
name = str(input("Enter your name : "))
year_of_birth = int(input("Enter your year of birth : "))
age = 2025-year_of_birth
print(f"{name} is {age} years old")

#2-question
txt = "LMaasleitbtui"
print("Car 1 = ", txt[0:13:2])
print("Car 2 = ", txt[1:13:2])

#3-question
word = str(input())
print(len(word))
print(word.upper())
print(word.lower())

#4-question
word2 = str(input())
mid = int(len(word2)/2)
half1 = word2[:mid]
half2 = word2[-1:mid:-1]
if half1==half2:
    print("Palindrome")
else:
    print("Not Palindrome")

#5-question
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
vowel_count = 0
consonant_count = 0
text = str(input())
for i in text:
    if i in vowels:
        vowel_count += 1
    else:
        consonant_count += 1
print("Number of vowels: ", vowel_count)
print("Number of consonants: ", consonant_count)

#6-question
string1 = str(input())
string2 = str(input())
if len(string1) > len(string2):
    if string2 in string1:
        print("Yes")
    else:
        print("No")
else:
    if string1 in string2:
        print("Yes")
    else:
        print("No")

#7-question
sentence = str(input("Sentence: "))
word_to_replace = str(input("Word to replace: "))
new_word = str(input("New word: "))
sentence = sentence.replace(word_to_replace, new_word)
print(sentence)

#8-question
string_user = str(input("Enter a string: "))
print("First letter: ", string_user[0])
print("Last letter: ", string_user[-1])

#9-question
string_input = str(input("Enter a string: "))
reversed_string = string_input[::-1]
print("Reversed string: ", reversed_string)

#10-question
word_count = 1
sentence_input = str(input("Enter a sentence: "))
words = sentence_input.split()
print("Number of words: ",len(words))

#11-question
n = str(input('Enter a string: '))
if any(char.isdigit()for char in n):
    print("Yes")
else:
    print("No")

#12-question
a = list(map(str, input().split()))
new_a = ",".join(a)
print(new_a)

#13-question

b_string = str(input("Enter a string: "))
new_b = "".join(b_string.split())
print(new_b)

#14-question
string_1 = input("Enter the first string: ")
string_2= input("Enter the second string: ")

if string_1 == string_2:
    print("Equal.")
else:
    print("Not Equal.")

#15-question
entered_string = input("Enter a sentence: ")
entered_string = entered_string.split()
acronym = ""
for word in entered_string:
    acronym += word[0].upper()
print(acronym)

#16-question

enter_a_string = str(input("Enter a string: "))
enter_a_character = str(input("Enter a character: "))
for character in enter_a_string:
    if character == enter_a_character:
        enter_a_string = enter_a_string.replace(character, "")
print(enter_a_string)

#17-question
enter_new_string = str(input("Enter a string: "))
for i in enter_new_string:
    if i in vowels:
        enter_new_string = enter_new_string.replace(i, "")
print(enter_new_string)

#18-question
enter_the_sentence = str(input("Enter a sentence: "))
enter_starting_word = str(input("Enter the starting word: "))
enter_ending_word = str(input("Enter the ending word: "))
enter_the_sentence = enter_the_sentence.split()
if enter_the_sentence[0]==enter_starting_word and enter_the_sentence[-1]==enter_ending_word:
    print("Yes")
else:
    print("No")




