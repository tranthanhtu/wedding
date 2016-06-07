from flask import Flask,render_template

app = Flask(__name__)


@app.route("/<path:path>")
def static_file(path):
    return app.send_static_file(path)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/forget.html')
def forget():
    return render_template("forget.html")

@app.route('/happyending')
def happyending():
    return render_template("index.html")

@app.route('/love')
def love():
    return render_template("love.html")



if __name__ == '__main__':
    app.run()
