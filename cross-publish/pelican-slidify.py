#!/usr/bin/env python

import argparse
import pypandoc
import os
from itertools import islice
from git import *
join = os.path.join

parser = argparse.ArgumentParser(description='convert markdown to W3c slidy while keeping document keys')
parser.add_argument('-f', '--file', type=argparse.FileType('r'), help='your input text file', required=True)
args = parser.parse_args()



input = args.file.name
# get first 4 lines of input doc
with open(input) as myfile:
    head = myfile.readlines()[0:5]
    changetitle = head[0].split(':')
    changetitle[0] = changetitle[0] + ': '
    changetitle[1] = 'slides' + changetitle[1]
    head[0] = ''.join(changetitle)
    head[3] = 'Status: published\n'
    print head
    head = ''.join(head).encode('utf-8')
    #print head
    output = pypandoc.convert_file(input, 'slidy').encode('utf-8')
    slidy_output = head + output
    #print slidy_output
    generated_slidy = open(input + ".slidy.md", 'w')
    generated_slidy.write(slidy_output)
    generated_slidy.close()
    print('converted input markdown to slidy and kept top of file:\n' + head)
#print head
#slidy = open(input + '.slidy.md', 'w')

    #
    # generated_html = pypandoc.convert_file(input, 'html5')
    # html_output = open(input + '.html', 'w')
    # html_output.write(generated_html)
    # html_output.close()
    # print('Wrote out html version to file: ' + input + '.html')
