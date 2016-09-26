# prototypes

Collects tiny tiny prototypes, experiments with items I'm working on (currently in the context of my self directed research at PZI).

## prototypes project & directory listing

* [tips-by-tools](/tips-by-tools)

  Tooltips are not used enough. Tooltips rely on an active curiosity that does not directly depend on a commitment. The idea of tooltips could be used to switch out modes of address from practical and direct to intimate and dialogic.

* [scrollometer](/scrollometer)

  A WebExtension that keeps an eye on how much you've scrolled today. [Scrolling is a metric, scrolling in narration.](https://pzwiki.wdka.nl/mediadesign/User:Colm/RW%26RS-scrolling-essay) Claim your metrics, be proud of your productivity.

* [Cross publish](/cross-publish)

  Maybe a PZI student specific workflow: call this script to cross publish your local text files to the [MDwiki](https://pzwiki.wdka.nl/mediadesign/Main_Page) and push to your git repo.
  I suggest saving this in your ~/bin, making it executable after answering the settings, and reviewing the usage like so:
  $ crosspublish.py -h

  ```
colm@debian-co:~$ crosspublish.py -h
usage: crosspublish.py [-h] -f FILE -wp WIKIPAGE [-m MESSAGE] [-ng] [-i]

Cross publish your texts to Mediawikis and git repos

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Your input text file
  -wp WIKIPAGE, --wikipage WIKIPAGE
                        Name of the wiki page to post to. If this page does
                        not exist it will be created. FYI, all of these pages
                        get posted to your namespace on the mdwiki.
  -m MESSAGE, --message MESSAGE
                        Your edit summary and commit message, use quotes for
                        strings. If not provided an automatic message is
                        placed with a timestamp.
  -ng, --nogit          Use this flag if youre not pushing to a git
                        repository.
  -i, --index           Adds a link to the published page on your wiki index
                        page.

  ```
