from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World!'


@app.route('/country/<country>')
def print_country_region(country):
	return 'Country: %s' % country



@app.route('/p/<int:post_id>')
def show_post(post_id):
	####
	# 		Post Page
	####

	return 'Post %d' % post_id


if __name__ == '__main__':
	app.debug = True
	app.run()