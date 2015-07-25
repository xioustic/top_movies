2015-07-25

Dependencies
============
1. You'll need MySQLdb in order to audit your Kodi/XBMC Database: https://pypi.python.org/pypi/MySQL-python
2. You'll need PyQuery which powers the scraping mechanisms for retrieving movie information from the rating sites: https://pypi.python.org/pypi/pyquery

Present Limitations
===================
1. This will only operate on a MySQL database for Kodi.
2. You must be somewhat familiar with your MySQL settings that Kodi uses, as well as the schema of your working database (database, table names, and column names).
3. For auditing, this will only retrieve the top 25 movies (per combined score) for each year and check if it can find the corresponding movie in your Kodi database by IMDB id.

Basic Instructions
==================
1. Install Python 2.7.
2. Retrieve and install the dependencies above.
3. Open main.py and modify the config for the range of years you want, and set the booleans for each aggregator source.
4. Run main.py. It will take awhile; it's scraping all the aggregators and populating/updating the sqlite database.
5. Open audit.py and modify the config for the MySQL configuration of your Kodi library.
6. Run audit.py. When finished, open audit.html which should display a table of data for what movies you have and what you don't.