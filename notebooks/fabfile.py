from fabric.api import *
import glob

def latex():
    files = glob.glob('*.ipynb')
    for fname in files:
        local('python exportlatex.py %s' % fname)
