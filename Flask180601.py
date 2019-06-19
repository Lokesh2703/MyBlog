from flask import Flask, render_template, request,url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app=Flask(__name__)

app.config['SECRET_KEY']= 'a6e828d40133feef0815ad54dd11b58f4a87e14afae6be8b77589a34b4fcb22f'

posts=[
	{
		'title':'Post 1',
		'author':'Lokesh',
		'date_posted':'June 19,2019',
		'content': 'This is my first blog'
	},
	{
		'title':'Post 2',
		'author':'Dinesh',
		'date_posted':'June 20,2019',
		'content': 'This is his first blog'
	}
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts,title="My Website-Home")

@app.route("/about")
def about():
    return render_template('about.html',title="My Website-About")

@app.route("/register" ,methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!','success')
		return redirect(url_for('home'))
	return render_template('register.html',title="My Website-register", form=form)

@app.route("/login",methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'lokesh27dinu@gmail.com' and form.password.data == 'password':
			flash('You have been logged in!','success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check Username and password','danger')
	return render_template('login.html',title="My Website-home", form=form)

if __name__== "__main__":
	app.run(debug=True)