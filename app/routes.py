from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username':'Gugun'}

	posts = [
		{
			'author':{'username':'Gugun'},
			'body':'This is Gugun\'s post'		
		},
		{
			'author':{'username':'Ade'},
			'body':'This is Ade\'s post'		
		}
	]
	return render_template('index.html', title='Home', user=user, posts=posts)