from flask import Flask, render_template  #NEW IMPORT!!

app = Flask(__name__)    #This is creating a new Flask object

#decorator that links...

@app.route('/')          						#This is the main URL
def index():
    return render_template("index.html", name="index")		#The argument should be in templates folder

@app.route('/index')          						#This is the main URL
def anotherindex():
    return render_template("index.html", name="index")
@app.route('/interests')
def interests():
    return render_template("interests.html", name="interests")

@app.route('/courses')          							#This is the main URL
def courses():
    return render_template("courses.html", name="courses")

@app.route('/other')          							#This is the main URL
def other():
    return render_template("other.html", name="other")

#Add the code for courses

#Add the code for other

#Hmmm, do we need another one?


if __name__ == '__main__':
    app.run(debug=True)		#debug=True is optional
