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
