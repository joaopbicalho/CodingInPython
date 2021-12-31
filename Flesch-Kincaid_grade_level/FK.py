#opens the file data2.txt and prints all the lines in it that contain the the word “lol”
#in any mixture of upper and lower case 
f = open("data2.txt")
text = f.read()
lines = text.split("\n")
print(lines)
for i in range(len(lines)):
    if ((lines[i].lower()).find("lol") != -1):
        print(lines[i])

def dict_to_str(d):
    '''Return a str containing each key and value in dict d.
    Keys and values are separated by a comma. Key-value pairs separated by a newline character from each other'''
    new_str = ""
    for key, value in d.items():
        new_str += (str(key) + ", ")
        new_str += (str(value) + "\n")
    return new_str

d = {"CAN": 80, "USA": 75, "GER": 88}
print(dict_to_str(d))

def dict_to_str_sorted(d):
    """Return a str containing each key and value in dict d.
    Keys and values are separated by a comma. Key-value
    pairs are separated by a newline character from each
    other, and are sorted in ascending order by key.
    For example, dict_to_str_sorted({1:2, 0:3, 10:5}) should
    return "0, 3\n1, 2\n10, 5". The keys in the string must
    be sorted in ascending order."""
    c = ""
    L = []
    for key, value in d.items():
        a = str(key) + ", " + str(value) + "\n"
        L.append(a)
    b = sorted(L)
    for i in range(len(L)):
        c += str(b[i])
    return c

d = {1:30, 4:5, 2:6, -3:7}

#Create a Python dictionary whose keys are words, and whose values are lists of phones.
f2 = open("cmudict-0.7b.txt")
text = f2.read()
lines = text.split("\n")
phone_dict = {}
for i in range(len(lines)):
    key_value = lines[i].split("  ")
    phones = key_value[1].split(" ")
    phone_dict[key_value[0]] = phones

f3 = open("cmudict-0.7b.phones.txt")
text = f3.read()
lines = text.split("\n")
vowel_dict = {}
for i in range(len(lines)):
    key_value = lines[i].split("\t")
    vowel_dict[key_value[0]] = key_value[1]
print(vowel_dict)

#takes in a word and returns the number of vowels in that word
def vowels_calc(word, dictp, dictv):
    word = word.upper()
    phones = dictp[word]
    vowels = 0
    for i in range(len(phones)):
        phones[i] = phones[i].replace("0", "")
        phones[i] = phones[i].replace("1", "")
        phones[i] = phones[i].replace("2", "")
        for key, value in dictv.items():
            if (key == phones[i]):
                if (value == "vowel"):
                    vowels += 1
    return vowels

#evaluates the Flesch-Kincaid Readability Grade level of a text.
def FK_grade(text, dictp, dictv):
    text += " "
    sentences = text.split(". ")
    del sentences[-1]
    words = []
    num_syll = 0
    num_words = 0
    for i in range(len(sentences)):
        words.append(sentences[i].split(" "))
        for j in range(len(words[i])):
            num_words += 1
            num_syll += num_vowels(words[i][j], dictp, dictv)
    num_sentences = len(sentences)
    return (0.39*(num_words/num_sentences) + 11.8*(num_syll/num_words) - 15.59)

# Test case
FK_grade("Hi. My name is Joao. This is a nondescript sentence. I am merely testing the grade of my lexicon.", phone_dict, vowel_dict)

