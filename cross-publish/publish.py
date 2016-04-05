#! /usr/bin/env python

import mwclient
import sys

def replace_page(wikiname,
                 wikibasepath,
                 pagename,
                 username,
                 password,
                 contents):
    site = mwclient.Site(wikiname,
                         wikibasepath,
                         force_login=True)
    site.login(username, password)
    page = site.Pages[pagename]
    some = page.edit()
    page.save(contents, summary='generated page update from script')

def main():
    wikiname='http://pzwart2.wdka.hro.nl'
    wikibasepath="/mw-mediadesign/"  # This assumes that your wiki pages all reside under http://wiki.mydomain.com/wiki/

    pagename='User:Colm/dump/'

    username="Colm"
    password=""
    contents=sys.stdin.read()
    replace_page(wikiname,
                 wikibasepath,
                 pagename,
                 username,
                 password,
                 contents)
