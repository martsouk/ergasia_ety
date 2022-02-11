import re

text_file = open("two_cities_ascii.txt", "r")
text = text_file.read()
text_file.close()
binary = ''.join(format(ord(i),'b').zfill(7) for i in text)
list = []
for i in range(len(binary)) :
    list.append(binary[i])
count = 0
max = 0
for i in range(len(list)) :
    if list[i] == '0' :
        count = count + 1
    else :
        if count > max :
            max = count
            count = 0
print("Η μεγαλύτερη ακολουθία απο συνεχόμενα 0 είναι: ", max, "\n")
for i in range(len(list)) :
    if list[i] == '1' :
        count = count + 1
    else :
        if count > max :
            max = count
            count = 0
print("Η μεγαλύτερη ακολουθία απο συνεχόμενα 1 είναι: ", max, "\n")
