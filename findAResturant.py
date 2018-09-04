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
	#Get the first resturant
	firstResturant = result['response']['venues'][0]
	firstResturant_id = firstResturant['id']
	
	
	#4. Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
	#5. Grab the first image
	#6. If no image is available, insert default a image url
	#7. Return a dictionary containing the restaurant name, address, and image url	
if __name__ == '__main__':
	findARestaurant("Pizza", "Tokyo, Japan")
	#findARestaurant("Tacos", "Jakarta, Indonesia")
	#findARestaurant("Tapas", "Maputo, Mozambique")
	#findARestaurant("Falafel", "Cairo, Egypt")
	#findARestaurant("Spaghetti", "New Delhi, India")
	#findARestaurant("Cappuccino", "Geneva, Switzerland")
	#findARestaurant("Sushi", "Los Angeles, California")
	#findARestaurant("Steak", "La Paz, Bolivia")
	#findARestaurant("Gyros", "Sydney Australia")