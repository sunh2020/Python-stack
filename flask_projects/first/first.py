# ---------------------------------
# Top Config
from flask import Flask, render_template # importing Flask
app = Flask(__name__) # creating a new instance of a server
# Flask got to be name
# ---------------------------------

@app.route("/") # listening for request on "localhost:5000"
def index():
    # Go retrieve some data from my DB
    name = "Sun"
    age = 37
    address = "123 some street"
    return render_template("index.html",
    templateName=name, templateAge=age, templateAddress=address, times=5
    )

@app.route("/hello") # listening for request on "localhost:5000/hello"
def hello():
    return render_template("hello.html")


@app.route("/m/<stack_id>/<module_id>/<page_id>")
def page(stack_id,module_id,page_id):
    print(stack_id) # this will print on html
    print(module_id)
    print(page_id)
    return f"{stack_id} {module_id} {page_id}"



# -----------------------------------------
# Bottom Config
if __name__ == "__main__": 
    # to check if name file is the main file that excuted
    # name will be main
    app.run(debug=True) # starting the Flask server with debug mode on
# -------------------------------