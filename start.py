from flask import *
app = Flask(__name__)

appname = 'ReportIt'

workin = '''<!DOCTYPE html>
<html>
  <head>
    <style type="text/css">
      html, body, #map-canvas { height: 100%; margin: 0; padding: 0;}
    </style>
    <script type="text/javascript"
      src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAgXKvcA_wB6l60kWyuyNWeYTP2zrVr6oo">
    </script>
    <script type="text/javascript">
      function initialize() {
        var mapOptions = {
          center: { lat: 31.9333, lng: 35.9333},
          zoom: 8,
          disableDefaultUI: true
        };
        var map = new google.maps.Map(document.getElementById('map-canvas'),
            mapOptions);
      }
      google.maps.event.addDomListener(window, 'load', initialize);
    </script>
  </head>
  <body>
<div id="map-canvas"></div>
  </body>
</html>'''

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
	return workin


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

if __name__ == '__main__':
	app.debug = True
	# app.logger.warning('A warning occurred (%d apples)', 42)
	app.run()