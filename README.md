# GEE-Data-Extraction
<br />

The objective of this project is to extract satellite imagery data for a Pakistan over the past year (2024) using Google Earth Engine (GEE), and process the data to calculate **NDVI (Normalized Difference Vegetation Index is a metric used to measure the health and density of vegetation)** and store the processed data in a PostgreSQL database for further analysis. Visualize the data in a map using NDVI color scheme.
<br /><br /><br />


![ETL Diagram](https://github.com/zaid638/GEE-Data-Extraction/blob/main/GEE%20ETL%20Diagram.png)
<br /><br /><br />

## Tools and Technologies Used
<br />

1. **Google Earth Engine (GEE):** For accessing and processing satellite imagery data.
2. **Python:** To write scripts for interacting with GEE and PostgreSQL. And visualize the data.
3. **PostgreSQL:** To store the extracted data.
4. **Libraries:**
   - earthengine-api
   - psycopg2
   - pandas
   - datetime
   - Folium
<br /><br />
