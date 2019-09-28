from random import choice

#
# questions = [
#     "Why is the sky blue?:",
#     "Why is there a face in the moon?:",
#     "Where are all the dinosaurs"
# ]
#
# question = choice(questions)
# answer = input(question).strip().lower()
# just_because = "just because"
#
# while answer != just_because:
#     answer = input("why?").strip().lower()
#
# print("Oh... Okay")

s = "abcdefghijklmnopqrstuvwxyz"
vowel = 0

for letter in s:
    if letter.lower() in "aeiou":
        vowel += 1
print("Number of Vowel :" + str(vowel))

s = "obobolhgioobobomwbobovbobobobobbobob"
numbob = 0
index = 0
for char in s:
    index = s.find('bob')
    if index >= 0:
        numbob +=1
        s = s[index+1:]
print('Number of times bob occurs is: ' + str(numbob))

