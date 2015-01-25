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


######### SQLITE

DATABASE = '/c.db'

def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = connect_to_database()
	return db

@app.teardown_appcontext
def close_connection(exception):
	db = getattr(g, '_database', None)
	if db is not None:
		db.close()



########## FLASK RESPONDS TO PAGES

@app.route('/submit', methods = ['GET', 'POST'])
def submit():
	if request.method == 'POST':

		print request.form

		email = request.form['email']
		lat = request.form['lat']
		lon = request.form['lon']
		cat1 = request.form['cat1']
		cat2 = request.form['cat2']
		description = request.form['description']
		# notify = request.form['notify']





		return render_template('form_action.html', 
					mail = email,
					lat = lat,
					lon = lon,
					cat1 = cat1,
					cat2 = cat2,
					description = description
					)

	else:
		return render_template('form_submit.html')

@app.route('/submit/<lat>/<lon>')
def submit_redirect(lat, lon):

	return render_template('form_submit.html',
			lat = lat,
			lon = lon)




@app.route('/country/<country>')
def print_country_region(country):
	return render_template('js-play.html', 
		country=country
		)
	# return render_template('hello.html', name = country)

@app.route('/city/<city>')
def print_city(city):
	return render_template('js-play.html', 
		city=city
		)

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