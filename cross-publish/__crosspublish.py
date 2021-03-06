#!/usr/bin/python3

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
parser.add_argument('-i', '--index', action='store_true', help='Adds a link to the published page on your wiki index page.')
parser.add_argument('-html', '--make_html', action='store_true', help='Generates a html version of the file in the working directory.')
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
# adds a link to the just created or updated wiki page on the users index page
index = args.index
indexpage = site.pages['User:' + wikiusername]
if index is False:
    print('index flag not in use, continuing')
else:
    indexpage.save('\n' + '==' 'Last unsorted drafts' + '==' + '\n' + 'unsorted draft from crosspublish.py: ' + 'https://pzwiki.wdka.nl/mediadesign/' 'User:' + wikiusername + '/'+ wikipagename , section='14')
    print('Added link to published wiki page on ' + wikiusername + 's index page')
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
html = args.make_html
if html is False:
    print('no html version generated')
else:
    generated_html = pypandoc.convert_file(input, 'html5')
    html_output = open(input + '.html', 'w')
    html_output.write(generated_html)
    html_output.close()
    print('Wrote out html version to file: ' + input + '.html')
