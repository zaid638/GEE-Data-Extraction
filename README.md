# GEE-Data-Extraction
<br />

The objective of this project is to extract satellite imagery data for a Pakistan over the past year (2024) using Google Earth Engine (GEE), and process the data to calculate **NDVI (Normalized Difference Vegetation Index is a metric used to measure the health and density of vegetation)** and store the processed data in a PostgreSQL database for further analysis. Visualize the data in a map using NDVI color scheme.
<br /><br /><br />


<!-- ![ETL Diagram](https://github.com/zaid638/GEE-Data-Extraction/blob/main/GEE%20ETL%20Diagram.png) -->
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
<br /><br /><br />


## Steps Involved
<br /><br />


### Step 1: Setup and Initialization
<br />

1. Authenticate and initialize the Google Earth Engine API in Python.
2. Define the Area of Interest (AOI) using geographical coordinates (Pakistan, splitted into provinces).
3. Specify the time range for data extraction (past one year, splitted into months).
<br /><br />


### Step 2: Data Extraction from GEE
<br />

1. Dataset Selection:
   - Used Sentinel-2 surface reflectance data (COPERNICUS/S2_HARMONIZED).
2. Filtering Criteria:
   - Temporal range: January 1, 2024, to December 31, 2024.
   - Spatial range: AOI defined for the specific region (Pakistan).
   - Cloud cover threshold: <20% cloudy pixels.
3. Processing:
   - Computed Normalized Difference Vegetation Index (NDVI) using GEE function:
     NDVI = (B8 - B4) / (B8 + B4)
   - Extracted date and NDVI values (ID, Date, Latitude, Longitude, NDVI).
   - Removed the rows that containing NULL values in NDVI column.
<br /><br />

### Step 3: Handling GEE Query Limitations
<br />

1. Reduced the spatial resolution based on needs (100/1000/1500 meters).
2. Divided the time range into monthly chunks to limit the number of images queried at a time.
3. Filtered images by cloud cover to reduce unnecessary data.
<br /><br />

### Step 4: Data Transformation and Cleaning
<br />

1. Used the Python Pandas library to covert data points into Dataframe.
2. Manually extracted the date from ID.
3. Dropped the rows that had null values in NDVI data.
<br /><br />

### Step 5: Data Export and Storage
<br />

1. Merged the Dataframes (for 1 month data).
2. Created a Database for every province in PostgreSQL.
3. Created tabled for every month in each database.
4. Inserted data into a PostgreSQL database.
5. Created a Data Warehouse that includes all the data.
<br /><br />

### Step 6: Error Handling
<br />

1. Addressed issues such as missing dates in images.
2. Split queries into manageable chunks to avoid exceeding GEE's element limits.
<br /><br /><br />


