from nltk.corpus import wordnet

syns = wordnet.synsets("program")
print(syns)

file = open("all_inkscape_interface_text.txt", "r")
