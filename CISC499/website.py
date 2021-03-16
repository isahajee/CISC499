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
		
	return redirect("/output.html")

@app.route('/application.html')
def wrapping():
	return render_template("application.html")

@app.route("/about.html")
def about():
	return render_template("about.html")

@app.route("/contact.html")
def contact():
	return render_template("contact.html")

@app.route("/help.html")
def help():
	return render_template("help.html")

@app.route("/output.html")
def output():
	svg1 = open("anim1.svg").read()
	svg2 = open("anim2.svg").read()
	svg3 = open("anim3.svg").read()
	svg4 = open("anim4.svg").read()
	svgfinal = open("ex.svg").read()
	return render_template("output.html", svg1 = svg1, svg2 = svg2, svg3 = svg3, svg4 = svg4, svgfinal = svgfinal)

@app.route("/download.html", methods=['GET'])
def download():
	return send_file('ex.svg', as_attachment = True)

if __name__ == "__main__":
	app.run(debug=True)
