from flask import *
from werkzeug.utils import *
import main

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		try:
			f = request.files['file']
			f.save(secure_filename(f.filename))
			main.main(f.filename)
		except:
			print("no file chosen")
		p = request.form
		height = p["height"]
		width = p["width"]
		if len(p) < 3:
			print("no thickness selected")
		try:
			h = float(height)
		except:
			print("height is not a valid number")
		try:
			w = float(width)
		except:
			print("width is not a valid number")
		
	return redirect("/")

if __name__ == "__main__":
	app.run(debug=True)
