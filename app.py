import flask from Flask
app = Flask(__name__)

@app.route("/")
def HomePage():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)