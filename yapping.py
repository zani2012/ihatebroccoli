from flask import Flask, render_template, request
app = Flask(__name__)


#Controller/Handler
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/yapping", methods=["POST"])

def yapping():
    binary = ""
    numbers = []
    number = int(request.form.get("number"))
    binary = bin(number)
    print(binary)
    return render_template("binary.html", number=number, binary=binary)

if __name__ == "__main__":
    app.run()

