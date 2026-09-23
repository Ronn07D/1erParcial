from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>verificando el entorno virtual</h1><p>entorno activado</p>"

if __name__ == "__main__":
    app.run(debug=True)
