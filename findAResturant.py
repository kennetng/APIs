from geoLocation import getGeocodeLocation
from myAPI import getFourSquareAPI
import json
import httplib2

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

foursquare_client_id, foursquare_client_secret = getFourSquareAPI()
#foursquare_client_secret = getFourSquareAPI_CLIENT()


def findARestaurant(mealType,location):
	#Getting latitude and longitude cordination from a location
	latitude, longitude = getGeocodeLocation(location)
	#Using foursquare API to find nearby resturant with given latitude, longitude and type of meal
	url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20130815&ll=%s,%s&query=%s'% (foursquare_client_id, foursquare_client_secret, latitude, longitude, mealType))
	h = httplib2.Http()
	result = json.loads(h.request(url,'GET')[1])

	#Find the first resturant
	firstResturant = result['response']['venues'][0]
	
	#Get the venue id of the resutrant so we can retrieve the photo of it
	venue_id = firstResturant['id']
	url = ('https://api.foursquare.com/v2/venues/%s/photos?client_id=%s&v=20150603&client_secret=%s' % (venue_id, foursquare_client_id, foursquare_client_secret))
	picture = json.loads(h.request(url,'GET')[1])
	
	url_picture = ''
	if picture['response']['photos']['count'] != 0:
		#Retrieve the first picture of the resturant
		url_picture = picture['response']['photos']['items'][0]
		url_picture = url_picture['prefix'] + "300x300" + url_picture['suffix']
	else:
		#If there is no picture, use a default picture.
		url_picture = 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Tom%27s_Restaurant%2C_NYC.jpg/1200px-Tom%27s_Restaurant%2C_NYC.jpg'
	
	return 
	#7. Return a dictionary containing the restaurant name, address, and image url	
if __name__ == '__main__':
	#findARestaurant("Pizza", "Tokyo, Japan")
	#findARestaurant("Tacos", "Jakarta, Indonesia")
	#findARestaurant("Tapas", "Maputo, Mozambique")
	#findARestaurant("Falafel", "Cairo, Egypt")
	#findARestaurant("Spaghetti", "New Delhi, India")
	#findARestaurant("Cappuccino", "Geneva, Switzerland")
	findARestaurant("Sushi", "Los Angeles, California")
	#findARestaurant("Steak", "La Paz, Bolivia")
	#findARestaurant("Gyros", "Sydney Australia")