from flask import Flask, render_template, request
# from flask_frozen import Freezer

from color import calculate_related_colors

app = Flask(__name__)
# freezer = Freezer(app)


@app.route("/", methods=["GET"], endpoint="index")
def index():
    return render_template("index.html")


@app.route("/", methods=["POST"], endpoint="apple")
def color_converter():
    hex_color = request.form["hex_color"]
    h, s, v = calculate_related_colors(hex_color)
    print(h, s, v)
    return render_template("converter.html", h=h, s=s, v=v)


# @freezer.register_generator
# def index():
#     yield "index", {}
#
#
# @freezer.register_generator
# def color_converter():
#     yield "apple", {}


if __name__ == '__main__':
    # freezer.freeze()
    app.run(debug=True)
