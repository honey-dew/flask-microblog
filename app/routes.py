from flask import render_template, request, redirect, url_for, flash
from app import app
from app.forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login success for user {}, remember_me is {}'.format(
			form.username.data, form.remember_me.data))
		return redirect('/')

	return render_template('login.html', title='login', form=form)