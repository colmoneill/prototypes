import nltk
import gettext
import json

pofile = 'en_GB.json'

#try:
#    load_json_file(pofile)
#except InvalidDataException:
#    # not valid
#    print('not valid')
#nltk.data.path=['en_GB.json']
nltk.data.load('en_GB.json')
nltk.read()
