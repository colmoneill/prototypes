#!/usr/bin/env python

import argparse
import mwclient
import pypandoc
import os
from git import *
import gitpath # pip install git+https://github.com/maxnoe/python-gitpath
from datetime import datetime
from time import gmtime, strftime
join = os.path.join

# settings for user:
# wikiusername = your /mediadesign mw username
# wikipassword = your pw

parser = argparse.ArgumentParser(description='Cross publish your texts to Mediawikis and git repos')
parser.add_argument('-f', '--file', type=argparse.FileType('r'), help='your input text file', required=True)
parser.add_argument('-wp', '--wikipage', help='name of the wiki page to post to. If this page does not exist it will be created.', required=True)
args = parser.parse_args()

# publish to mediawiki
input = args.file.name
output = pypandoc.convert_file(input, 'mediawiki')
now = datetime.now
site = mwclient.Site('pzwiki.wdka.nl', '/mw-mediadesign/')
site.force_login = True
site.login(wikiusername, wikipassword)
wikipagename = args.wikipage
page = site.pages['User:' + wikiusername + '/'+ wikipagename]
timenow = datetime.now()
now = strftime("%Y-%m-%d %H:%M:%S", gmtime())
automatic_edit_summary = 'version pushed from crosspublish.py at ' + now
print (automatic_edit_summary)
page.save(output, automatic_edit_summary)
print('Converted ' + input + ' to mediawiki syntax and published on ' + 'https://pzwiki.wdka.nl/mw-mediadesign/' 'User:' + wikiusername + '/'+ wikipagename)

#publish to a git repo
gitrepo = gitpath.root()
repo = Repo(gitrepo)
index = repo.index
gitinput = os.path.abspath(input)
index.add([gitinput])
index.commit(automatic_edit_summary)
git = repo.git
git.push()
print("Pushed " + input + "to " + gitrepo )
