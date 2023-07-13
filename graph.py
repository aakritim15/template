from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    data = [
        
        ("01-01-2020",1597),
        ("02-01-2020",1519),
        ("03-01-2020",4845),
        ("04-01-2020",1854),
        ("05-01-2020",8789),
        ("06-01-2020",6220),
        ("07-01-2020",1000),
        ("08-01-2020",1597),
        ]
    labels = [row[0] for row in data]
    values = [row[1] for row in data]


    return render_template("graph.html", labels=labels, values=values)


if __name__ == "__main__":
    app.run(debug="True")
