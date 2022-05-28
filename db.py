import sqlite3
conn=sqlite3.connect("users.sqlite")
cursor=conn.cursor()
query="""Create table users(
    Name text,
    Email text primary key,
    ContactNumber integer,
    CourseLevel text,
    CountryPreferences text,
    DateOfBirth datetime

)
"""
drop="drop table users"
cursor.execute(query)