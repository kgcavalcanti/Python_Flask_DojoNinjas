from flask import Flask, render_template, redirect, request
app = Flask(__name__)
@app.route('/')
def index():
	return render_template ('index.html')

@app.route('/ninja')
def ninja():
	return render_template ('ninjas.html')

@app.route('/ninja/blue')
def blue():
	return render_template ('ninjas_blue.html', turtle = 'Leonardo')

@app.route('/ninja/orange')
def orange():
	return render_template ('ninjas_orange.html', turtle = 'Michelangelo')

@app.route('/ninja/red')
def red():
	return render_template ('ninjas_red.html', turtle = 'Raphael')

@app.route('/ninja/purple')
def purple():
	return render_template ('ninjas_purple.html', turtle = 'Donatello' )

@app.route('/ninja/<something>')
def something(something):
	return render_template ('something.html', something = something)

app.run(debug=True)