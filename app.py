from flask import Flask,render_template
from sparkpost import SparkPost

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

@app.route('/email')
def send_email():
	sparky = SparkPost('b5db5f3dbabccc1a978befe88ca226807b695e24')
 
	response = sparky.transmissions.send(
	    use_sandbox=True,
	    recipients=['developers+python@sparkpost.com'],
	    html='<html><body><p>Testing SparkPost - the world\'s most awesomest email service!</p></body></html>',
	    from_email='testing@sparkpostbox.com',
	    subject='Oh hey!')

	return render_template('about.html')

if __name__ == "__main__":
	app.run()
