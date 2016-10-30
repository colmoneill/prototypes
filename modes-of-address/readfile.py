import re

file = open("en_GB.po", "r")
content = file.read()
#print content
match = re.findall(r"msgstr\s\"([^\"\\]*)\"", content)
print match
