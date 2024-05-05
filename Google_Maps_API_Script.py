import requests
import time
import json
import csv

csv_file_path = r"C:\Users\Tyler\Downloads\cordinates.csv"  # Replace with your actual file path
with open(csv_file_path, "r") as csvfile:  #100 unique cordinates
    reader = csv.reader(csvfile)
    locations = [",".join(row) for row in reader] 

radius = 1609.34  # Replace with desired radius in meters (1 mile radius)
type = "car_repair"  # Replace with desired business type
key = ""  # Replace with your API key

# List to store place IDs
place_ids = []

# Iterate through each location
for location in locations:
    print(f"Processing location: {location}")
    pagetoken = None  # Reset pagetoken for each location
    
    while True:
        # Add delay to avoid hitting query rate limit
        time.sleep(2)

        # Send request to Places API and retrieve results
        url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&type={type}&key={key}&pagetoken={'' if pagetoken is None else pagetoken}"
        response = requests.get(url)
        results = response.json().get("results", [])
        place_ids += [result["place_id"] for result in results]

        # Check if there are more results to retrieve
        pagetoken = response.json().get("next_page_token")
        if not pagetoken:
            break

# Remove duplicate place IDs
place_ids = list(set(place_ids))
print(f"Total unique place IDs: {len(place_ids)}")

# Retrieve detailed information for each place using Place Details API
data = []

for place_id in place_ids:
    print(f"Retrieving details for place ID: {place_id}")
    # Add delay to avoid hitting query rate limit
    time.sleep(2)
    # Send request to Place Details API and retrieve result
    url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=name,formatted_address,formatted_phone_number,rating,review,opening_hours&key={key}"
    response = requests.get(url)
    result = response.json().get("result")
    if result:
        data.append(result)

# Save results to a JSON file
with open("places.json", "w") as outfile:
    json.dump(data, outfile)

# Print results
print(f"Total detailed information retrieved: {len(data)}")
print(data)