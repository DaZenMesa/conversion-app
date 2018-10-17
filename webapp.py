from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/page1")
def render_page1():
	return render_template('page1.html')
	
@app.route("/page11")
def render_page11():
	if "meters1" in request.args:
		meters1 = float(request.args['meters1'])
		feet1 = meters1 * 3.28084
		return render_template('page11.html', response1 = feet1)
	if "feet2" in request.args:
		feet2 = float(request.args['feet2'])
		meters2 = feet2 / 3.28084  
		return render_template('page11.html', response2 = meters2)
	if "miles3" in request.args:
		miles3 = float(request.args['miles3'])
		feet3 = miles3 / 3.28084  
		return render_template('page11.html', response3 = miles3)
	return render_template('page11.html')
	
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
