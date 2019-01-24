# Simulating student traffic on campus.  This type of data could be used
# for a variety of purposes like path improvement targeting, safety checkpoints, info booth placement
# and more.  Let's use Google Routes API to act as though
# foot traffic has actually happened on these paths.

import random
import json
import requests
import urllib
import os

from route_data import locs

def main():

    # Adding a bunch of campus locations for start and end points
    locations = locs.get_locations()
    try:
        os.mkdir('./routes')
    except:
        pass

    # Google endpoints
    google_route_url = "https://maps.googleapis.com/maps/api/directions/json"
    # Environment variable to house the API key of me
    google_route_key = os.environ['GOOGLE_ROUTES_KEY']
    # Using "alternatives", we can nearly tripple simulated traffic with only one 
    # web service call.  Let's save them $$$ on API calls. :)
    google_route_args = "&alternatives=true&mode=walking"
    
    # Hard code the timeframe when this supposed traffic happened
    begin_of_day = 1544103000
    end_of_day   = 1544146200
    
    # Get 100 samples
    # and write out each to its own JSON file
    for i in range(1,100):
        # Write our XML to a file
        filename = str(i) + ".json"
        # Starting location
        rand_index = random.randint(0,len(locations) - 1)
        orig_name = locations[rand_index]['name']
        orig_loc  = locations[rand_index]['location']
      
        # Ending Location
        rand_index = random.randint(0,len(locations) - 1)
        dest_name = locations[rand_index]['name']
        dest_loc  = locations[rand_index]['location']
      
        print orig_name + " -> " + dest_name
      
        # TODO: Try / Except here
        # Get our API args situated
        args = {'origin' : orig_loc, 'destination' : dest_loc, 'key' : google_route_key, 'alternatives': 'true', 'mode' : 'walking' }
        encoded_args = urllib.urlencode(args)
        url = google_route_url + "?" + encoded_args
        r   = requests.get( url )
       
        multi_routes = json.loads(r.content)
        multi_routes['user_id'] = random.randint(1, 50)
        multi_routes['path_name'] = orig_name + " to " + dest_name
      
        # Let's append some human readable data into the output from the Google API
        for routes in multi_routes['routes']:
            start_time = random.randint(begin_of_day, end_of_day)
            routes['start_address_name'] = orig_name
            routes['end_address_name'] = dest_name
            routes['start_time'] = start_time
            routes['end_time']   = start_time + routes['legs'][0]['duration']['value']
      
        out = open( "routes/" + filename, "w")
        out.write(json.dumps(multi_routes))
    
if __name__ == "__main__":
    main()
