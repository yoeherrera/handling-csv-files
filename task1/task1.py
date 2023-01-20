# import needed modules
import requests 
import json  

# url provided
url = "https://swapi.dev/api/vehicles/"

# make request
res = requests.get(url)

# get the text of the request
data = res.text

# transform to json
data_json = json.loads(data)

# select manufacturers without repetition
unique_manufacturers = []
for k in range(len(data_json['results'])):
    manufacturer = data_json['results'][k]['manufacturer']
    # in case of manufacturer not being in list, then added
    if manufacturer not in unique_manufacturers:
        unique_manufacturers.append(manufacturer)
unique_manufacturers

# print the list of first five (5) manufacturers
print("The first five (5) manufacturers are") 
for manufacturer in unique_manufacturers[:5]:
    print(manufacturer)