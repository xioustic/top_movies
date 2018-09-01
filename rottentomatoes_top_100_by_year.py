#!/usr/bin/env python

from pyquery import PyQuery as pq
import json

def getTop100ByYear(year):
    url = 'http://www.rottentomatoes.com/top/bestofrt/?year=%d' % year
    d = pq(url=url)
    movies = d('#top_movies_main > div > table > tr')

    results = []

    for m in movies.items():
        thisobj = {}
        
        for i,e in enumerate(m.children().items()):
            text = e.text()
            
            if i == 0:
                thisobj['rank'] = int(text[:-1])
            elif i == 1:
                thisobj['score'] = int(text[:-1])
            elif i == 2:
                thisobj['title'] = text[:-7]
                thisobj['year'] = int(text[-5:-1])
            elif i == 3:
                thisobj['numratings'] = int(text)

        results.append(thisobj)
        
    return results

if __name__ == "__main__":
    import sys

    def print_help():
        print "Usage: ./"+sys.argv[0],"[-h | <year>]"
        print "Print JSON of top 100 movies according to RottenTomatoes per given year."
        print ""
        print "  -h    Show this help."

    try:
        first_arg = sys.argv[1]
    except:
        print 'Error: Invalid number of arguments'
        print_help()
        sys.exit(1)

    if first_arg == '-h':
        print_help()
        sys.exit()

    try:
        year = int(first_arg)
    except:
        print 'Error: Year must be an integer'
        sys.exit(1)

    a = getTop100ByYear(year)
    print json.dumps(a, indent=2, sort_keys=True)
