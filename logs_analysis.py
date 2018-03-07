#!/usr/bin/env python

import psycopg2


"""Query variables"""
articles_query = """
select articles.title, count(*) as views
from articles join log on log.path
like '%' || articles.slug || '%'
group by articles.title
order by views desc limit 3;
"""

authors_query = """
select authors.name, views
from authors,
(select articles.author, count(*) as views
from articles join log on log.path
like '%' || articles.slug || '%'
group by articles.author) as sub
where authors.id = sub.author
order by views desc;
"""

errordays_query = """
select error.date, 100 * cast(numerror as float) / (numok + numerror) as rate
from (select date(time) as date, count(*) as numerror
from log where status like '404%' group by date) as error,
(select date(time) as date, count(*) as numok
from log where status like '200%' group by date) as ok
where error.date = ok.date
order by rate desc;
"""


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=news")


def topArticles():
    """Prints the most popular three articles of all time"""
    conn = connect()
    c = conn.cursor()
    c.execute(articles_query)
    result = c.fetchall()
    print "***The most popular three articles of all time***"
    for i in result:
        print "\"" + i[0] + "\" -- " + str(i[1]) + " views"


def topAuthors():
    """Prints the most popular article authors of all time"""
    conn = connect()
    c = conn.cursor()
    c.execute(authors_query)
    result = c.fetchall()
    print "\n***The most popular article authors of all time***"
    for i in result:
        print i[0] + " -- " + str(i[1]) + " views"


def errorDays():
    """Prints days with more than 1% of requests lead to errors"""
    conn = connect()
    c = conn.cursor()
    c.execute(errordays_query)
    result = c.fetchall()
    print "\n***Days with more than 1% of requests lead to errors***"
    for i in result:
        if i[1] > 1:
            print i[0].strftime('%b %d, %Y') + " -- " + \
                str(round(i[1], 2)) + "% errors\n"


if __name__ == '__main__':
    topArticles()
    topAuthors()
    errorDays()
