import re

year_re = re.compile(r'\(\d{4}\)\s*$')
rev_article_re = re.compile(r'^(.*?),\s*(the|an?)\s*$', re.I)
articles_re = re.compile(r'^\s*(the|an?)\s+', re.I)
badchars_re = re.compile(r'[^a-z0-9 ]', re.I)
whitespace_re = re.compile(r'\s+')
and_re = re.compile(r'\s+and\s+', re.I)

def normalize(name):
    name = year_re.sub('', name)              # strip trailing year
    name = rev_article_re.sub(r'\2 \1', name) # Movie, The = The Movie
    name = articles_re.sub('', name)          # strip leading the/an
    name = badchars_re.sub(' ', name)         # only allow alnum
    name = name.lower()                       # lowercase only
    name = name.strip()                       # strip whitespace
    name = whitespace_re.sub(' ', name)       # compress whitespace
    name = and_re.sub(' ', name)              # the word "and"

    return name