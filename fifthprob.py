import re
from string import ascii_letters
from collections import Counter

def most_frequent(words):
    occurence_count = Counter(words)
    return occurence_count.most_common(10)

def most_frequent2(words2):
    occurence_count = Counter(words2)
    return occurence_count.most_common(3)

def most_frequent3(words3):
    occurence_count = Counter(words3)
    return occurence_count.most_common(3)


text_file = open("two_cities_ascii.txt", "r")
text = text_file.read()
text_file.close()
allowed = set(ascii_letters + ' ')
text = ''.join(l for l in text if l in allowed)
text = text.lower()
words = re.sub("[^\w]", " ",text).split()
print("Οι 10 πιο δημοφηλείς λέξεις και η συχνότητα με την οποία εμφανίζονται: ", most_frequent(words),"\n")
words3 = []
words2 = []
for i in range(len(words)) :
    if len(words[i]) >= 3 :
        words[i] = words[i][:3]
        words3.append(words[i])
    if len(words[i]) >= 2 :
        words[i] = words[i][:2]
        words2.append(words[i])
print("Τα 3 πιο συχνά δύο πρώτα γράμματα και η συχνότητα με την οποία εμφανίζονται: ", most_frequent2(words2),"\n")
print("Τα 3 πιο συχνά τρία πρώτα γράμματα και η συχνότητα με την οποία εμφανίζονται: ", most_frequent3(words3))
