from flask import Flask, render_template
app = Flask(__name__) 

@app.route("/play")
def index():
    color="blue"
    return render_template("index.html", num=3, tempColor=color)

@app.route("/play/<fun>")
def two(fun):
    # num = int(fun)
    return render_template("index.html", num=int(fun), tempColor="blue")

@app.route("/play/<>/<>")
def color():


if __name__ == "__main__":
    # to check if name file is the main file that excuted
    # name will be main
    app.run(debug=True)