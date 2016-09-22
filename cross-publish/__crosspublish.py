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
parser.add_argument('-f', '--file', type=argparse.FileType('r'), help='Your input text file', required=True)
parser.add_argument('-wp', '--wikipage', help='Name of the wiki page to post to. If this page does not exist it will be created. FYI, all of these pages get posted to your namespace on the mdwiki.', required=True)
parser.add_argument('-m', '--message', help='Your edit summary and commit message, use quotes for strings. If not provided an automatic message is placed with a timestamp.')
parser.add_argument('-ng', '--nogit', action='store_true', help='Use this flag if youre not pushing to a git repository.')
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
if args.message:
    page.save(output, args.message)
else:
    page.save(output, automatic_edit_summary)
print('Converted ' + input + ' to mediawiki syntax and published on ' + 'https://pzwiki.wdka.nl/mw-mediadesign/' 'User:' + wikiusername + '/'+ wikipagename)

#publish to a git repo
nogit = args.nogit
if nogit is True:
    print('git option set to flase, finished cross publishing')
else:
    gitrepo = gitpath.root()
    repo = Repo(gitrepo)
    index = repo.index
    gitinput = os.path.abspath(input)
    index.add([gitinput])
    if args.message:
        index.commit(args.message)
    else:
        index.commit(automatic_edit_summary)
        git = repo.git
        git.push()
    print("Pushed " + input + " to " + repo.remotes.origin.url )
