from pyquery import PyQuery as pq
import json

def parseIMDBlist(url):
    results = []

    d = pq(url=url)
    movies = d('div#pagecontent div#main div.lister-list div.lister-item.mode-advanced')
    for movie in movies.items():
        movie = pq(movie)
        # print "=----------------------------="
        obj = {}
        #print movie('.lister-item-header .text-primary').text()
        #print movie.children('.lister-item-header').text()
        
        obj['rank'] = int(movie('.lister-item-header span.text-primary').text()[:-1])

        link = movie('.lister-item-header > a')
        obj['title'] = link.text()
        obj['imdb_id'] = link.attr['href'].split('/')[2]

        year_text = movie('.lister-item-header > .text-muted').text().split(' ')[-1].replace('(','').replace(')','')
        obj['year'] = int(year_text)

        obj['outline'] = movie('p.text-muted').eq(1).text()
        obj['genres'] = movie('p.text-muted').eq(0).text().split(' | ')[-1].split(', ')
        obj['rated'] = movie('p.text-muted').eq(0).text().split(' | ')[0]
        obj['runtime'] = movie('p.text-muted').eq(0).text().split(' | ')[1]
        obj['rating'] = movie('.ratings-imdb-rating > strong').text().replace('.','')
        obj['numratings'] = movie('.sort-num_votes-visible > span').eq(1).text().replace(',','')

        #print obj
        results.append(obj)
            
    return results

def getTop100ByYear(year):
    url1 = 'http://www.imdb.com/search/title?sort=moviemeter,asc&start=1&title_type=feature&year=%d,%d' % (year,year)
    url2 = 'http://www.imdb.com/search/title?sort=moviemeter,asc&start=51&title_type=feature&year=%d,%d' % (year,year)

    results = []
    
    for url in [url1,url2]:
        results += parseIMDBlist(url)

    return results

if __name__ == "__main__":
    import sys

    try:
        year_text = sys.argv[1]
    except:
        print 'Invalid number of arguments'
        sys.exit(1)

    try:
        year = int(year_text)
    except:
        print 'Argument must be an integer'
        sys.exit(1)

    a = getTop100ByYear(year)
    print json.dumps(a, indent=2, sort_keys=True)
