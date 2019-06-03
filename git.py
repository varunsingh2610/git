#!/usr/bin/python3
# from git import Repo

import sh
git = sh.git.bake(_cwd='/home/varun.singh/Dev/')
print (git.status())
# checkout and track a remote branch
# print git.checkout('-b', 'somebranch')
# # add a file
# print git.add('somefile')
# # commit
# print git.commit(m='my commit message')
# # now we are one commit ahead
# print git.status()
