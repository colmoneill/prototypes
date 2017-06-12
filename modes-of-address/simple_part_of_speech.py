import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
from operator import itemgetter
from collections import Counter

file = open("en_GB.po", "r")
output = open('tagged_language.txt', 'w')
output2 = open('occurences_of_language.txt', 'w')
## not sure about the approach here; do I parse the content of the .po
## file myself or do I feed it straight into NLTK?
## option 1
content = file.read()
#print content
match = re.findall(r"msgstr\s\"([^\"\\]*)\"", content)
match = " ".join(match)
match = match.decode('utf8')

text = word_tokenize(match)
processed = nltk.pos_tag(text)
sorted_processed = sorted(processed,key=itemgetter(1))
#print (sorted_processed)
#for item in sorted_processed:
#    print>>output, item

counter = (Counter(sorted_processed))
#for item in counter.items():
#    print>>output2, item

count_pos = [x[1] for x in sorted_processed]
count_pos = (Counter(count_pos))
print (count_pos)
