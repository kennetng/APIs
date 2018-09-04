from myAPI import getGoogleAPI
import httplib2
import json

def getGeocodeLocation(inputStr):
    google_api_key = getGoogleAPI()
    locationString = inputStr.replace(' ' , '+')
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'% (locationString, google_api_key))
    h = httplib2.Http()
    result = json.loads(h.request(url,'GET')[1])
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']
    return (latitude,longitude)