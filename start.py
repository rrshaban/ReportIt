from flask import *
app = Flask(__name__)

appname = 'ReportIt'

working = "<br />."

@app.route('/')
def home():
	return 'Welcome to %s!'+ working % appname


@app.route('/about')
def about():
	return 'The about page.'

@app.route('/login')
def login():
	return 'login'


@app.route('/country/<country>')
def print_country_region(country):
	return 'Country: %s' % country


@app.route('/p/<int:post_id>')
def show_post(post_id):
	####
	# 		Post Page
	####

	return 'Post %d' % post_id


# with app.test_request_context():
# 	print url_for('home')
# 	print url_for('login', next = '/')

if __name__ == '__main__':
	app.debug = True
	app.logger.warning('A warning occurred (%d apples)', 42)
	app.run()