# Level 1
# When a user visits http://localhost:5000/play, 
# have it render three beautiful looking blue boxes. 
# Please use a template to render this.

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def repeatSame():
    return render_template("index.html")

@app.route('/play/<int:x>')
def repeatSame2(x):
    return render_template("index.html", y = x, c = "blue")
    # c = "blue" is set blue color on this specified


@app.route('/play/<int:x>/<color>')
def repeatSame3(x, color):
    return render_template("index.html", y = x, c = color)


if __name__ == "__main__": 
    app.run(debug=True)




# @app.route("/play/<x>")
# def repeatSame(box, x):
    # color = int()
#     return render_template("index.html", int(num), tempColor=color )


# @app.route("/play/<x>/<color>")
# def repeatSame(box, x, color):
#     return render_template("index.html", x, )



