from flask import Flask

## API REST - Representational State Transfer
##HTTP -> GET, POST, PUT, DELETE, PATCH

# __name__ = "__main__" -> Feito de Forma manual
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/about")
def about():
    return "Página Sobre"

if __name__ == "__main__":
    app.run(debug=True)