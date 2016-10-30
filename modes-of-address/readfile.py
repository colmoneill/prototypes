import re
from nltk.tokenize import sent_tokenize, word_tokenize
file = open("en_GB.po", "r")

## not sure about the approach here; do I parse the content of the .po
## file myself or do I feed it straight into NLTK?
## option 1
content = file.read()
#print content
match = re.findall(r"msgstr\s\"([^\"\\]*)\"", content)
match = " ".join(match)
match = match.decode('utf8')
print match
#print(sent_tokenize(match))

## option 2
content = content.decode('utf8')
#print(sent_tokenize(match))
#print(sent_tokenize(content))
