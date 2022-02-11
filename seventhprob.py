import re
from string import ascii_letters
from collections import Counter

def most_frequent(words):
    occurence_count = Counter(words)
    return occurence_count.most_common(1)[0][0]

text_file = open("two_cities_ascii.txt", "r")
text = text_file.read()
allowed = set(ascii_letters + ' ')
text = ''.join(l for l in text if l in allowed)
text = text.lower()
lst = re.sub("[^\w]", " ",text).split()
j = 0
dictionary = {}
k=0
for i in range(0, len(lst), 3) :
    if (i + 3) <= len(lst) :
        dictionary[k] = {
        "firstword" : lst[j],
        "secondword" : lst[j+1],
        "thirdword" : lst[j+2]
        }
        k = k + 1
        j = j + 3
print("Τα διαθέσιμα κλειδιά είναι τα: firstword, secondword, thirdword")
print("Παρακαλώ πληκτρολογήστε ένα από τα παραπάνω κλειδιά.")
wrong = True
while wrong :
    user = input()
    if user == "firstword" or user == "secondword" or user == "thirdword" :
        wrong = False
    else :
        print("Παρακαλώ προσπαθήστε ξανά, έτσι ώστε η απάντηση σας να εμφανίζεται στα παραπάνω κλειδιά.")
max = dictionary[1].get(user)
for i in range(len(dictionary)) :
    if dictionary[i].get(user) > max :
        max = dictionary[i].get(user)
print("Η μεγαλύτερη τιμή για αυτό το κλειδί: ", max)
min = dictionary[1].get(user)
for i in range(len(dictionary)) :
    if dictionary[i].get(user) < min :
        min = dictionary[i].get(user)
print("Η μικρότερη τιμή για αυτό το κλειδί: ", min)
words = []
for i in range(len(dictionary)) :
    words.append(dictionary[i].get(user))
print("Η πιο δημοφηλής λέξη για αυτό το κλειδί: ", most_frequent(words))
