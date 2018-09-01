from pyquery import PyQuery as pq

def getTop100ByYear(year):
    url = 'http://www.metacritic.com/browse/movies/score/metascore/year/filtered?year_selected=%d' % year

    results = []
    
    d = pq(url=url, headers={'user-agent': 'pyquery'})
    #print d
    movies = d('div.product_row.movie')
    print len(movies)
    for movie in movies.items():
        obj = {}
        obj['rank'] = int(movie.children('div.row_num').text()[:-1])
        obj['score'] = int(movie.children('div.product_score').text())
        obj['title'] = movie.children('div.product_title').text()

        z = movie.children('div.product_userscore_txt').text()[6:].replace('.','')
        if z == 'tbd':
            obj['rating'] = None
        else:
            obj['rating'] = int(z)

        obj['releasedate'] = movie.children('div.product_date').text()
        
        #print obj
        results.append(obj)        

    return results
    
if __name__ == "__main__":
    a = getTop100ByYear(2004)
    for b in a:
        print b
