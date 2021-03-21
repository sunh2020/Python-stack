# 1. localhost:5000/ - have it say "Hello World!"
# from flask import Flask
# app = Flask(__name__) 
# @app.route("/")
# def success():
#     return "Hello World"



# 2. localhost:5000/dojo - have it say "Dojo!"
# from flask import Flask
# app = Flask(__name__) 
# @app.route("/dojo")
# def success():
#     return "Dojo!"



# 3. Create one url pattern and function that can handle the following examples:
# localhost:5000/say/flask - have it say "Hi Flask!"
# localhost:5000/say/michael - have it say "Hi Michael!"
# localhost:5000/say/john - have it say "Hi John!"

# from flask import Flask
# app = Flask(__name__)
# @app.route("/greet/<name>")
# def sayHi(name="you"): 
#     return f"Hello, {name}"




# 4. Create one url pattern and function that can handle the following examples 
# (HINT: int() will come in handy! For example int("35") returns 35):
# localhost:5000/repeat/35/hello - have it say "hello" 35 times
# localhost:5000/repeat/80/bye - have it say "bye" 80 times
# localhost:5000/repeat/99/dogs - have it say "dogs" 99 times
from flask import Flask
app = Flask(__name__)
@app.route("/repeat/<int:times>/<word>")
def repeatSame(times, word):
    return word * times



if __name__ == "__main__": 
#     # to check if name file is the main file that excuted
#     # name will be main
    app.run(debug=True)
