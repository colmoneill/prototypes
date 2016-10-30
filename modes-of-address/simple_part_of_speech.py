import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
from operator import itemgetter
from collections import Counter

### POS tag list:
###
### CC	coordinating conjunction
### CD	cardinal digit
### DT	determiner
### EX	existential there (like: "there is" ... think of it like "there exists")
### FW	foreign word
### IN	preposition/subordinating conjunction
### JJ	adjective	'big'
### JJR	adjective, comparative	'bigger'
### JJS	adjective, superlative	'biggest'
### LS	list marker	1)
### MD	modal	could, will
### NN	noun, singular 'desk'
### NNS	noun plural	'desks'
### NNP	proper noun, singular	'Harrison'
### NNPS	proper noun, plural	'Americans'
### PDT	predeterminer	'all the kids'
### POS	possessive ending	parent's
### PRP	personal pronoun	I, he, she
### PRP$	possessive pronoun	my, his, hers
### RB	adverb	very, silently,
### RBR	adverb, comparative	better
### RBS	adverb, superlative	best
### RP	particle	give up
### TO	to	go 'to' the store.
### UH	interjection	errrrrrrrm
### VB	verb, base form	take
### VBD	verb, past tense	took
### VBG	verb, gerund/present participle	taking
### VBN	verb, past participle	taken
### VBP	verb, sing. present, non-3d	take
### VBZ	verb, 3rd person sing. present	takes
### WDT	wh-determiner	which
### WP	wh-pronoun	who, what
### WP$	possessive wh-pronoun	whose
### WRB	wh-abverb	where, when

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
#output2.write( count_pos )
#output2.close()
