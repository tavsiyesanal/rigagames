from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")

@app.route('/privacy')
def privacyPolicy():  # put application's code here
    return render_template("privacyPolicy.html")

@app.route('/app-ads.txt')
def appAds():
    return render_template("app-ads.txt")

if __name__ == '__main__':
    app.run()