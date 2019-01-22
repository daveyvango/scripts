# Simulating student traffic on campus.  This type of data could be used
# for a variety of purposes like path improvement targeting, safety checkpoints, info booth placement
# and more.  Let's use Google Routes API to act as though
# foot traffic has actually happened on these paths.

import random
import json
import requests
import urllib
import os

def main():
    # TODO: Externalize this
    # Adding a bunch of campus locations for start and end points
    locations = [
        {
            "location": "217 Normal Rd, DeKalb, IL 60115",
            "name": "Founders Memorial Library"
        },
        {
            "location": "1525 W Lincoln Hwy, DeKalb, IL 60115",
            "name": "Huskie Stadium"
        },
        {
            "location": "New Residence Hall West, 1175 Lincoln Dr N, DeKalb, IL 60115",
            "name": "New Residence Hall West"
        },
        {
            "location": "Holmes Student Center, DeKalb, IL 60115",
            "name": "Holmes Student Center"
        },
        {
            "location": "385 Wirtz Dr, DeKalb, IL 60115",
            "name": "ELS Language Centers - DeKalb"
        },
        {
            "location": "399 Gilbert Dr, DeKalb, IL 60115",
            "name": "Gilbert Hall"
        },
        {
            "location": "218 Normal Rd, DeKalb, IL 60115",
            "name": "Davis Hall"
        },
        {
            "location": "100 Normal Rd, DeKalb, IL 60115",
            "name": "NIU Computer Science Building"
        },
        {
            "location": "202 Normal Rd, DeKalb, IL 60115",
            "name": "LaTourette Hall"
        },
        {
            "location": "Stevens Bldg DeKalb, IL 60115",
            "name": "Stevens Building"
        }, 
        {
            "location": "Neptune North Hall, 750 Lucinda Ave, DeKalb, IL 60115",
            "name": "Neptune Hall Central"
        },
        {
            "location": "Neptune West Hall, 800 Lucinda Ave, DeKalb, IL 60115",
            "name": "Neptune Hall East"
        },
        {
            "location": "Neptune North Hall, 750 Lucinda Ave, DeKalb, IL 60115",
            "name": "Neptune Hall North"
        },
        {
            "location": "Neptune West Hall, 800 Lucinda Ave, DeKalb, IL 60115",
            "name": "Neptune Hall West"
        },
        {
            "location": "Adams Hall DeKalb, IL 60115",
            "name": "Adams Hall"
        },
        {
            "location": "Wirtz Hall DeKalb, IL 60115",
            "name": "Wirtz Hall"
        },
        {
            "location": "McMurry Hall Dekalb Il 60115",
            "name": "McMurry Hall"
        },
        {
            "location": "Anderson Hall DeKalb, IL 60115",
            "name": "Anderson Hall"
        },
        {
            "location": "590 Garden Rd, DeKalb, IL 60115",
            "name": "Engineering Building"
        },
        {
            "location": "Chick Evans Field House, DeKalb, IL 60115",
            "name": "Chick Evans Field House"
        },
        {
            "location": "325 N Annie Glidden Rd, DeKalb, IL 60115",
            "name": "Student Recreation Center"
        },
        {
            "location": "Stevenson Towers DeKalb, IL 60115",
            "name": "Stevenson Towers North"
        },
        {
            "location": "Stevenson Towers DeKalb, IL 60115",
            "name": "Stevenson Towers South"
        },
        {
            "location": "New Residence Hall Community Center DeKalb, IL 60115",
            "name": "New Residence Hall Community Center"
        },
        {
            "location": "New Residence Hall Community Center DeKalb, IL 60115",
            "name": "New Residence Hall East"
        },
        {
            "location": "1250 N Grant Dr, DeKalb, IL 60115",
            "name": "Grant Towers North"
        },
        {
            "location": "1250 N Grant Dr, DeKalb, IL 60115",
            "name": "Grant Towers South"
        },
        {
            "location": "Barsema Hall DeKalb, IL 60115",
            "name": "Barsema Hall"
        },
        {
            "location": "901 Lucinda Ave Suite T, DeKalb, IL 60115",
            "name": "Pita Pete's"
        },
        {
            "location": "1015 W Lincoln Hwy, DeKalb, IL 60115",
            "name": "Starbucks"
        },
        {
            "location": "805 W Lincoln Hwy, DeKalb, IL 60115",
            "name": "McDonald's"
        },
        {
            "location": "Montgomery Hall, DeKalb, IL 60115",
            "name": "Montgomery Hall"
        },
        {
            "location": "116 altgeld hall, DeKalb, IL 60115",
            "name": "Altgeld Hall"
        },
        {
            "location": "Swen Parson Hall, DeKalb, IL 60115",
            "name": "Swen Parson Hall"
        },
        {
            "location": "Faraday Hall, DeKalb, IL 60115",
            "name": "Faraday Hall"
        }
    ]

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
