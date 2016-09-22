#!/usr/bin/env python

import argparse
import mwclient
import pypandoc
import os
from git import *
import datetime
join = os.path.join

# settings for user:
# wikiusername =
# wikipassword =
# repo =
repopath = '/home/colm/git/prototypes/'
repo = Repo('/home/colm/git/prototypes/')
remoteURL = 'git@github.com:colmoneill/prototypes.git'

parser = argparse.ArgumentParser(description='Cross publish your texts to Mediawikis and git repos')
parser.add_argument('-f', '--file', type=argparse.FileType('r'), help='your input text file', required=True)
parser.add_argument('-wp', '--wikipage', help='name of the wiki page to post to. If this page does not exist it will be created.', required=True)
args = parser.parse_args()

# publish to mediawiki
input = args.file.name
output = pypandoc.convert_file(input, 'mediawiki')
now = datetime.datetime.now
site = mwclient.Site('pzwiki.wdka.nl', '/mw-mediadesign/')
site.force_login = True
site.login(wikiusername, wikipassword)
wikipagename = args.wikipage
page = site.pages['User:' + wikiusername + '/'+ wikipagename]
page.save(output, 'version pushed from crosspublish.py')
print 'Converted ' + input + ' to mediawiki syntax and published on ' + 'https://pzwiki.wdka.nl/mw-mediadesign/' 'User:' + wikiusername + '/'+ wikipagename

#publish to a git repo
git = repo.git
repo.config_reader()
cw = repo.config_writer()
index = repo.index
git.pull
git.add([input])
print 'added input to git'
index.commit("Crosspublish from script ").type == 'commit'
print 'committed automatic commit message with datetime'
git.push()
