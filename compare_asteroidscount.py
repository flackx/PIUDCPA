import urllib.request
from cmath import log
import requests
import json
import logging
import logging.config
from configparser import ConfigParser
from datetime import datetime
import yaml

from datetime import datetime, timedelta


# Loading logging configuration
with open('./log_worker.yaml', 'r') as stream:
    log_config = yaml.safe_load(stream)

logging.config.dictConfig(log_config)
# Creating logger
logger = logging.getLogger('root')
logger.info('Asteroid processing service')

# Initiating and reading config values
logger.info('Loading configuration from file')
try:
	config = ConfigParser()
	config.read("/home/s155/files/config.ini")

	nasa_api_key = config.get('nasa', 'api_key')
	nasa_api_url = config.get('nasa', 'api_url')
except:
	logger.exception('')
logger.info('DONE')

if __name__ == "__main__":
    # Getting todays date
    dt = datetime.now()
    request_date = str(dt.year) + "-" + str(dt.month).zfill(2) + "-" + str(dt.day).zfill(2)  
    logger.debug("Generated today's date: " + str(request_date))
    #Getting yesterdays date
    yesterday = dt- timedelta(days=1)
    #Getting date from exaclty a week ago
    weekago = dt- timedelta(days=7)
    #Getting date from exactly a month ago
    monthago = dt- timedelta(days=30)
    #Getting date from exactly a year ago
    yearago = dt- timedelta(days=365)
    
    #Generating requests
    request_yt = str(yesterday.year) + "-" + str(yesterday.month).zfill(2) + "-" + str(yesterday.day).zfill(2)  
    logger.debug("Generated yesterday's date: " + str(request_yt))
    request_week = str(weekago.year) + "-" + str(weekago.month).zfill(2) + "-" + str(weekago.day).zfill(2)  
    logger.debug("Generated 1week ago date: " + str(request_week))
    request_month = str(monthago.year) + "-" + str(monthago.month).zfill(2) + "-" + str(monthago.day).zfill(2)  
    logger.debug("Generated a month ago date: " + str(request_month))
    request_year = str(yearago.year) + "-" + str(yearago.month).zfill(2) + "-" + str(yearago.day).zfill(2)  
    logger.debug("Generated a year ago date: " + str(request_year))

    
    # Requesting info from NASA api
    r = requests.get(nasa_api_url + "rest/v1/feed?start_date=" + request_date + "&end_date=" + request_date + "&api_key=" + nasa_api_key)
    #yesterday
    r1 = requests.get(nasa_api_url + "rest/v1/feed?start_date=" + request_yt + "&end_date=" + request_yt + "&api_key=" + nasa_api_key)
    #1 week ago
    r2 = requests.get(nasa_api_url + "rest/v1/feed?start_date=" + request_week + "&end_date=" + request_week + "&api_key=" + nasa_api_key)
    #month ago  
    r3 = requests.get(nasa_api_url + "rest/v1/feed?start_date=" + request_month + "&end_date=" + request_month + "&api_key=" + nasa_api_key)
    #year ago
    r4 = requests.get(nasa_api_url + "rest/v1/feed?start_date=" + request_year + "&end_date=" + request_year + "&api_key=" + nasa_api_key)
    
    #empty array for later
    arr=[]
    #Array with request values for later
    rvalues=[r,r1,r2,r3,r4]
    #For cycle that goes trough the request values and finds and saves the count of asteroids.
    for x in rvalues:
        if x.status_code == 200:
            json_data = json.loads(x.text)
            ast_safe = []
            ast_hazardous = []
                # Counts asteroids for given date
            if 'element_count' in json_data:
                y = int(json_data['element_count'])
                arr.append(y)
                
    diroftimes = {
        "Today": arr[0],
        "Yesterday": arr[1],
        "A week ago": arr[2],
        "A month ago": arr[3],
        "A year ago": arr[4],
    }
    arr.sort()
    print("Asteroid count:")
    print(diroftimes)
    print("Asteroid count sorted in order: "+str(arr))
    
    
    
    