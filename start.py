import sqlite3 as lite
from flask import *
app = Flask(__name__, template_folder='templates')

appname = 'ReportIt'

@app.route('/')
def home():
	return 'Welcome to %s!' % appname



@app.route('/about')
def about():
	return 'The about page.'

@app.route('/login')
def login():
	return 'login'

@app.route('/working')
def working():
	return render_template('js-play.html')


@app.route('/submit', methods = ['GET', 'POST'])
def submit():
	if request.method == 'POST':

		title = request.form['title']
		city = request.form['city']
		category1 = request.form['category1']
		category2 = request.form['category2']
		description = request.form['description']

		return render_template('form_action.html', 
					title=title, 
					city=city,
					category1=category1,
					category2=category2,
					description=description)

	else:
		return render_template('form_submit.html')




@app.route('/country/<country>')
def print_country_region(country):
	return render_template('hello.html', name = country)


@app.route('/p/<int:post_id>')
def show_post(post_id):
	####
	# 		Post Page
	####

	return 'Post %d' % post_id


# with app.test_request_context():
# 	print url_for('home')
# 	print url_for('login', next = '/')
# 	print url_for('print_country_region', country = 'Jordan')
		# url_for('static', filename='style.css')
		#  this has to be in folder static

if __name__ == '__main__':
	app.debug = True
	# app.logger.warning('A warning occurred (%d apples)', 42)
	app.run()