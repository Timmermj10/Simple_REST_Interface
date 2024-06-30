# Explanation of work:

    location.py uses urllib and json to request and parse the information returned from API requests to ipstack, returning the information as a json object that can be used in an auxiliary CLI tool.

    Other people would use this CLI tool to get information on latitude and longitude values based on a given IP address. This is done by calling 'python location.py {IP ADDRESS}' (note that on some machines you must specify python3, py, py3, etc)

# Security:

    With the free subscription plan on ipstack, https is not supported. This means that the request must be sent as plaintext with http over the network.
    With the request being sent as plaintext, anyone that has access to the network will be able to see every IP address that you request the API with.

    Another note on security, with API keys you need to be careful to not release your own onto public forums. I made this mistake a few years ago and have made it a note to never repeat it. To avoid this, make sure that your key is not stored in a file that will be on the public repository. This can be done by creating a separate file and importing the variable. While also being sure to add this extra file to your .gitignore.
