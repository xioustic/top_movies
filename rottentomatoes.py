from pyquery import PyQuery as pq

def getTop100ByYear(year):
    url = 'http://www.rottentomatoes.com/top/bestofrt/?year=%d' % year
    d = pq(url=url)
    movies = d('#top_movies_main > div > table > tr')
    #.map(lambda i,e: pq(this).text())

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
    a = getTop100ByYear(2004)
    for b in a:
        print b
