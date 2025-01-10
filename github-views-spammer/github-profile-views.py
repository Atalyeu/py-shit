import requests

url = "" # PLEASE READ STEP 3 IN THE README FILE
NUMBER_OF_REQUESTS = 200

for i in range(1, NUMBER_OF_REQUESTS): 
    r =    requests.get(url)
    print(f"{i} new views")
