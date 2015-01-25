import sqlite3 as lite
import sys
from flask import *
from contextlib import closing
app = Flask(__name__, template_folder='templates')

appname = 'ReportIt'
DATABASE = 'db/c.db'

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

def test_db():
	con = None

	try: 
		con = lite.connect(DATABASE)

		cur = con.cursor()
		cur.execute('SELECT SQLITE_VERSION()')

		data = cur.fetchone()

		print "SQLite version: %s" % data 

	except lite.Error, e:
		
		print "Error %s:" % e.args[0]
		sys.exit(1)

	finally:
		if con:
			con.close()


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


def connect_db():
    return lite.connect(app.config['DATABASE'])


def make_dicts(cursor, row):
    return dict((cur.description[idx][0], value)
                for idx, value in enumerate(row))

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


# for user in query_db('select * from users'):
#     print user['username'], 'has the id', user['user_id']




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
		notify = False
		# city = request.form['city']
		# country = request.form['country']
		# pic_url = request.form['pic_url']
		city = "lululand"
		country = ""
		pic_url = ""


		con = lite.connect(DATABASE)

		with con:

			cur = con.cursor()

			cur.execute('''INSERT INTO complaints(lat,lon,email,cat1,cat2,description,notify,city,country,pic_url)
                  VALUES(?,?,?,?,?,?,?,?,?,?)''', (lat,lon,email,cat1,cat2,description,notify,city,country,pic_url))


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


@app.route('/test')
def index():

	return render_template('index.html')




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