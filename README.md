2015-07-25

What This Does
==============
The intent of this project is to assist with finding good movies, according to aggregated scores from various sources, and then checking to see if the movies exist in your movie collection.

Presently, this is being developed for use with Kodi media libraries that are backed by MySQL. There is an intention to support other Kodi database stores in the future. Perhaps later support could be provided for a simple set of sanely named files/folders.

Targets for score aggregation include:
- IMDB Yearly Rank (Out of 100)
- IMDB User Rating
- RottenTomatoes Yearly Rank (Out of 100)
- RottenTomatoes Score
- MetaCritic Yearly Rank (Out of 100)
- MetaCritic User Rating

Scores are aggregated, paired using normalized movie titles, and information scraped placed into a local SQlite database. Final score used in audit is calculated by normalizing all score aggregations 0 to 100 (higher is better) and then multiplying to get final score.

Dependencies
============
1. You'll need MySQLdb in order to audit your Kodi/XBMC Database: https://pypi.python.org/pypi/MySQL-python
2. You'll need PyQuery which powers the scraping mechanisms for retrieving movie information from the rating sites: https://pypi.python.org/pypi/pyquery
3. You'll probably need a MySQL browser to figure out your schema for the auditing configuration step; I'd recommend HeidiSQL: http://www.heidisql.com/

Basic Instructions
==================
1. Install Python 2.7.
2. Retrieve and install the dependencies above.
3. Open main.py and modify the config for the range of years you want, and set the booleans for each aggregator source.
4. Run main.py. It will take awhile; it's scraping all the aggregators and populating/updating the sqlite database.
5. Open audit.py and modify the config for the MySQL configuration of your Kodi library.
6. Run audit.py. When finished, open audit.html which should display a table of data for what movies you have and what you don't.