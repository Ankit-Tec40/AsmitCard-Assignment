from flask import Flask, redirect, render_template, request
from datetime import datetime
import sqlite3
import os
app=Flask(__name__)


@app.route("/",methods=['POST','GET'])
def index():
    return render_template("index.html")

@app.route("/addData",methods=['POST','GET'])
def addData():
    if request.method=="GET":
        return render_template("AddData.html")
    else:
        name=request.form.get("name")
        email=request.form.get("email")
        mobNo=request.form.get("mobno")
        coursLevel=request.form.get("courses")
        country=request.form.get("countries")
        dataOfBirth=request.form.get("birthday")
        connection=sqlite3.connect("users.sqlite")
        cursor=connection.cursor()
        insertQuery="""insert into users(Name,Email,ContactNumber,CourseLevel,CountryPreferences,DateOfBirth) values (?,?,?,?,?,?)"""
        
        cursor.execute(insertQuery,(name,email,mobNo,coursLevel,country,dataOfBirth))
        connection.commit()
        return("Data Added")

@app.route("/showData",methods=['POST','GET'])
def showData():
    if request.method=="GET":
        return render_template("ShowData.html")
    else:
        email=request.form.get("email")
        connection=sqlite3.connect("users.sqlite")
        cursor=connection.cursor()
        query=f"""select * from users where email='{email}'"""
        data=cursor.execute(query)
        usersData=cursor.fetchall()
        print(usersData)

        return render_template("ShowData.html",usersData=usersData)






if __name__=="__main__":
    app.run(debug=True)