#! /usr/bin/env python

import os
from git import Repo
join = os.path.join

repo = Repo('/home/colm/git/prototypes/')

repo.config_reader()
cw = repo.config_writer()
cw.release()

print cw
