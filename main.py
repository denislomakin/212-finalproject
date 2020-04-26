from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def open_file():
	return render_template("web-speech-demo.html")

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8082, ssl_context='adhoc')
