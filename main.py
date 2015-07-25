from movies import normalize
import imdb
import metacritic
import rottentomatoes

import sqlite3

config = {
  "dbfile": "top_movies.db",
  "years": range(2015-25,2015),
  "do_imdb": True,
  "do_rt": True,
  "do_mc": True
}

conn = sqlite3.connect(config['dbfile'])

c = conn.cursor()

def get_or_create(normalize_title,year=None):
  # gets or creates a movie entry by normalized title and, optionally, year
  # returns the corresponding row id number in the movies database

  # try for normalized title plus imdbyear
  c.execute("SELECT id FROM movies WHERE normalize_title=? AND imdb_year=?", (normalize_title,year))
  result = c.fetchone()
  if result: return result[0]

  # try for normalized title plus (imdbyear+1)
  c.execute("SELECT id FROM movies WHERE normalize_title=? AND imdb_year=?", (normalize_title,year+1))
  result = c.fetchone()
  if result: return result[0]

  # try for normalized title plus (imdbyear-1)
  c.execute("SELECT id FROM movies WHERE normalize_title=? AND imdb_year=?", (normalize_title,year-1))
  result = c.fetchone()
  if result: return result[0]

  # try for normalized title plus rtyear
  c.execute("SELECT id FROM movies WHERE normalize_title=? AND rt_year=?", (normalize_title,year))
  result = c.fetchone()
  if result: return result[0]

  # try for normalized title plus (rtyear+1)
  c.execute("SELECT id FROM movies WHERE normalize_title=? AND rt_year=?", (normalize_title,year+1))
  result = c.fetchone()
  if result: return result[0]

  # try for normalized title plus (rtyear-1)
  c.execute("SELECT id FROM movies WHERE normalize_title=? AND rt_year=?", (normalize_title,year-1))
  result = c.fetchone()
  if result: return result[0]

  # finally, give up and create it
  c.execute("INSERT INTO movies (normalize_title) VALUES (?)",(normalize_title,))
  return c.lastrowid

c.execute('''CREATE TABLE IF NOT EXISTS movies
  (id INTEGER PRIMARY KEY AUTOINCREMENT, normalize_title TEXT, 
   imdb_id TEXT, imdb_rank INTEGER, imdb_title TEXT, imdb_year INT, imdb_outline TEXT, imdb_genres TEXT,
   imdb_rated TEXT, imdb_runtime INTEGER, imdb_rating INTEGER, imdb_numratings INTEGER,
   rt_rank INTEGER, rt_score INTEGER, rt_title TEXT, rt_year INTEGER, rt_numratings INTEGER,
   mc_rank INTEGER, mc_score INTEGER, mc_title TEXT, mc_rating INTEGER, mc_releasedate TEXT)''')

if config.get('do_imdb'):
  # do imdb set first
  print "Getting IMDB Set"

  for year in config['years']:
    print "Doing IDMB Year %d" % year

    movies = imdb.getTop100ByYear(year)

    for movie in movies:
      #print u'Working on #%d. %s (%d)' % (movie['rank'],movie['title'],movie['year'])

      normalized_title = normalize(movie['title'])
      #print u"Normalized: %s" % normalized_title

      this_id = get_or_create(normalized_title,movie['year'])
      print "Got id %d (%s,%s)" % (this_id,normalized_title,movie['year'])

      # augment the dict so it can be passed to the execute statement below
      movie['id'] = this_id
      movie['genres'] = ', '.join(movie['genres'])

      c.execute('''UPDATE movies SET imdb_id=:imdb_id, imdb_rank=:rank, imdb_title=:title, imdb_year=:year, imdb_outline=:outline,
                                     imdb_genres=:genres, imdb_rated=:rated, imdb_runtime=:runtime,
                                     imdb_rating=:rating, imdb_numratings=:numratings WHERE id=:id''', movie)

    # commit at the end of each year
    conn.commit()

# following runs should look forward and backward one year just in case discrepancy
config['years'] = [min(config['years'])-1] + config['years'] + [max(config['years'])+1]

if config.get('do_rt'):
  print "Getting RT Set"

  for year in config['years']:
    print "Doing RT Year %d" % year

    movies = rottentomatoes.getTop100ByYear(year)

    for movie in movies:
      normalized_title = normalize(movie['title'])
      this_id = get_or_create(normalized_title,movie['year'])
      print "Got id %d (%s,%s)" % (this_id,normalized_title,movie['year'])
      movie['id'] = this_id

      c.execute('''UPDATE movies SET rt_rank=:rank, rt_score=:score, rt_title=:title, rt_year=:year, 
                                     rt_numratings=:numratings WHERE id=:id''', movie)

  conn.commit()

if config.get('do_mc'):
  print "Getting MC Set"

  for year in config['years']:
    print "Doing MC Year %d" % year

    movies = metacritic.getTop100ByYear(year)

    for movie in movies:
      normalized_title = normalize(movie['title'])

      movie['year'] = int(movie['releasedate'][-4:])

      this_id = get_or_create(normalized_title,movie['year'])
      print "Got id %d (%s,%s)" % (this_id,normalized_title,movie['year'])
      movie['id'] = this_id

      c.execute('''UPDATE movies SET mc_rank=:rank, mc_score=:score, mc_title=:title, mc_rating=:rating,
                                     mc_releasedate=:releasedate WHERE id=:id''', movie)

  conn.commit()

conn.close()
