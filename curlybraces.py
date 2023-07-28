#!/usr/bin/python3

from flask import Flask
from flask import request, redirect, url_for # missing imports

app = Flask(__name__)

html= '''<style>
body {
  background-color: black;
  text-align: center;
  color: white;
  font-family: Comic Sans MS, Impact, sans-serif;
}
</style>
</head>
<body>

<h1>TRIVIA TIME</h1>
<p>What is the meaning of life, the universe, and everything?</p>
<img src="https://shokugekinosoma.fandom.com/wiki/Isami_Aldini?file=Isami+Aldini+%28anime%29.png" alt="Avatar" style="width:200px">

    <form action = "/login" method = "POST">
        <p><input type = "text" name = "nm"></p>
        <p><input type = "submit" value = "submit"></p>
    </form>

</body>
</html>'''

@app.route("/correct") # missing decorator
def success():
    return f"That is correct!"

@app.route("/") # missing decorator
def start():
    return html

@app.route("/login", methods= ["POST"]) # missing decorator, 
                                        #ALSO must specify that POST method allowed
def login():
        if request.form.get("nm"):
            answer = request.form.get("nm")
            if answer == "42":
                return redirect(url_for("success")) # missing ending )
            else:
                return redirect("/")  # missing "" around /
        else:
            return redirect("/")      # missing "" around /

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)  # specify host and port so we can see in aux1
