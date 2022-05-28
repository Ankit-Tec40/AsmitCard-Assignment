import sqlite3
conn=sqlite3.connect("users.sqlite")
cursor=conn.cursor()
query="""Create table users(
    Name text,
    Email text,
    ContactNumber integer,
    CourseLevel text,
    CountryPreferences text,
    DateOfBirth datetime

)
"""
cursor.execute(query)