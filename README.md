# Google Maps API Project
# Overview
This project is an API I coded to scrape information on different businesses on Google Maps. It utilizes Google Places API which allows for $200 of free API calls every month. It consists of two main scripts: one to generate a 10x10 grid of coordinates and another to query the Places API for business information.

# Coordinate Generation (coordinate_generation.R)
The "coordinate_generation.R" script generates a grid of coordinates covering a specified area. It calculates a grid of coordinates within a defined bounding box in latitude and longitude and outputs them to a CSV file. For example, if you were interested in getting every single repair shop for the city New York, you would simply change the NE LAT&LON and SW LAT&LON to be the point to the most North East and the point to the most South West in New York. This is needed because if we just use one cordinate, the API only returns 60 results. Instead by having 100 cordinates with smaller radiuses covering the entire city, we then can generate 60*10*10 unique business returned by the API.

Parameters:
NORTHEAST_LAT: Latitude for the northeast most point in the area of interest (New York City in this case).
NORTHEAST_LNG: Longitude for the northeast most point in the area of interest.
SOUTHWEST_LAT: Latitude for the southwest most point in the area of interest.
SOUTHWEST_LNG: Longitude for the southwest most point in the area of interest.
DESIRED_GRID_LENGTH: Desired grid length (e.g., 10x10 grid). The larger the grid i.e 100x100 the smaller the radius needs to be set in the py script
API Script (api_script.py)
The api_script.py utilizes the generated coordinates to query the Google Places API for business information within a specified radius.

# Parameters:
csv_file_path: Path to the CSV file containing the generated coordinates written by the first R script.
radius: Radius around each coordinate to search for businesses (in meters). *(Set this paramater so that for the grid of cordinates the radiuses are slighly overlapping)*
type: Type of business to search for. (Utilize Google Places "Place Type" to search for specific businesses)
key: Your API key from Google Places. 

# Usage:
Run coordinate_generation.R to generate a grid of coordinates for a desired city/location and save them to a CSV file.
Update the parameters in api_script.py with your desired values. (Radius, Business Type, and Data to be collected)
Run api_script.py to query the Google Places API and retrieve business information for each coordinate.
The results will be saved to a JSON file named places.json.

#Notes
Ensure you have a valid API key from Google Places and proper permissions set up for API usage.
Be mindful of API rate limits to avoid being blocked or rate-limited.
Remember to replace placeholder values with your actual data before running the scripts.
