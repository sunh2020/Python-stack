from flask import Flask, render_template
app = Flask(__name__)

# # http://localhost:5000 - should display 8 by 8 checkerboard

# @app.route('/')
# def index():
#     return render_template("index.html")


# # # http://localhost:5000/4 - should display 8 by 4 checkerboard


# # http://localhost:5000/(x)/(y) - should display x by y checkerboard.  
# # For example, http://localhost:5000/10/10 should display 10 by 10 checkerboard.  
# Before you pass x or y to Jinja, please remember to convert it to integer first 
# (so that you can use x or y in a for loop)
@app.route('/<int:x>/<int:y>')
def index(x = 8, y = 8):
    return render_template("index.html", x = x, y = y)



if __name__ == "__main__": 
    app.run(debug=True)