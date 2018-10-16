from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/page1")
def render_page1():
	return render_template('page1.html')
	
	@app.route("/page11")
def render_page11():
	meters = float(request.args['meters'])
	feet = meters * 3.28084 
	return render_template('page11.html', response = meters)
	
@app.route("/page2")
def render_page2():
    return render_template('page2.html')

@app.route("/page3")
def render_page3():
    return render_template('page3.html')

@app.route("/page4")
def render_page4():
    return render_template('page4.html')
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
