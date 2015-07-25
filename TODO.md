___Sources___
## themoviedb ##
TBD

## rottentomatoes top 100 year ##
URL: http://www.rottentomatoes.com/top/bestofrt/?year=2014
js: jQuery("#top_movies_main > div > table > tbody > tr > td > a.unstyled.articleLink").map(function() {return this.outerText})

## imdb top 100 year ##
URL: http://www.imdb.com/search/title?sort=moviemeter,asc&start=1&title_type=feature&year=2014,2014
URL: http://www.imdb.com/search/title?sort=moviemeter,asc&start=51&title_type=feature&year=2014,2014
js: jQuery("#main > table > tbody > tr > td > a").filter(function() {return this.outerText != ""}).map(function() {return this.outerText})

## metacritic top 100 year ##
URL: http://www.metacritic.com/browse/movies/score/metascore/year?year_selected=2014
js: jQuery("div > div > div > div > div > div > div > div > a:not([class])").map(function() {return this.outerText})

__Normalizing__
- maybe good source here: https://github.com/ToxicFrog/lancow/blob/master/madcow/modules/movie.py
- might be good to map by imdb id, since we can search by that in our media collection too probably

__Reporting__
- Display each movie with each rating (normalized to 0 thru 100)
- Display each movie with an averaged set of alll ratings
- Sort by the average rating, and then by number of ratings
- Search for the movie in local collection to see if we're missing it and print Green if we have it, Red if not

__Future Ideas__
- Set Definitive Source? (Often conflict between year)
- TV Shows?
- More Rating Sources?
- Ability to Search Torrents? (Think Sickrage/Couchpotato)
    + Kat.CR (https://kat.cr/usearch/<searchstring>%20category:movies/)
    + TPB (https://thepiratebay.mn/search/<searchstring>/0/99/200)
    + Cap Filesize Per Movie
    + Cap Filesize Per Movie Runtime
    + Search By Normalized Name; Filter Results on Year (If Fail, Use Year +- 1)
    + Score Based On:
        * Age In Days (Scalar)
        * Seeders (Scalar)
        * Leechers (Scalar)
        * VIP Uploader? (Boolean)
        * # Comments (Scalar)
        * Keywords (Boolean)
    + Boolean Scores Can Kill a Result OR Add a Score Amount
    + Scalar Results Can:
        * Kill OR Add a Score Amount Per Threshold (>,>=,<,<=,==)
        * Add a Score Amount Per Value
- Ability to Use Put.IO to Get, Download, and Move Torrents?
    + Push Torrent to Put.IO
    + Wait for Torrent Completion
    + Find Largest File in Torrent
    + Download Largest File
    + Wait for Download Completion
    + Rename File, Move to Collection, add IMDB Nfo File
- Ability to Search NZBs? (Think Sickrage/Couchpotato)
- Ability to Get Total Number of Episodes / Specials, Compare Against Collection (Think Sickrage)