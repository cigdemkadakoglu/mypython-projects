from flask import Flask
app = Flask(__name__)

@app.route("/")
def function_hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("8000"), debug=True)