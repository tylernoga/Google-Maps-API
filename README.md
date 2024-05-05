# Google Maps API Project
# Overview
This project is an API I coded to scrape information on different businesses on Google Maps. It utilizes Google Places API which allows for $200 of free API calls every month. It consists of two main scripts: one to generate a 10x10 grid of coordinates and another to query the Places API for business information.

# Example
This is an example of utilizing this API. I scraped every repair shop in a 30 mile radius of New York and saved the shops data as a JSON file, which I then uploaded to google maps. 

![google maps](https://github.com/tylernoga/Google-Maps-API/assets/114703388/87a620ff-dde0-4287-90a2-1bc0763777ef)

You then have the ability to click on every point (repair shop) to get information about that shop
![google maps 1](https://github.com/tylernoga/Google-Maps-API/assets/114703388/30f2036c-fd9e-462c-a7db-ff94dcebf157)

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
- csv_file_path: Path to the CSV file containing the generated coordinates written by the first R script.
- radius: Radius around each coordinate to search for businesses (in meters). *(Set this paramater so that for the grid of cordinates the radiuses are slighly overlapping)*
- type: Type of business to search for. (Utilize Google Places "Place Type" to search for specific businesses)
- key: Your API key from Google Places. 

# Usage:
Run coordinate_generation.R to generate a grid of coordinates for a desired city/location and save them to a CSV file.
Update the parameters in api_script.py with your desired values. (Radius, Business Type, and Data to be collected)
Run api_script.py to query the Google Places API and retrieve business information for each coordinate.
The results will be saved to a JSON file named places.json.

#Notes
Ensure you have a valid API key from Google Places and proper permissions set up for API usage.
Be mindful of API rate limits to avoid being blocked or rate-limited.
Remember to replace placeholder values with your actual data before running the scripts.

# Use Cases

Market Research and Analysis:
- Identifying Trends: By scraping business types from Google Maps, market researchers can gain insights into emerging trends in various industries. This data can reveal shifts in consumer preferences, popular business models, and areas with high demand for specific services or products.
- Competitor Analysis: Understanding the landscape of businesses within a particular sector is crucial for competitive analysis. Your API script enables users to gather data on competitors operating in a specific geographic area, helping businesses make informed decisions about market positioning and strategy.
Business Expansion and Location Planning:
-Site Selection: Businesses looking to expand or open new locations can use the scraped data to identify optimal locations based on the presence of similar businesses in the area. This information can inform decisions regarding target demographics, competition density, and market saturation.
-Market Entry Strategy: For companies entering new markets, knowing the distribution of existing business types can provide valuable insights into local consumer preferences and competition intensity. This knowledge can guide the development of tailored marketing strategies and product offerings.
Local SEO and Digital Marketing:
- Keyword Research: Scraped data on prevalent business types can serve as a foundation for keyword research in local search engine optimization (SEO) and digital marketing campaigns. Understanding commonly searched terms related to specific industries can help businesses optimize their online presence and target relevant audiences effectively.
- Content Strategy: Businesses can leverage insights from your API script to develop content strategies tailored to local market interests and needs. By aligning content with popular business categories in a given area, organizations can enhance their visibility and relevance in local search results.
Urban Planning and Development:
- Community Planning: City planners and policymakers can utilize the scraped data to inform decisions related to zoning regulations, infrastructure development, and urban revitalization efforts. Understanding the distribution of businesses across different sectors can aid in creating vibrant, diverse communities that meet the needs of residents and visitors alike.
- Economic Development: By analyzing patterns of business activity within a city or region, economic development agencies can identify opportunities for targeted investment and support initiatives that foster entrepreneurship and job creation in key industries.
Academic Research and Data Analysis:
- Socioeconomic Studies: Researchers studying urban dynamics, economic inequality, and regional development can utilize the scraped data to investigate correlations between business distributions and demographic factors. This information can contribute to academic research aimed at understanding the drivers of economic growth and social change.
- Data Visualization: The scraped data can be visualized through maps, charts, and graphs to illustrate spatial patterns and trends, making complex datasets more accessible and comprehensible for analysis and presentation purposes.
