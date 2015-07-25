SELECT * FROM (
	SELECT * FROM (SELECT *,(IFNULL(imdb_rating,1)*IFNULL(rt_score,1)*IFNULL(mc_score,1)*IFNULL(mc_rating,1)*IFNULL(101-mc_rank,1)*IFNULL(101-imdb_rank,1)*IFNULL(101-rt_rank,1)) AS score, IFNULL(imdb_year,imdb_year) AS year FROM movies WHERE year = 1989 AND score IS NOT NULL ORDER BY score DESC LIMIT 25)
 UNION 
	SELECT * FROM (SELECT *,(IFNULL(imdb_rating,1)*IFNULL(rt_score,1)*IFNULL(mc_score,1)*IFNULL(mc_rating,1)*IFNULL(101-mc_rank,1)*IFNULL(101-imdb_rank,1)*IFNULL(101-rt_rank,1)) AS score, IFNULL(imdb_year,imdb_year) AS year FROM movies WHERE year = 1990 AND score IS NOT NULL ORDER BY score DESC LIMIT 25)
 UNION 
	SELECT * FROM (SELECT *,(IFNULL(imdb_rating,1)*IFNULL(rt_score,1)*IFNULL(mc_score,1)*IFNULL(mc_rating,1)*IFNULL(101-mc_rank,1)*IFNULL(101-imdb_rank,1)*IFNULL(101-rt_rank,1)) AS score, IFNULL(imdb_year,imdb_year) AS year FROM movies WHERE year = 1991 AND score IS NOT NULL ORDER BY score DESC LIMIT 25)
 UNION 
	SELECT * FROM (SELECT *,(IFNULL(imdb_rating,1)*IFNULL(rt_score,1)*IFNULL(mc_score,1)*IFNULL(mc_rating,1)*IFNULL(101-mc_rank,1)*IFNULL(101-imdb_rank,1)*IFNULL(101-rt_rank,1)) AS score, IFNULL(imdb_year,imdb_year) AS year FROM movies WHERE year = 1992 AND score IS NOT NULL ORDER BY score DESC LIMIT 25)
 UNION 
	SELECT * FROM (SELECT *,(IFNULL(imdb_rating,1)*IFNULL(rt_score,1)*IFNULL(mc_score,1)*IFNULL(mc_rating,1)*IFNULL(101-mc_rank,1)*IFNULL(101-imdb_rank,1)*IFNULL(101-rt_rank,1)) AS score, IFNULL(imdb_year,imdb_year) AS year FROM movies WHERE year = 1993 AND score IS NOT NULL ORDER BY score DESC LIMIT 25)
 UNION 
	SELECT * FROM (SELECT *,(IFNULL(imdb_rating,1)*IFNULL(rt_score,1)*IFNULL(mc_score,1)*IFNULL(mc_rating,1)*IFNULL(101-mc_rank,1)*IFNULL(101-imdb_rank,1)*IFNULL(101-rt_rank,1)) AS score, IFNULL(imdb_year,imdb_year) AS year FROM movies WHERE year = 1994 AND score IS NOT NULL ORDER BY score DESC LIMIT 25)
 UNION 
	SELECT * FROM (SELECT *,(IFNULL(imdb_rating,1)*IFNULL(rt_score,1)*IFNULL(mc_score,1)*IFNULL(mc_rating,1)*IFNULL(101-mc_rank,1)*IFNULL(101-imdb_rank,1)*IFNULL(101-rt_rank,1)) AS score, IFNULL(imdb_year,imdb_year) AS year FROM movies WHERE year = 1995 AND score IS NOT NULL ORDER BY score DESC LIMIT 25)
 UNION 
	SELECT * FROM (SELECT *,(IFNULL(imdb_rating,1)*IFNULL(rt_score,1)*IFNULL(mc_score,1)*IFNULL(mc_rating,1)*IFNULL(101-mc_rank,1)*IFNULL(101-imdb_rank,1)*IFNULL(101-rt_rank,1)) AS score, IFNULL(imdb_year,imdb_year) AS year FROM movies WHERE year = 1996 AND score IS NOT NULL ORDER BY score DESC LIMIT 25)
 UNION 
	SELECT * FROM (SELECT *,(IFNULL(imdb_rating,1)*IFNULL(rt_score,1)*IFNULL(mc_score,1)*IFNULL(mc_rating,1)*IFNULL(101-mc_rank,1)*IFNULL(101-imdb_rank,1)*IFNULL(101-rt_rank,1)) AS score, IFNULL(imdb_year,imdb_year) AS year FROM movies WHERE year = 1997 AND score IS NOT NULL ORDER BY score DESC LIMIT 25)
 UNION 
	SELECT * FROM (SELECT *,(IFNULL(imdb_rating,1)*IFNULL(rt_score,1)*IFNULL(mc_score,1)*IFNULL(mc_rating,1)*IFNULL(101-mc_rank,1)*IFNULL(101-imdb_rank,1)*IFNULL(101-rt_rank,1)) AS score, IFNULL(imdb_year,imdb_year) AS year FROM movies WHERE year = 1998 AND score IS NOT NULL ORDER BY score DESC LIMIT 25)
 UNION 
	SELECT * FROM (SELECT *,(IFNULL(imdb_rating,1)*IFNULL(rt_score,1)*IFNULL(mc_score,1)*IFNULL(mc_rating,1)*IFNULL(101-mc_rank,1)*IFNULL(101-imdb_rank,1)*IFNULL(101-rt_rank,1)) AS score, IFNULL(imdb_year,imdb_year) AS year FROM movies WHERE year = 1999 AND score IS NOT NULL ORDER BY score DESC LIMIT 25)
 UNION 
	SELECT * FROM (SELECT *,(IFNULL(imdb_rating,1)*IFNULL(rt_score,1)*IFNULL(mc_score,1)*IFNULL(mc_rating,1)*IFNULL(101-mc_rank,1)*IFNULL(101-imdb_rank,1)*IFNULL(101-rt_rank,1)) AS score, IFNULL(imdb_year,imdb_year) AS year FROM movies WHERE year = 2000 AND score IS NOT NULL ORDER BY score DESC LIMIT 25)
 UNION 
	SELECT * FROM (SELECT *,(IFNULL(imdb_rating,1)*IFNULL(rt_score,1)*IFNULL(mc_score,1)*IFNULL(mc_rating,1)*IFNULL(101-mc_rank,1)*IFNULL(101-imdb_rank,1)*IFNULL(101-rt_rank,1)) AS score, IFNULL(imdb_year,imdb_year) AS year FROM movies WHERE year = 2001 AND score IS NOT NULL ORDER BY score DESC LIMIT 25)
 UNION 
	SELECT * FROM (SELECT *,(IFNULL(imdb_rating,1)*IFNULL(rt_score,1)*IFNULL(mc_score,1)*IFNULL(mc_rating,1)*IFNULL(101-mc_rank,1)*IFNULL(101-imdb_rank,1)*IFNULL(101-rt_rank,1)) AS score, IFNULL(imdb_year,imdb_year) AS year FROM movies WHERE year = 2002 AND score IS NOT NULL ORDER BY score DESC LIMIT 25)
 UNION 
	SELECT * FROM (SELECT *,(IFNULL(imdb_rating,1)*IFNULL(rt_score,1)*IFNULL(mc_score,1)*IFNULL(mc_rating,1)*IFNULL(101-mc_rank,1)*IFNULL(101-imdb_rank,1)*IFNULL(101-rt_rank,1)) AS score, IFNULL(imdb_year,imdb_year) AS year FROM movies WHERE year = 2003 AND score IS NOT NULL ORDER BY score DESC LIMIT 25)
 UNION 
	SELECT * FROM (SELECT *,(IFNULL(imdb_rating,1)*IFNULL(rt_score,1)*IFNULL(mc_score,1)*IFNULL(mc_rating,1)*IFNULL(101-mc_rank,1)*IFNULL(101-imdb_rank,1)*IFNULL(101-rt_rank,1)) AS score, IFNULL(imdb_year,imdb_year) AS year FROM movies WHERE year = 2004 AND score IS NOT NULL ORDER BY score DESC LIMIT 25)
 UNION 
	SELECT * FROM (SELECT *,(IFNULL(imdb_rating,1)*IFNULL(rt_score,1)*IFNULL(mc_score,1)*IFNULL(mc_rating,1)*IFNULL(101-mc_rank,1)*IFNULL(101-imdb_rank,1)*IFNULL(101-rt_rank,1)) AS score, IFNULL(imdb_year,imdb_year) AS year FROM movies WHERE year = 2005 AND score IS NOT NULL ORDER BY score DESC LIMIT 25)
 UNION
	SELECT * FROM (SELECT *,(IFNULL(imdb_rating,1)*IFNULL(rt_score,1)*IFNULL(mc_score,1)*IFNULL(mc_rating,1)*IFNULL(101-mc_rank,1)*IFNULL(101-imdb_rank,1)*IFNULL(101-rt_rank,1)) AS score, IFNULL(imdb_year,imdb_year) AS year FROM movies WHERE year = 2006 AND score IS NOT NULL ORDER BY score DESC LIMIT 25)
 UNION 
	SELECT * FROM (SELECT *,(IFNULL(imdb_rating,1)*IFNULL(rt_score,1)*IFNULL(mc_score,1)*IFNULL(mc_rating,1)*IFNULL(101-mc_rank,1)*IFNULL(101-imdb_rank,1)*IFNULL(101-rt_rank,1)) AS score, IFNULL(imdb_year,imdb_year) AS year FROM movies WHERE year = 2007 AND score IS NOT NULL ORDER BY score DESC LIMIT 25)
 UNION 
	SELECT * FROM (SELECT *,(IFNULL(imdb_rating,1)*IFNULL(rt_score,1)*IFNULL(mc_score,1)*IFNULL(mc_rating,1)*IFNULL(101-mc_rank,1)*IFNULL(101-imdb_rank,1)*IFNULL(101-rt_rank,1)) AS score, IFNULL(imdb_year,imdb_year) AS year FROM movies WHERE year = 2008 AND score IS NOT NULL ORDER BY score DESC LIMIT 25)
 UNION 
	SELECT * FROM (SELECT *,(IFNULL(imdb_rating,1)*IFNULL(rt_score,1)*IFNULL(mc_score,1)*IFNULL(mc_rating,1)*IFNULL(101-mc_rank,1)*IFNULL(101-imdb_rank,1)*IFNULL(101-rt_rank,1)) AS score, IFNULL(imdb_year,imdb_year) AS year FROM movies WHERE year = 2009 AND score IS NOT NULL ORDER BY score DESC LIMIT 25)
 UNION 
	SELECT * FROM (SELECT *,(IFNULL(imdb_rating,1)*IFNULL(rt_score,1)*IFNULL(mc_score,1)*IFNULL(mc_rating,1)*IFNULL(101-mc_rank,1)*IFNULL(101-imdb_rank,1)*IFNULL(101-rt_rank,1)) AS score, IFNULL(imdb_year,imdb_year) AS year FROM movies WHERE year = 2010 AND score IS NOT NULL ORDER BY score DESC LIMIT 25)
 UNION 
	SELECT * FROM (SELECT *,(IFNULL(imdb_rating,1)*IFNULL(rt_score,1)*IFNULL(mc_score,1)*IFNULL(mc_rating,1)*IFNULL(101-mc_rank,1)*IFNULL(101-imdb_rank,1)*IFNULL(101-rt_rank,1)) AS score, IFNULL(imdb_year,imdb_year) AS year FROM movies WHERE year = 2011 AND score IS NOT NULL ORDER BY score DESC LIMIT 25)
 UNION 
	SELECT * FROM (SELECT *,(IFNULL(imdb_rating,1)*IFNULL(rt_score,1)*IFNULL(mc_score,1)*IFNULL(mc_rating,1)*IFNULL(101-mc_rank,1)*IFNULL(101-imdb_rank,1)*IFNULL(101-rt_rank,1)) AS score, IFNULL(imdb_year,imdb_year) AS year FROM movies WHERE year = 2012 AND score IS NOT NULL ORDER BY score DESC LIMIT 25)
 UNION 
	SELECT * FROM (SELECT *,(IFNULL(imdb_rating,1)*IFNULL(rt_score,1)*IFNULL(mc_score,1)*IFNULL(mc_rating,1)*IFNULL(101-mc_rank,1)*IFNULL(101-imdb_rank,1)*IFNULL(101-rt_rank,1)) AS score, IFNULL(imdb_year,imdb_year) AS year FROM movies WHERE year = 2013 AND score IS NOT NULL ORDER BY score DESC LIMIT 25)
 UNION 
	SELECT * FROM (SELECT *,(IFNULL(imdb_rating,1)*IFNULL(rt_score,1)*IFNULL(mc_score,1)*IFNULL(mc_rating,1)*IFNULL(101-mc_rank,1)*IFNULL(101-imdb_rank,1)*IFNULL(101-rt_rank,1)) AS score, IFNULL(imdb_year,imdb_year) AS year FROM movies WHERE year = 2014 AND score IS NOT NULL ORDER BY score DESC LIMIT 25)
 UNION 
	SELECT * FROM (SELECT *,(IFNULL(imdb_rating,1)*IFNULL(rt_score,1)*IFNULL(mc_score,1)*IFNULL(mc_rating,1)*IFNULL(101-mc_rank,1)*IFNULL(101-imdb_rank,1)*IFNULL(101-rt_rank,1)) AS score, IFNULL(imdb_year,imdb_year) AS year FROM movies WHERE year = 2015 AND score IS NOT NULL ORDER BY score DESC LIMIT 25)
) ORDER BY score DESC;