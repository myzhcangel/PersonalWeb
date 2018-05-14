from flask import Flask,render_template

conn = None
app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)