from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    email_list = [
            "Richie.Foley@DCComic.com",
            "Beast.Boy@TeenTitans.com",
            "RobinIsCool@SladeisAlive.com"
            ]
    return render_template('staticshock.html',email_list=email_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2224)

