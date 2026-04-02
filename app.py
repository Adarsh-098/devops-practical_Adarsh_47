from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Adarsh Yadav roll no 47 se c cmpn c2"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)