import sqlite3
import MySQLdb
import codecs
from urllib import quote

config = {
  "dbfile": "top_movies.db",
  "years": range(2015-25,2015),
  "do_imdb": True,
  "do_rt": True,
  "do_mc": True,
  "mysql_addr": "192.168.1.122",
  "mysql_port": 3306,
  "mysql_user": "xbmc",
  "mysql_pass": "xbmc",
  "mysql_db": "MyVideos90",
  "mysql_table": "movie",
  "mysql_imdb_id_colname": "c09",
  "mysql_path_colname": "c22"
}

with open('top_25_by_year.sql','r') as f:
	top_25_query = f.read()

sqliteconn = sqlite3.connect(config['dbfile'])
mysqlconn = MySQLdb.connect(
	host=config['mysql_addr'],
	user=config['mysql_user'],
	passwd=config['mysql_pass'],
	db=config['mysql_db'])

c = sqliteconn.cursor()
d = mysqlconn.cursor()

c.execute(top_25_query)
results = c.fetchall()

audits = []

i = 1
for row in results:
	obj = {}
	obj['rank'] = i
	obj['normalize'] = row[1]
	obj['imdb_id'] = row[2]
	obj['imdb_name'] = row[4]
	obj['imdb_year'] = row[5]
	obj['imdb_outline'] = row[6]
	obj['imdb_genres'] = row[7]
	obj['total_score'] = row[-2]
	obj['have'] = False

	# check if in Kodi database
	d.execute('SELECT c22 FROM '+config['mysql_table']+' WHERE '+config['mysql_imdb_id_colname']+'=%s',(obj['imdb_id'],))
	a = d.fetchone()
	# print "vvvvvvvvvvvvvvvvvvvvvvvvvvvvv"
	# print a
	# print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
	if a:
		obj['have'] = True
		obj['path'] = a[0]

	audits.append(obj)
	i = i+1

headers = ['rank','imdb_name','imdb_year','imdb_outline','imdb_genres','total_score','have']

with codecs.open('audit.html',mode='w',encoding='utf-8') as f:
	f.write("""
		<style>
		table {border-collapse:collapse;}
		tr.donthave {background-color: lightpink;}
		</style>
		""")
	f.write('<table border=1>')
	f.write('<tr>')
	for header in headers:
		f.write('<td>%s</td>' % header)
	f.write('</tr>')
	for audit in audits:
		if audit['have']:
			f.write('<tr class="have">')
		else:
			f.write('<tr class="donthave">')
		for header in headers:
                        if header == "imdb_name":
                                f.write('<td><a href="http://www.imdb.com/title/%s/">%s</a></td>' % (audit['imdb_id'],audit[header]))
                        elif header == "have" and audit['have'] is False:
                                f.write('<td><a href="https://thepiratebay.mn/search/%s/0/99/200">TPB</a><br /><a href="https://kat.cr/usearch/%s%%20category:movies/">KAT</a></td>' % (quote(audit['normalize']),quote(audit['normalize'])))
                        else:
                                f.write('<td>%s</td>' % audit[header])
		f.write('</tr>')
	f.write('</table>')
	f.write('<pre>')
	for audit in [x for x in audits if x.get('path')]:
		try:
			#rsync -azP Wolf\ of\ Wall\ Street,\ The\ \(2013\) 'osmc@192.168.1.67:/media/momdadmedia/Media/Movies'
			name = audit['path'].split('/')[-2]
			name = name.replace(' ','\\ ')
			name = name.replace('(','\\(')
			name = name.replace(')','\\)')
			name = name.replace('&','\\&')
			name = name.replace("'","\\'")
			name = name.replace('"','\\"')
			f.write("rsync -azP %s 'osmc@192.168.1.75:/media/momdadmedia/Media/Movies'" % name)
			f.write('\n')
			# f.write('%s\n' % audit['path'])
		except:
			pass
	f.write('</pre>')
