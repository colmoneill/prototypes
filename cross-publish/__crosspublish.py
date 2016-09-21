#!/usr/bin/env python

# settings for user:
# wikiusername =
# wikipassword =

import argparse
import mwclient
import pypandoc

parser = argparse.ArgumentParser(description='Cross publish your texts to Mediawikis and git repos')
parser.add_argument('-f', '--file', type=argparse.FileType('r'), help='your input text file', required=True)
parser.add_argument('-wp', '--wikipage', help='name of the wiki page to post to. If this page does not exist it will be created.', required=True)
args = parser.parse_args()

input = args.file.name
output = pypandoc.convert_file(input, 'mediawiki')
site = mwclient.Site('pzwiki.wdka.nl', '/mw-mediadesign/')
site.force_login = True
site.login(wikiusername, wikipassword)
wikipagename = args.wikipage
page = site.pages['User:' + username + '/'+ wikipagename]
page.save(output, 'version pushed from crosspublish.py')
print 'Converted ' + input + ' to mediawiki syntax and published on ' + 'https://pzwiki.wdka.nl/mw-mediadesign/' 'User:' + username + '/'+ wikipagename
