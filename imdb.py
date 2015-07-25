from pyquery import PyQuery as pq

def getTop100ByYear(year):
    url1 = 'http://www.imdb.com/search/title?sort=moviemeter,asc&start=1&title_type=feature&year=%d,%d' % (year,year)
    url2 = 'http://www.imdb.com/search/title?sort=moviemeter,asc&start=51&title_type=feature&year=%d,%d' % (year,year)

    results = []
    
    for url in [url1,url2]:
        d = pq(url=url)
        movies = d('tr.detailed')
        for movie in movies.items():
            # print movie
            # print "=----------------------------="
            obj = {}
            obj['rank'] = int(movie.children('.number').text()[:-1])
            z = movie.children('td.title > a')
            obj['title'] = z.text()
            obj['imdb_id'] = z.attr['href'][7:-1]
            obj['title'] = movie.children('td.title > a').text()
            obj['year'] = int(movie.children('td.title > span.year_type').text()[1:-1])
            obj['outline'] = movie.children('td.title > span.outline').text()
            obj['genres'] = movie.children('td.title > span.genre').text().split(' | ')
            obj['rated'] = movie.children('td.title > span.certificate > span').attr['title']
            
            try:
                # get runtime info; could be missing
                obj['runtime'] = int(movie.children('td.title > span.runtime').text().split()[0])
            except:
                obj['runtime'] = None
            
            try:
                # get user rating info; could be missing
                z = movie.children('td.title > div.user_rating > div.rating').attr['title']
                z = z.split()
                # normalize on a scale of 0 to 100
                obj['rating'] = int(z[3][:-3].replace('.',''))
                obj['numratings'] = int(z[4][1:].replace(',',''))
            except:
                obj['rating'] = None
                obj['numratings'] = None
            
            #print obj
            results.append(obj)
            

    return results
    #.map(lambda i,e: pq(this).text())

##    results = []
##
##    for m in movies.items():
##        thisobj = {}
##        
##        for i,e in enumerate(m.children().items()):
##            text = e.text()
##            
##            if i == 0:
##                thisobj['rank'] = int(text[:-1])
##            elif i == 1:
##                thisobj['rating'] = int(text[:-1])
##            elif i == 2:
##                thisobj['title'] = text
##            elif i == 3:
##                thisobj['numratings'] = int(text)
##
##        results.append(thisobj)
##        
##    return results

if __name__ == "__main__":
    a = getTop100ByYear(2015)
    for b in a:
        print b
