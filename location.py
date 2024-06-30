import sys
import urllib.request
import json
from apikey import access_key

base = 'http://api.ipstack.com/'
ip = ''

# Get the IP address from the command line
try:
    ip = sys.argv[1]
except:
    print('Error: Please pass an IP address as an argument')
    sys.exit(1)

# Format the URL for the API request
url = f'{base}{ip}?access_key={access_key}'

# Send the API request over the network
try:
    with urllib.request.urlopen(url) as request:
        data = request.read()
        data = json.loads(data)
        
        # Format the output latt/long values
        output = {
            'latitude': data['latitude'],
            'longitude': data['longitude']
        }
        output = json.dumps(output)
        print(output)
except:
    print('Error: Unable to retrieve API response. Please check the IP address and try again')
    sys.exit(1)