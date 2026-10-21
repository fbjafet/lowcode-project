from flask import Flask

app = Flask(__name__)

@app.route("/C:/Users/fabia/Documents/lowcode-project")
def lowcode_project():
    return "<h1>Hello from Fabiana Jafet</h1>"

if __name__ == "__main__":
    app.run(debug=True)